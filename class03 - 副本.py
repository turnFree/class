
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=20) #设置超时
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except: #异常处理
        return "产生异常"


if __name__ == '__main__':
    url = "https://www.baidu.com"
    print(getHTMLText(url))
