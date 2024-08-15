#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
from dadata import Dadata
import httpx


def get_address(token, latitude, longitude):
    address_components = []
    try:
        dadata = Dadata(token)
        result = dadata.geolocate(name="address", lat=latitude, lon=longitude)

        if len(result) != 0:  # проверка, что найден хотя бы один адрес
            full_address = result[0]['unrestricted_value']
            address_components = full_address.split(', ')

    except httpx.ConnectError as e:  # обработка проблемы с соединением с API DaData
        print(e)
        address_components = None

    return address_components
