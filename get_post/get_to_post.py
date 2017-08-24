#!/usr/bin/env python
#encoding=gbk


import sys,pdb,time,json,urllib,urllib2
import BaseHTTPServer
from BaseHTTPServer import *
from SocketServer import ThreadingMixIn


def webPostCommand(url, data, to):
	try:
		request = urllib2.Request(url, data=data)
		response = urllib2.urlopen(request,timeout=to)
		ln = response.readline()
		response.close()
		print "post ret:" + ln
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
		login_info = post_data.split('&')

		login_items = {}
		for item in login_info:
			(key,value) = item.split('=')
			login_items[key]=value
		print "----------------------------------"
		print login_items
		print "----------------------------------"
		jsonData = json.dumps(login_items)
		self.wfile.write(jsonData)
		#self.send_response(200,"OK")
	def do_GET(self):
		print "GET"
		if '?' in self.path:
			query = urllib.splitquery(self.path)
			print query
			queryParams = {}
			if query[1]: #接收get参数
				for qp in query[1].split('&'):
					kv = qp.split('=')
					queryParams[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
			print queryParams
			#将现有参数POST出去
			params = urllib.unquote(query[1])
			flag = False
			resp = ""
			(flag,resp)=webPostCommand("http://127.0.0.1:4545/", params, 30)
			print flag, resp
			if not flag:
				self.send_response(501, 'server error')
				return
			else:
				self.send_response(200, resp)
				return
		else:
			self.send_response(501, "can't find get params")
			return

class ThreadingServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
	pass


def init():
	HandlerClass = MyHandler
	ServerClass = BaseHTTPServer.HTTPServer
	Protocol = "HTTP/1.0"

	server_address = ('0.0.0.0', 4545)
	HandlerClass.protocol_version = Protocol
	#httpd = ServerClass(server_address, HandlerClass)
	
	httpd = ThreadingServer(server_address, HandlerClass)
	sa = httpd.socket.getsockname()

	print "Server HTTP on", sa[0], "port", sa[1], "..."
	
	httpd.serve_forever()

def main():
	init()

if __name__ == "__main__":
	main()

