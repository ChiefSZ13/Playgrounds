import requests
import time
import json
from datetime import datetime
import time

def get_current_timestamp():
    # Get the current datetime
    now = datetime.now()
    
    # Convert the current datetime to a timestamp (seconds since the Unix epoch)
    timestamp = int(datetime.timestamp(now))
    
    return timestamp

def get_current_timestamp_ms():
    return int(time.time() * 1000)




body = {
    "buyer": {
        "id": "725455862197841920",
        "openId": "oOya25PUKZ3CqVl6iw1AgEuXaur4",
        "mobile": "18339901263",
        "credentialNo": "152126197505010315",
        "credentialType": "0",
        "nickName": "朱卫强"
    },
    "couponCode": "",
    "startDate": "2024-03-29",
    "endDate": "2024-03-29",
    "addTickets": [
        {
            "modelCode": "MP2022070117150305046",
            "amount": 1,
            "parentModelCode": "MP2022070117025856157",
            "spiltStartTime": "06:00",
            "spiltEndTime": "12:00",
            "fsName": "上午",
            "realName": "T",
            "needConfirm": "F",
            "orderCertAuthList": [
                {
                    "realName": "朱卫强",
                    "certNo": "152126197505010315",
                    "certType": 0,
                    "ticketName": "标准票"
                }
            ]
        },
        {
            "modelCode": "MP2022082418002114289",
            "amount": 1,
            "parentModelCode": "MP2022070117025856157",
            "spiltStartTime": "06:00",
            "spiltEndTime": "12:00",
            "fsName": "上午",
            "realName": "T",
            "needConfirm": "F",
            "orderCertAuthList": [
                {
                    "realName": "朱卫强",
                    "certNo": "152126197505010315",
                    "certType": 0,
                    "ticketName": "标准票"
                }
            ]
        }
    ],
    "saveOrders": [
        {
            "ticketName": "门票全价票",
            "price": 40,
            "amount": 1,
            "modelCode": "MP2022070117025856157",
            "itemId": "75821",
            "wayType": "6",
            "fsName": "上午",
            "orderCertAuthList": [
                {
                    "realName": "朱卫强",
                    "certType": 0,
                    "certNo": "152126197505010315"
                }
            ],
            "needConfirm": "F",
            "spiltStartTime": "06:00",
            "spiltEndTime": "12:00"
        }
    ],
    "wayType": "6",
    "orderType": "park",
    "merchantInfoId": "2655"
}

json1 = json.dumps(body, separators=(',', ':'), ensure_ascii=False).encode('utf-8')



while True:
    url = "https://lotswap.dpm.org.cn/dubboApi/trade-core/tradeCreateService/create?sign=fc2188f3d4c1ed290889556eef616250&timestamp=1711372206703"
    headers = {
    'Host': 'lotswap.dpm.org.cn',
    'Connection': 'keep-alive',
    'Content-Length': '1237',  # This might be automatically adjusted by requests
    'ts': '1711372207',
    'mpOpenId': 'oOya25ATFeCCxWS2VwBzgSMOJFqE',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
    'access-token': 'eyJhbGciOiJIUzUxMiJ9.eyJ1IjoiNzI1ODA3Mjk1Mzg4NTY1NTA0IiwidCI6IjAiLCJleHAiOjE3MTEzNzg0NjF9.PQ0-bNV5hMFCGzn-0i8_XhPo45mJsxPWq3xhFcqKNFdsHETwPlGHP0oDax1jnoCZbwXejGdTzhKStt2VMbWuHw',
    'Content-Type': 'application/json',
    'xweb_xhr': '1',
    'app': 'app_qqmap_tickets',
    'mpDeviceToken': 'v2:wqkBRTXcMLQ+8UrmFcAxACwpww3AOXHv/AzJvuRLcNqSVDKq44js6tJ+BKzWgrvTsrZFvTzJxQURZHJ6jb0C9N4nsNrUWZ2U5Tlj3SauyiBfEiaBbN/TSFhY2UXt6COUO2L4A07Rt8WPlOftGUCYlyKpdR1MrVyUtQmn5y5RX8RlVdj0LW6hJnlbTlmouZ7Fuji89duJIkaC+YfhwxJz7mlVQ6MHwDw=',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://servicewechat.com/wx13169e68a3e63e55/135/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    response = requests.post(url, headers=headers, data=json1)
    print(response.text)
    time.sleep(1)