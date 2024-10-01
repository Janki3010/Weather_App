from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'dfd4206b61f50a4bc53cf187d94965ea'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather', methods=['POST', 'GET'])
def weather():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06a5b8b8613f672b617bf50613ff9efe'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return render_template('weather.html', weather=weather_info)
    else:
        error_message = data.get('message', 'City not found!')
        return render_template('index.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=False, port=3007)
