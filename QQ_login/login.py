#encoding:utf8
import urllib
import urllib2
import re

import cookielib
import sys


global_cookie_jar = cookielib.CookieJar();

class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        # print "weifei response " 
        # print code
        # print msg 
        # print hdrs
        # only add this line to stop 302 redirection.
        if code == 302: return response

        if not (200 <= code < 300):
            response = self.parent.error(
                'http', request, response, code, msg, hdrs)
        return response

    https_response = http_response


def GetToken_Qun():
	ret = {}
	url="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=715030901&daid=73&hide_close_icon=1&pt_no_auth=1&s_url=https%3A%2F%2Fqun.qq.com%2Fmember.html"
	try:
		# req=urllib2.Request(url=url,headers=headers)
		cj = cookielib.CookieJar();
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
		urllib2.install_opener(opener);
		resp = urllib2.urlopen(url);
		for _, cookie in enumerate(cj):
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		# print ret
	except Exception as e:
		print e
	pass
	return ret
def GetToken():
	ret = {}
	url="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0"

	try:
		# req=urllib2.Request(url=url,headers=headers)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		resp = urllib2.urlopen(url);
		for _, cookie in enumerate(global_cookie_jar):
			#print cookie
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		#print ret
		#print resp
	except Exception as e:
		print e
	pass
	return ret

def GetAccount(token, uikey):
	# 其实就是 4301
	port=4301
	url='https://localhost.ptlogin2.qq.com:'+str(port)+'/pt_get_uins?callback=ptui_getuins_CB&r=0.39923783252274414&pt_local_tk='+token
	
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Cookie':'pt_local_token='+token+';uikey='+uikey+';',
	'Host':'localhost.ptlogin2.qq.com:4301',
	'Referer':'https://xui.ptlogin2.qq.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	try:
		req=urllib2.Request(url=url,headers=headers)
		result=urllib2.urlopen(req).read()
		#print result
		result=[re.compile(r'uin":"(\d+)"').findall(result),re.compile(r'nickname":"([^"]+)"').findall(result)]
		return result
	except Exception as e:
		print e
	return []
def GetAccount_Qun(token):
	# 其实就是 4301
	port=4301
	url='https://localhost.ptlogin2.qq.com:'+str(port)+'/pt_get_uins?callback=ptui_getuins_CB&r=0.39923783252274414&pt_local_tk='+token
	
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Cookie':'pt_local_token='+token,
	'Host':'localhost.ptlogin2.qq.com:4301',
	'Referer':'https://xui.ptlogin2.qq.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	try:
		req=urllib2.Request(url=url,headers=headers)
		result=urllib2.urlopen(req).read()
		print result
		result=[re.compile(r'uin":"(\d+)"').findall(result),re.compile(r'nickname":"([^"]+)"').findall(result)]
		return result
	except Exception as e:
		i+=1
	return []
def Getaccount_Old():
	# 其实1个QQ就是 4301
	port=['4300','4301','4302','4303','4304','4305','4306','4307','4308']
	i=0
	
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Cookie':'RK=0I2uxizPSc; LW_sid=q1f4I9v7k5D7R6O5e4S9p7P8V1; LW_uid=q1Z419f7X5k7n6o5A449A708K2; pgv_pvi=5160215552; tvfe_boss_uuid=d2e9e2992c2f6b14; eas_sid=61Z57067j5p3m9G2x7s9S3d2J6; pac_uid=1_123456789; ptcz=18cfc32c59a21faa22f4c97613a01e184bd5ed3838c42b8d0ac4c41b76873fe9; o_cookie=123456789; pgv_pvid=9730655232; pt2gguin=o0123456789; _qpsvr_localtk=1527494364831; pgv_si=s3689689088; pgv_info=ssid=s250026112; confirmuin=0; ptdrvs=gzHJNsKwyLge2eJpGUpPEsyTJs02UlEErMI1rTCOTl8_; ptvfsession=99a88037b2b433ab61922b20b970bb64c5ea90bc19cb04c8cbe0ef5fbbbb91efef5eefbb321ef3775d04b1301e840b1fce347b7eea0d121a; ptisp=ctc;ETK=; skey=@k8jlvoMlF; ptnick_123456789=e5ad99e98791e58589; _qz_referrer=i.qq.com; pt_login_sig=rJ2-e-RdO-U1BKb64PgKp1WbCqOtwdxctdpenMQXMnGLxG2ZrAUisGboQlV5rlOf; pt_clientip=ca667d47e5b1f515; pt_serverip=86930abf06592ed7; pt_local_token=-1909176059; uikey=b01f2c4333cd59b37cfcca5f8dd2e20f50d17ba13cac145b6ae7d324d3db476a; pt_guid_sig=cf3d82b3651d1715cf4d1fab6d4a32d404e1aea65c3081f6d8ef2fe8e4e4b820; pt_recent_uins=c4ef4c627886a903aec329578da7cdfad8b1ed0642acf27a117548094cbee3f74d00864bf00874333301d1afb3e56d1221590d2a92c5b064; qrsig=qLA88IWo1bVkCs9O-mKn1Dr7sMUXkbnIUxXPOY70n8i5VmsZ0tZsHl9NqXkrj5zF',
	'Host':'localhost.ptlogin2.qq.com:4301',
	'Referer':'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=0',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	while(i<len(port)):
		try:
			req=urllib2.Request(url='https://localhost.ptlogin2.qq.com:'+port[i]+'/pt_get_uins?callback=ptui_getuins_CB&r=0.39923783252274414&pt_local_tk=-1909176059',headers=headers)
			result=urllib2.urlopen(req).read()
			print result
			result=[re.compile(r'account":"(\d+)"').findall(result),re.compile(r'nickname":"([^"]+)"').findall(result)]
			return result
		except Exception as e:
			i+=1
	return []

def GetClientKey(uin, token):
	port = 4301
	url='https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin='+uin+'&callback=ptui_getst_CB&r=0.4266647630782271&pt_local_tk='+token
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	#'Cookie':'pt_local_token='+token,
	'Host':'localhost.ptlogin2.qq.com:4301',
	'Referer':'https://xui.ptlogin2.qq.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	ret = {}
	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		req=urllib2.Request(url=url,headers=headers)
		resp = urllib2.urlopen(req);
		for _, cookie in enumerate(global_cookie_jar):
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		# print ret
	except Exception as e:
		print e
	pass
	return ret

def Jump(uin, token, clientkey):
	url='https://ssl.ptlogin2.qq.com/jump?clientuin='+uin+'&keyindex=9&pt_aid=549000912&daid=5&u1=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_local_tk='+token+'&pt_3rd_aid=0&ptopt=1&style=40'
	headers={
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	#'Cookie':'pt_local_token='+token+';clientkey='+clientkey+';uin='+uin+';',
	'Host':'ssl.ptlogin2.qq.com',
	'Referer':'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	ret = {}
	ret_url = ""
	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		req=urllib2.Request(url=url,headers=headers)
		resp = urllib2.urlopen(req).read();

		#print resp.info();
		for _, cookie in enumerate(global_cookie_jar):
			#print cookie
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		#print "->"+resp
		tt = resp.split('\', \'')
		ret_url = tt[1]
		return ret, ret_url
	except Exception as e:
		print e
	return ret, ret_url

def Jump2(url):

	headers={
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Referer':'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	ret = {}

	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		req=urllib2.Request(url=url,headers=headers)
		resp = urllib2.urlopen(req).read();
		for _, cookie in enumerate(global_cookie_jar):
			#print cookie
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		#print ret
		#print "Jump2 resp->"+resp
	except Exception as e:
		print e
	pass
	return ret
def Login(uin):
	
	url = 'https://user.qzone.qq.com/'+uin
	headers={
	#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	#'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}
	ret = {}
	qzonetokens = ""

	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		req=urllib2.Request(url=url,headers=headers)
		resp = urllib2.urlopen(req).read();
		for _, cookie in enumerate(global_cookie_jar):
			#print cookie
			tt = str(cookie).split(' ')
			key_value = str(tt[1]).split('=')
			ret[key_value[0]] = key_value[1]
		# print ret
		#print "Login resp->"+resp
		re_info = re.compile('window.g_qzonetoken.*?try{return.*?\"(.*?)\";}', re.S)
		qzonetokens = re.findall(re_info, resp)[0]
		#print qzonetokens
	except Exception as e:
		print e
	return ret, qzonetokens


def LongToInt(value):  
    if isinstance(value, int):
        return int(value)
    else:
        return int(value & sys.maxint)
def LeftShiftInt(number, step):  
    if isinstance((number << step), long):
        return int((number << step) - 0x200000000L)
    else:
        return int(number << step)
def getOldGTK(skey):
    a = 5381
    for i in range(0, len(skey)):
        a = a + LeftShiftInt(a, 5) + ord(skey[i])
        a = LongToInt(a)
    return a & 0x7fffffff

def getNewGTK(p_skey, skey, rv2):
    b = p_skey or skey or rv2
    a = 5381
    for i in range(0, len(b)):
        a = a + LeftShiftInt(a, 5) + ord(b[i])
        a = LongToInt(a)
    return a & 0x7fffffff


def ShuoShuo(uin, g_tk, qzonetoken, con):
	url="https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_publish_v6?qzonetoken="+qzonetoken+"&g_tk="+g_tk
	headers={
		#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		#'Accept-Language':'zh-CN,zh;q=0.9',
		'Content-Type': 'application/x-www-form-urlencoded',
		#'Connection': 'keep-alive',
		#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
	}

	formate = {
	    "syn_tweet_verson": '1',
		"paramstr": '1',
		"pic_template": "",
		"richtype": "",
		"richval": "",
		"special_url": "",
		"subrichtype": "",
		"who": '1',
		"con": con,
		"feedversion": '1',
		"ver": '1',
		"ugc_right": '1',
		"to_sign": '0',
		"hostuin": uin,
		"code_version": '1',
		"format": "fs",
		"qzreferrer": "https://user.qzone.qq.com/"+uin,
	}
	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(global_cookie_jar));
		urllib2.install_opener(opener);
		req=urllib2.Request(url=url, headers=headers, data = urllib.urlencode(formate))
		resp = urllib2.urlopen(req).read();
		#print resp
		#for _, cookie in enumerate(global_cookie_jar):
		#	#print cookie
		#	tt = str(cookie).split(' ')
		#	key_value = str(tt[1]).split('=')
		#	ret[key_value[0]] = key_value[1]
		# print ret
		#print "Login resp->"+resp
		#re_info = re.compile('window.g_qzonetoken.*?try{return.*?\"(.*?)\";}', re.S)
		#qzonetokens = re.findall(re_info, resp)[0]
		#print qzonetokens
	except Exception as e:
		print "ShuoShuo:"+str(e)

if __name__ == '__main__':
	cookie = GetToken()
	#print cookie
	
	token = cookie["pt_local_token"]
	uikey = cookie["uikey"]
	#print token
	result = GetAccount(token, uikey)

	#print result
	if(result==[]):
		print "当前没有登录qq"
	else:
		num=len(result[0])
		print "当前登录了"+repr(num)+"个QQ"
		for i in range(num):
			uin = result[0][i]
			nickname = result[1][i]
			print "uin:"+uin
			print "昵称:"+nickname
			ret = GetClientKey(uin, token)
			#print ret
			clientkey = ret["clientkey"]
			ret, new_url= Jump(uin, token, clientkey)
			#print ret
			#print new_url
			#print global_cookie_jar
			Jump2(new_url)
			#print ret
			ret, qzonetokens = Login(uin)
			#print ret["p_skey"], ret["skey"], qzonetokens
			p_skey = ret["p_skey"]
			skey = ret["skey"]
			rv2 = ""
			g_tk = str(getNewGTK(p_skey, skey, rv2))
			con = "看片+Q"+str(uin) + "\r\n\r\n嘤嘤嘤\r\n"
			ShuoShuo(uin, g_tk, qzonetokens, con)


