#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
from dadata import Dadata


def get_address(token, latitude, longitude):
    dadata = Dadata(token)
    result = dadata.geolocate(name="address", lat=latitude, lon=longitude)
    address_components = []
    if len(result) != 0:
        full_address = result[0]['unrestricted_value']
        address_components = full_address.split(', ')
    print(address_components)
    return address_components
