#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : __init__.py.py
# @Time      : 2019/1/09 17:06
# @software  : PyCharm
from flask import render_template, flash, redirect, url_for
from wtforms import ValidationError

from weather import app, models,db
import requests, urllib, json
from flask import Flask, render_template, request
from weather.forms import AddCityForm

from weather.models import City


# @app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_city = request.form.get('city')
        print(new_city)

        if new_city:
            city_name = City.query.filter_by(name=new_city).first()
            if city_name is not None:
                # raise ValidationError('Please use a different city name.')
                flash('Please use a different city name.')
                return redirect(url_for('weather1.html'))

            new_city_obj = City(name=new_city)
            # all_city = City.query.all()
            if new_city_obj == city_name:
                flash('You have already added the city')
                return redirect(url_for('add_city'))
            else:
                db.session.add(new_city_obj)
                db.session.commit()

    weather_data = []
    # AppId = 'b0dc56086602d63179f7328505807eeb'
    # AppId = '70a2a88cd66dbe11b1f1a6b20ca3889c'
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # base_url = "https://api.darksky.net/forecast/0123456789abcdef9876543210fedcba/42.3601,-71.0589"

    # key = '8a439a7e0e034cdcb4122c918f55e5f3'
    # key = '8a439a7e0e034cdcb4122c918f55e5f3' # v5

    key = 'eda832ba81c4433982bc2fe24a90e7c8'

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
        r6 = requests.get(url3).json()
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
        print(r6)
        print(r4)
        print(r5)
        print(r6)

        weather = {
            'cid': r0['HeWeather6'][0]['basic']['cid'],
            'city': r0['HeWeather6'][0]['basic']['location'],
            'parent_city': r0['HeWeather6'][0]['basic']['parent_city'],

            'admin_area': r0['HeWeather6'][0]['basic']['admin_area'],
            'area': r0['HeWeather6'][0]['basic']['location'] + '-' + r0['HeWeather6'][0]['basic']['admin_area'] + '-' + r0['HeWeather6'][0]['basic']['cnty'],
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
            # 'sr': r2['HeWeather6'][0]['sunrise_sunset'][2]['date'] + ':' + r2['HeWeather6'][0]['sunrise_sunset'][2]['sr'],
            # 'ss': r2['HeWeather6'][0]['sunrise_sunset'][0]['date'] + ':' + r2['HeWeather6'][0]['sunrise_sunset'][0]['ss'],
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

            'date': r4['HeWeather6'][0]['daily_forecast'][0]['date'],
            'sr': r4['HeWeather6'][0]['daily_forecast'][0]['sr'],
            'ss': r4['HeWeather6'][0]['daily_forecast'][0]['ss'],
            'mr': r4['HeWeather6'][0]['daily_forecast'][0]['mr'],
            'ms': r4['HeWeather6'][0]['daily_forecast'][0]['ms'],
            'tmp_max': r4['HeWeather6'][0]['daily_forecast'][0]['tmp_max'],
            'tmp_min': r4['HeWeather6'][0]['daily_forecast'][0]['tmp_min'],
            'cond_txt_d': r4['HeWeather6'][0]['daily_forecast'][0]['cond_txt_d'],
            'cond_txt_n': r4['HeWeather6'][0]['daily_forecast'][0]['cond_txt_n'],
            'wind_deg': r4['HeWeather6'][0]['daily_forecast'][0]['wind_deg'],
            'wind_dir': r4['HeWeather6'][0]['daily_forecast'][0]['wind_dir'],
            'wind_sc': r4['HeWeather6'][0]['daily_forecast'][0]['wind_sc'],
            'wind_spd': r4['HeWeather6'][0]['daily_forecast'][0]['wind_spd'],
            'pcpn': r4['HeWeather6'][0]['daily_forecast'][0]['pcpn'],
            'pres': r4['HeWeather6'][0]['daily_forecast'][0]['pres'],
            'vis': r4['HeWeather6'][0]['daily_forecast'][0]['vis'],
            'pops': r4['HeWeather6'][0]['daily_forecast'][0]['pop'],
            'uv_index': r4['HeWeather6'][0]['daily_forecast'][0]['uv_index'],
            'hum': r4['HeWeather6'][0]['daily_forecast'][0]['hum'],


            'now_cloud': r6['HeWeather6'][0]['now']['cloud'],
            'now_fl': r6['HeWeather6'][0]['now']['fl'],
            'now_tmp': r6['HeWeather6'][0]['now']['tmp'],
            'now_cond_txt': r6['HeWeather6'][0]['now']['cond_txt'],
            'now_wind_deg': r6['HeWeather6'][0]['now']['wind_deg'],
            'now_wind_dir': r6['HeWeather6'][0]['now']['wind_dir'],
            'now_wind_sc': r6['HeWeather6'][0]['now']['wind_sc'],
            'now_wind_spd': r6['HeWeather6'][0]['now']['wind_spd'],
            'now_hum': r6['HeWeather6'][0]['now']['hum'],
            'now_pcpn': r6['HeWeather6'][0]['now']['pcpn'],
            'now_pres': r6['HeWeather6'][0]['now']['pres'],
            'now_vis': r6['HeWeather6'][0]['now']['vis'],
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

    return render_template('weather1.html', weather_data=weather_data)


# @app.route('/', methods=['GET', 'POST'])
# def add_city():
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('index'))
#     weather_data=[]
#     weather = {
#                 'id': 111111,
#                 'city': '北京',
#                 'area': '北京-北京-中国',
#                 'country': '中国',
#                 'coordinate': 34.45,
#                 'time_zone': +8,
#                 'local_time': '2019.01.19 18:36:36',
#                 'aqi': '54',
#                 'qlty': '良',
#                 'main': 'PM10',
#                 'pm25': '33',
#                 'pm10': '58',
#                 'no2': '61',
#                 'so2': '7',
#                 'co': '0.8',
#                 'o3': '19',
#                 'pub_time': '2019-01-16 18:00',
#         'cloud': '0',
#         'cond_code': '100',
#         'cond_txt': '晴',
#         'fl': '-5',
#         'hum': '14',
#         'pcpn': '0.0',
#         'pres': '1025',
#         'tmp': '-1',
#         'vis': '10',
#         'wind_deg': '210',
#         'wind_dir': '西南风',
#         'wind_sc': '2',
#         'wind_spd': '7',
#         'cond_code_d': '100',
#         'cond_code_n': '100',
#         'cond_txt_d': '晴',
#         'cond_txt_n': '晴',
#         'date': '2019-01-16',
#         'mr': '13:00',
#         'ms': '01:57',
#         'pop': '0',
#         'sr': '07:33',
#         'ss': '17:15',
#         'tmp_max': '2',
#         'tmp_min': '-8',
#         'uv_index': '3',
#
#                 'lifestyle': [
#                     {'type': 'comf', 'brf': '较不舒适', 'txt': '白天天气晴好，但仍会使您感觉偏冷，不很舒适，请注意适时添加衣物，以防感冒。'},
#                     {'type': 'drsg', 'brf': '冷', 'txt': '天气冷，建议着棉服、羽绒服、皮夹克加羊毛衫等冬季服装。年老体弱者宜着厚棉衣、冬大衣或厚羽绒服。'},
#                     {'type': 'flu', 'brf': '少发', 'txt': '各项气象条件适宜，无明显降温过程，发生感冒机率较低。'},
#                     {'type': 'sport', 'brf': '较不宜', 'txt': '天气较好，但考虑天气寒冷，推荐您进行室内运动，户外运动时请注意保暖并做好准备活动。'},
#                     {'type': 'trav', 'brf': '较适宜', 'txt': '天气较好，同时又有微风伴您一路同行。稍冷，较适宜旅游，您仍可陶醉于大自然的美丽风光中。'},
#                     {'type': 'uv', 'brf': '弱', 'txt': '紫外线强度较弱，建议出门前涂擦SPF在12-15之间、PA+的防晒护肤品。'},
#                     {'type': 'cw', 'brf': '较适宜', 'txt': '较适宜洗车，未来一天无雨，风力较小，擦洗一新的汽车至少能保持一天。'},
#                     {'type': 'air', 'brf': '中', 'txt': '气象条件对空气污染物稀释、扩散和清除无明显影响，易感人群应适当减少室外活动时间。'}],
#         'now_cloud': '91',
#         'now_cond_code': '101',
#         'now_cond_txt': '多云',
#         'now_fl': '0',
#         'now_hum': '61',
#         'now_pcpn': '0.0',
#         'now_pres': '1030',
#         'now_tmp': '3',
#         'now_vis': '16',
#         'now_wind_deg': '276',
#         'now_wind_dir': '西风',
#         'now_wind_sc': '1',
#         'now_wind_spd': '5',
#
#                 }
#     weather_data.append(weather)
#     print(weather_data)
#
#     return render_template('weather1.html', weather_data=weather_data)
