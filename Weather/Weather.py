import sys
import requests
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


def get_weather(location):
    api_key = '1b86abaedd0604dce27bfbc2b40ae211'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': location, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = str(data['main']['temp'])
            humidity = str(data['main']['humidity'])
            weather_conditions = str(data['weather'][0]['description'])
            result = f"Weather in '{location}':\nCondition: {weather_conditions.capitalize()}\n"
            result += f"Temperature: {temperature}°C\nHumidity: {humidity}%"
        else:
            result = f"Error: {data['message']}"

        return result
    except Exception as e:
        return "Error fetching data. Please check your internet connection or try again later."


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        # City Input
        self.city_label = QLabel("Enter City:")
        self.layout.addWidget(self.city_label)

        self.city_input = QLineEdit()
        self.city_input.returnPressed.connect(self.show_weather)  # Enter key trigger
        self.layout.addWidget(self.city_input)

        # Show Weather Button
        self.show_button = QPushButton("Show Weather")
        self.show_button.clicked.connect(self.show_weather)
        self.layout.addWidget(self.show_button)

        # Result Label
        self.result_label = QLabel("")
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def show_weather(self):
        location = self.city_input.text()
        if location:
            weather_info = get_weather(location)
            self.result_label.setText(weather_info)
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a location.")


# Main loop
app = QApplication(sys.argv)
window = WeatherApp()
window.show()
sys.exit(app.exec_())
