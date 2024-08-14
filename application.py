#!/usr/bin/python3.7
#-*- coding: UTF-8 -*-
from bottle import route, run, template, request, redirect

@route('/main', method=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        redirect('/address')
    return template('templates/main.html')

@route('/address', method=['GET', 'POST'])
def get_address():
    if request.method == 'POST':
        redirect('/main')
    return template('templates/address.html')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)