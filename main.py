import requests
import json
from api_keys import openweathermap_key, ipbase_key
import csv
ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']
with open('ip_orai.csv', 'w', newline="", encoding='UTF-8') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(['IP', 'Country', 'City', 'Temp', 'Weather'])
    for ip in ip_list:
        geo_payload = {'apikey': ipbase_key, 'ip': ip}
        ip_response = requests.get(f"https://api.ipbase.com/v2/info", params=geo_payload)
        ip_location = json.loads(ip_response.text)
        country = ip_location['data']['location']['country']['name']
        city = ip_location['data']['location']['city']['name']
        try:
        # if city != '':
            payload = {'appid': openweathermap_key, 'q': city, 'units': "metric"}
            weather_response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
            weather_by_ip = json.loads(weather_response.text)
            ip_temp = weather_by_ip['main']['temp']
            ip_weather = weather_by_ip['weather'][0]['main']
            print("Temp:", ip_temp, "Weather:", ip_weather, "City:", city, "Country:", country)
            csvwriter.writerow([ip, country, city, ip_temp, ip_weather])
        except KeyError:
            print(f"City of {country} was not found.")



