#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : __init__.py.py
# @Time      : 2019/1/09 17:06
# @software  : PyCharm
from flask import render_template, flash, redirect, url_for
from weather import app, models,db
import requests, urllib, json
from flask import Flask, render_template, request

from weather.models import City


# @app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    weather_data = []
    # AppId = 'b0dc56086602d63179f7328505807eeb'
    # AppId = '70a2a88cd66dbe11b1f1a6b20ca3889c'
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # base_url = "https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589"

    # key = '8a439a7e0e034cdcb4122c918f55e5f3'
    key = 'cd06b6f74ce346b095bada680fe54375'

    hefeng_air = 'https://free-api.heweather.net/s6/air/now?'
    hefeng_lifestyle = 'https://free-api.heweather.net/s6/weather/lifestyle?'
    hefeng_solarsunrise_sunset = 'https://free-api.heweather.net/s6/solar/sunrise-sunset?'
    hefeng_weather = 'https://free-api.heweather.net/s6/weather?'
    hefeng_forecast = 'https://free-api.heweather.net/s6/weather/forecast?'
    hefeng_hourly = 'https://free-api.heweather.net/s6/weather/hourly?'
    hefeng_now = 'https://free-api.heweather.net/s6/weather/now?'

    # city = 'LasVegas'
    # city = 'beijing'
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={city name}，{country code}'
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&' + AppId
    # url = base_url + '&q=' +city + '&appid=' + AppId
    # city = 'Las Vegas'

    # parametres = {
    #     'location': 'beijing',
    #     'key': 'cd06b6f74ce346b095bada680fe54375',
    #     'lang': 'zh',
    #     'unit': 'm'
    # }

    cities = City.query.all()

    for city in cities:
        # url = hefeng_air + 'city=' + city + '&key=' + key
        url0 = hefeng_air + 'key=' + key + '&location=' + city.name
        url1 = hefeng_lifestyle + 'key=' + key + '&location=' + city.name
        url2 = hefeng_solarsunrise_sunset + 'key=' + key + '&location=' + city.name
        url3 = hefeng_weather + 'key=' + key + '&location=' + city.name
        url4 = hefeng_forecast + 'key=' + key + '&location=' + city.name
        url5 = hefeng_hourly + 'key=' + key + '&location=' + city.name
        url6 = hefeng_now + 'key=' + key + '&location=' + city.name
        #
        print(url0)
        print(url1)
        print(url2)
        print(url3)
        print(url4)
        print(url5)
        print(url6)
        print('..................')
        # r = requests.get(base_url)
        # r = requests.get(base_url).json()
        r0 = requests.get(url0).json()
        r1 = requests.get(url1).json()
        r2 = requests.get(url2).json()
        r3 = requests.get(url3).json()
        r4 = requests.get(url4).json()
        r5 = requests.get(url5).json()
        r6 = requests.get(url6).json()

        # try:
        #
        #     response = requests.get(hefeng_forecast, params=parametres)
        #
        #     r = json.loads(json.dumps(response.text, ensure_ascii=False, indent=1))
        #
        #     r = json.loads(response.text)
        # except Exception as err:
        #
        #     print(err)
        print(r0)
        print(r1)
        print(r2)
        print(r3)
        print(r4)
        print(r5)
        print(r6)

        weather = {
            'id': r0['HeWeather6'][0]['basic']['cid'],
            'city': r0['HeWeather6'][0]['basic']['location'] + '-' + r0['HeWeather6'][0]['basic']['cnty'],
            'country': r0['HeWeather6'][0]['basic']['cnty'],
            'coordinate': r0['HeWeather6'][0]['basic']['lat'] + ',' + r0['HeWeather6'][0]['basic']['lon'],
            'time_zone': r0['HeWeather6'][0]['basic']['tz'],
            'local_time': r0['HeWeather6'][0]['update']['loc'],
            'aqi': r0['HeWeather6'][0]['air_now_city']['aqi'],
            'main': r0['HeWeather6'][0]['air_now_city']['main'],
            'qlty': r0['HeWeather6'][0]['air_now_city']['qlty'],
            'pm10': r0['HeWeather6'][0]['air_now_city']['pm10'],
            'pm25': r0['HeWeather6'][0]['air_now_city']['pm25'],
            'no2': r0['HeWeather6'][0]['air_now_city']['no2'],
            'so2': r0['HeWeather6'][0]['air_now_city']['so2'],
            'co': r0['HeWeather6'][0]['air_now_city']['co'],
            'o3': r0['HeWeather6'][0]['air_now_city']['o3'],
            'pub_time': r0['HeWeather6'][0]['air_now_city']['pub_time'],
            'lifestyle': {
                'comf': r1['HeWeather6'][0]['lifestyle'][0]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][0][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][0]['txt'],
                'drsg': r1['HeWeather6'][0]['lifestyle'][1]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][1][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][1]['txt'],
                'flu': r1['HeWeather6'][0]['lifestyle'][2]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][2][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][2]['txt'],
                'sport': r1['HeWeather6'][0]['lifestyle'][3]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][3][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][3]['txt'],
                'trav': r1['HeWeather6'][0]['lifestyle'][4]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][4][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][4]['txt'],
                'uv': r1['HeWeather6'][0]['lifestyle'][5]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][5][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][5]['txt'],
                'cw': r1['HeWeather6'][0]['lifestyle'][6]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][6][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][6]['txt'],
                'air': r1['HeWeather6'][0]['lifestyle'][7]['type'] + '...' + r1['HeWeather6'][0]['lifestyle'][7][
                    'brf'] + '...' + r1['HeWeather6'][0]['lifestyle'][7]['txt'],
            },
            'sunrise_sunset': {
                'mr0': r2['HeWeather6'][0]['sunrise_sunset'][0]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][0]['mr'],
                'mr1': r2['HeWeather6'][0]['sunrise_sunset'][1]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][1]['mr'],
                'mr2': r2['HeWeather6'][0]['sunrise_sunset'][2]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][2]['mr'],
                'ms0': r2['HeWeather6'][0]['sunrise_sunset'][0]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][0]['ms'],
                'ms1': r2['HeWeather6'][0]['sunrise_sunset'][1]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][1]['ms'],
                'ms2': r2['HeWeather6'][0]['sunrise_sunset'][2]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][2]['ms'],
                'sr0': r2['HeWeather6'][0]['sunrise_sunset'][0]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][0]['sr'],
                'sr1': r2['HeWeather6'][0]['sunrise_sunset'][1]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][1]['sr'],
                'sr2': r2['HeWeather6'][0]['sunrise_sunset'][2]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][2]['sr'],
                'ss0': r2['HeWeather6'][0]['sunrise_sunset'][0]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][0]['ss'],
                'ss1': r2['HeWeather6'][0]['sunrise_sunset'][1]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][1]['ss'],
                'ss2': r2['HeWeather6'][0]['sunrise_sunset'][2]['date'] + ':' +
                       r2['HeWeather6'][0]['sunrise_sunset'][2]['ss'],

            },

            'cloud': r3['HeWeather6'][0]['now']['cloud'],
            'fl': r3['HeWeather6'][0]['now']['fl'],
            'tmp': r3['HeWeather6'][0]['now']['tmp'],
            'cond_txt': r3['HeWeather6'][0]['now']['cond_txt'],
            'wind_dir': r3['HeWeather6'][0]['now']['wind_dir'],
            'wind_sc': r3['HeWeather6'][0]['now']['wind_sc'],
            'wind_spd': r3['HeWeather6'][0]['now']['wind_spd'],
            'hum': r3['HeWeather6'][0]['now']['hum'],
            'pcpn': r3['HeWeather6'][0]['now']['pcpn'],
            'pres': r3['HeWeather6'][0]['now']['pres'],
            'vis': r3['HeWeather6'][0]['now']['vis'],
            'daily_forecast': {
                'date': r4['HeWeather6'][0]['daily_forecast'][0]['date'],
                'sr': r4['HeWeather6'][0]['daily_forecast'][0]['sr'],
                'ss': r4['HeWeather6'][0]['daily_forecast'][0]['ss'],
                'mr': r4['HeWeather6'][0]['daily_forecast'][0]['mr'],
                'ms': r4['HeWeather6'][0]['daily_forecast'][0]['ms'],
                'tmp_max': r4['HeWeather6'][0]['daily_forecast'][0]['tmp_max'],
                'tmp_min': r4['HeWeather6'][0]['daily_forecast'][0]['tmp_min'],
                'cond_txt_d': r4['HeWeather6'][0]['daily_forecast'][0]['cond_txt_d'],
                'cond_txt_n': r4['HeWeather6'][0]['daily_forecast'][0]['cond_txt_n'],
                'pop': r4['HeWeather6'][0]['daily_forecast'][0]['pop'],
                'uv_index': r4['HeWeather6'][0]['daily_forecast'][0]['uv_index'],
                'hum': r4['HeWeather6'][0]['daily_forecast'][0]['hum'],
                # 'tmp_min': r4['HeWeather6'][0]['daily_forecast'][0]['tmp_min'],
                # 'pub_time': r0['HeWeather6'][0]['air_now_city']['pub_time'],

            }
        }
        print(weather)
        # print(r.json())
        # print(r.json())

        weather_data.append(weather)
        print(weather_data)

    return render_template('weather.html', weather_data=weather_data)