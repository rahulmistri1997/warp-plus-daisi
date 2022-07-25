from datetime import datetime
import urllib.request, json, string, random

def getData(uid):
	url = f'https://api.cloudflareclient.com/v0a{randomDigit(3)}/reg'
	install_id = randomString(22)
	body = {
		"key": "{}=".format(randomString(43)),
		"install_id": install_id,
		"fcm_token": "{}:APA91b{}".format(install_id, randomString(134)),
		"referrer": uid,
		"warp_enabled": False,
		"tos": datetime.now().isoformat()[:-3] + "+02:00",
		"type": "Android",
		"locale": "es_ES"
	}
	data = json.dumps(body).encode('utf8')
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Host': 'api.cloudflareclient.com',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.12.1'
	}
	req = urllib.request.Request(url, data, headers)
	if proxy_enabled:
		if len(custom_proxy) == 0:
			try:
				with urllib.request.urlopen('https://api.getproxylist.com/proxy?protocol[]=http&minDownloadSpeed=400&anonymity[]=high%20anonymity&allowsCustomHeaders=1&allowsPost=1&allowsHttps=1&maxSecondsToFirstByte=1') as response:
					proxy = json.loads(response.read())
					req.set_proxy("{}:{}".format(proxy["ip"], proxy["port"]), proxy["protocol"])
			except:
				print("Failed to set proxy from getproxylist.com.")
		else:
			try:
				req.set_proxy(custom_proxy["host"], custom_proxy["protocol"])
			except:
				print("Failed to set custom proxy.")
	try:
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return True if status_code == 200 else False
	except Exception as e:
		print(e)
		return False

def getjson(uid):
	referrer = uid
	for x in range(3):
		success = getData(referrer)
		if success:
			return "Successfully Added 1GB"

	return "Error in Adding 1 GB"