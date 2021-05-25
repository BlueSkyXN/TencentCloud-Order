import requests
url = "https://cloud.tencent.com/act/common/ajax/dianshi?uin=【UID】&csrfCode=【csrfCode】"
cookies = "【随便腾讯云控制台的cookies】"
headers = {
    "Cookie" : cookies,
    "Content-Type" : "application/x-www-form-urlencoded",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

data = 'action=checkActAvailable&data={"activity_id":12772,"goods":[{"act_id":17184610522473,"type":"voucher"}]}'
respond = requests.post(url, data= data, headers = headers)
print(respond.json())