from flask import Flask
import requests

app = Flask(__name__)

def main():
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"'}
        r = requests.post('https://www.guadeloupe.gouv.fr/booking/create/12828/0', headers=headers,data={'condition':'on','nextButton':'Effectuer+une+demande+de+rendez-vous'})
        return r.text

@app.route("/")
def hello_world():
    return main()


if __name__ == '__main__':
    app.run(debug=True,port=4000)