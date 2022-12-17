from flask import Flask
import requests



app = Flask(__name__)

http_proxy = "http://elpibe12221:zcW77HwYxEJr5Zzh@proxy.packetstream.io:31112"
https_proxy = "http://elpibe12221:zcW77HwYxEJr5Zzh@proxy.packetstream.io:31112"
url = "https://www.guadeloupe.gouv.fr/booking/create/12828/0"
proxyDict = {
    "http": http_proxy,
    "https": https_proxy,
}

def main():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"'}
        r = requests.post(url, proxies=proxyDict, headers=headers,data={'condition':'on','nextButton':'Effectuer+une+demande+de+rendez-vous'})
        data={"response":r.text}
        return data
    except:  "Error during request"
        




@app.route("/")
def hello_world():
    return main()


if __name__ == '__main__':
    app.run(debug=True)