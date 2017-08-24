#!/usr/bin/env python
#encoding=gbk


import sys,pdb,time,json,urllib,urllib2
import BaseHTTPServer
from BaseHTTPServer import *
from SocketServer import ThreadingMixIn


def webCommand(url, to):
	try:
		fp = urllib2.urlopen(url, timeout=to)
		ln = fp.readline()
		fp.close()
		resp = json.loads(ln,encoding="utf-8")
		return (True,resp)
	except:
		resp = ""
		return (False,resp)

class MyHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		print "POST"

		post_data_len = 0
		for header in self.headers:
			if header.lower() == "content-length":
				post_data_len = int(self.headers[header])

		post_data = ""
		if post_data_len > 0:
			post_data = self.rfile.read(post_data_len)
			if len(post_data) != post_data_len:
				self.send_response(501, 'content-length error1')
				return
		else:
			self.send_response(501, 'content-length error2')
			return

		post_data = urllib.unquote(post_data)
		cash_info = post_data.split('&')

		cash_items = {}
		for item in cash_info:
			(key,value) = item.split('=')
			cash_items[key]=value

		flag = False
		resp = ""
		print cash_items

		post_data = urllib.urlencode(cash_items)
		(flag,resp)=webCommand("http://127.0.0.1:8072/xxx?%s" % post_data, 30)
		
		print flag, resp
		if not flag:
			self.send_response(501, 'server error')
			return
		else:
			self.send_response(200, resp)
			return

	def do_GET(self):
		print "GET"

class ThreadingServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
	pass


def init():
	HandlerClass = MyHandler
	ServerClass = BaseHTTPServer.HTTPServer
	Protocol = "HTTP/1.0"

	server_address = ('0.0.0.0', 4545)
	HandlerClass.protocol_version = Protocol
	
	httpd = ThreadingServer(server_address, HandlerClass)
	sa = httpd.socket.getsockname()

	print "Server HTTP on", sa[0], "port", sa[1], "..."
	
	httpd.serve_forever()

def main():
	init()

if __name__ == "__main__":
	main()

