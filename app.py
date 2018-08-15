from flask import Flask, render_template #, request
import requests, time, datetime


app = Flask(__name__)

@app.route('/')
def index():
	r = requests.get('http://api.openweathermap.org/data/2.5/group?id=5128638,1689973,5368381,3582383,4861716,6167865,1850692,524901,703448,2643743&units=metric&appid=68e0576296ad23454ce2bbfd1c560322')
	jsonObject = r.json()
	info=jsonObject["list"]
	for city in info:
		city['dt']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(city['dt']))
	return render_template('temperature.html',cityInfo=jsonObject["list"],time=datetime.datetime.now(),enumerate=enumerate)


if __name__ == '__main__':
	app.run()

