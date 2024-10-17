# IOT management system

Controling sensors and actuators connected to ESP32 over the internet!

## Tools
- Django
- Vue.js
- Mosquito
- ESP32
- ApexChart


## Implementation Details
This project has 4 parts:
- ESP32 codes
- Django backend
- Vue.js frontend
- Musquito broker

ESP32s connect to a mqtt broker, so they can send their collected data and recive commands in json. Django server connects to the broker, and then sends and receives data. each device has a corresponding object in Django with a token. this token is sent with each message to authenticate the device. You can add as many devices as you want by using the Front-end panel. The collected data will be saved in the database.


## How to Run

First, run a Mosquitto broker on a server. 
After running that, you should update the code for ESP32 to connect to wifi and also connect to the mqtt broker.
Moreover, change the credentials of the mqtt broker in the mqtt_client file in the backend. now you can run Django Back-end with this command in the dashboard folder:
```bash
python manage.py runserver
```

after that, run this command in the Front-end folder to start the Front-end:
```bash
npm run serve
```

For each ESP32 device, you need a token. You can get that token by adding a new device in the frontend. All devices are shown in the Front-end section. Upload the code to the ESP32 and customize the ports if you want. When the account is logged in, the data and its control system are shown. Bore can be used to test the project over the internet. 


## Results
login page:


![login](https://github.com/Sharif-University-ESRLab/summer2024-iot-management-system/blob/main/Miscellaneous/photo_2024-09-02_21-03-14.jpg)


user panel:


![user panel](https://github.com/Sharif-University-ESRLab/summer2024-iot-management-system/blob/main/Miscellaneous/photo_2024-09-02_21-03-20.jpg)


test:


![project test](https://github.com/Sharif-University-ESRLab/summer2024-iot-management-system/blob/main/Miscellaneous/photo_2024-09-02_21-02-33.jpg)



## Related Links
 - [ESP32 Pinout](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)
 - [Django Doc](https://docs.djangoproject.com/en/5.0/)
 - [bore](https://github.com/ekzhang/bore)
 - [Apexcharts](http://apexcharts.com/)


## Authors
Authors and their github link come here.
- [@moeen89](https://github.com/moeen89/)
- [@amirhosse-in](https://github.com/amirhosse-in/)
- [@shayanshabani](https://github.com/shayanshabani/)
