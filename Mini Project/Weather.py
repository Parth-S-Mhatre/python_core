import sys
import  requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter city name:",self)
        self.city_input=QLineEdit(self)
        self.get_weather=QPushButton("Get Weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.desc_label=QLabel(self)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\weather.png"))
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)
        self.setLayout(vbox)
        # alignment
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)
        # object name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temp_label")
        self.get_weather.setObjectName("get_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")
        self.setStyleSheet("""
                QLabel,QPushButton{
                           font-family:calibri;
                           }
                QLabel#city_label{
                           font-size:40px;
                           font-style:italic;
                           }
                QLineEdit#city_input{
                           font-size:40px;
                           }
                QPushButton#get_label{
                           font-size:30px;
                           font-weight:bold;
                           }
                QLabel#temp_label{
                           font-size:70px;
                           }
                QLabel#emoji_label{
                           font-size:100px;
                           }
                QLabel#desc_label{
                           font-size:50px;}
                QPushButton#get_label{
                           background-color:hsl(118, 6%, 60%);
                           }
                QPushButton#get_label:hover{
                           background-color:hsl(118, 100%, 80%);
                           }
                           """)
        self.get_weather.clicked.connect(self.get_Weather)
    def get_Weather(self):
        api_key="bb8f1a118734c0ff5db619fd6bfd7e40"
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
           response=requests.get(url)
           response.raise_for_status()
           data=response.json()

           if data["cod"]==200:
              self.show_weather(data)

        except requests.exceptions.HTTPError as errh:
            match response.status_code:
                case 400:
                     self.display_error("Bad request\nPlease check your input!!")
                case 401:
                     self.display_error("Unauthorized\nInvalid API key!!")
                case 403:
                     self.display_error("Forbidden\nAccess is denied!!")
                case 404:
                     self.display_error("Not Found\nCity not found!!")
                case 500:
                     self.display_error("Internal Sever Error\nPlease try again later!!")
                case 502:
                     self.display_error("Bad gateway\nInvalid response from server!!")
                case 503:
                     self.display_error("Service Unavaliable\nServer is down!!")
                case 504:
                     self.display_error("Gateway Timeout\nNo response from server!!")
                case _:
                     self.display_error(f"HTTP error occurred!!{errh}")
        except requests.exceptions.ConnectionError as errc:
             self.display_error(f"Connection Error:\nCheck your Internet Connection")
        except requests.exceptions.Timeout as errt:
             self.display_error(f"Timeout Error:\n{errt} The request time out!!")
        except requests.exceptions.TooManyRedirects as err:
             self.display_error(f"Too Many Redirects:\n{err} The request too many redirects!!")


        except requests.exceptions.RequestException as err1:
            print(f"Request Error:\n {err1} as the request failed ")
        
    def show_weather(self,data):
        self.temperature_label.setStyleSheet("font-size:75px;")
        temperature_k=data["main"]["temp"]
        temperature_c=temperature_k-273.15
        temperature_f=(temperature_k*9/5)-459.67
        weather_id=data["weather"][0]["id"]
        weather_desc=data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_emoji(weather_id))
        self.desc_label.setText(weather_desc)

    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:30px;")
        self.temperature_label.setText(message)
        self.emoji_label.setText("")
        self.desc_label.setText("")
    @staticmethod
    def get_emoji(weather_id):
         if 200 <= weather_id <= 232:
            return "⛈️"  # Thunderstorm
         elif 300 <= weather_id <= 321:
           return "🌦️"  # Drizzle
         elif 500 <= weather_id <= 531:
           return "🌧️"  # Rain
         elif 600 <= weather_id <= 622:
           return "🌨️"  # Snow
         elif 700 <= weather_id <= 741:
           return "🍃"  # Mist/Fog
         elif weather_id == 781:
           return "🌪️"  # Tornado
         elif weather_id == 800:
           return "🌞"  # Clear sky
         elif 801 <= weather_id <= 804:
           return "☁️"  # Clouds
         elif 900 <= weather_id <= 902:
           return "🌩️"  # Severe Thunderstorm
         elif weather_id == 903:
           return "❄️"  # Cold
         elif weather_id == 904:
           return "🌡️"  # Hot
         elif 905 <= weather_id <= 1000:
           return "💨"  # Windy
         else:
           return "🌈"  # Unknown weather

app=QApplication(sys.argv)
weather_app=Weather()
weather_app.show()
sys.exit(app.exec_())