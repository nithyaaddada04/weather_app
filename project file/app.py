from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "3b0c425803a81fe9379e700e0a515964"# Replace this

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city'].strip().title()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    print(f" API URL:{url}")
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['cod'] == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed']
        }
        return render_template('result.html', weather=weather_data)
    else:
        error = "City not found or API error"
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)