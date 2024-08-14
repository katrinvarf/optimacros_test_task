#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
import bottle
from bottle import template, request, redirect
import argparse

app = bottle.Bottle()
token = ''


@app.route('/main', method=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        redirect('/address')
    return template('templates/main.html')


@app.route('/address', method=['GET', 'POST'])
def get_address():
    if request.method == 'POST':
        redirect('/main')
    return template('templates/address.html')


if __name__ == '__main__':
    # получаем токен для DaData из аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--token', action='store', dest='token', type=str)
    args = parser.parse_args()
    token = args.token

    app.run(host='localhost', port=8080, debug=True)
