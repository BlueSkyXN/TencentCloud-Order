import requests
url = "https://api.cybree.com/v1/instances"
cookies = ""
headers = {
    "Cookie" : cookies,
    "Content-Type" : "application/json",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

data = '{"name":"jp01","region":"tyo1","size":"xs-1vcpu-1gb","image":"centos-7-x64","password":"QWIxMjMONTY30A=="}'
respond = requests.post(url, data= data, headers = headers)
print(respond.json())
