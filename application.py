#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import bottle
from bottle import template, request, redirect, response
import argparse
import getter

app = bottle.Bottle()
token = ''
urlPrefix = '/test_task'


@app.route(urlPrefix + '/main', method=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        # получаем значения широты и долготы
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        # записываем координаты в куки
        response.set_cookie('latitude', latitude, secret='something_special')
        response.set_cookie('longitude', longitude, secret='something_special')

        redirect(urlPrefix + '/address')
    return template('templates/main.html')


@app.route(urlPrefix + '/address', method=['GET', 'POST'])
def get_address():
    if request.method == 'POST':
        redirect(urlPrefix + '/main')
    else:
        # берем значения координат из куки
        latitude = request.get_cookie('latitude', secret='something_special')
        longitude = request.get_cookie('longitude', secret='something_special')
        coordinates = f'({latitude}, {longitude})'

        # запрашиваем адрес по координатам
        address_components = getter.get_address(token, latitude, longitude)

    return template('templates/address.html', address_components=address_components, coordinates=coordinates)


if __name__ == '__main__':
    # получаем токен для DaData из аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', action='store', dest='token', type=str)
    args = parser.parse_args()
    token = args.token

    app.run(host='localhost', port=8080, debug=True)
