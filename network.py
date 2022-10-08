#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
__file__ = network.py
__author__ = rotoapanta "Roberto Toapanta"
__copyright__ = "Copyright 2022, BitTech"
__credits__ = ["Roberto Toapanta, Giovanny Toapanta"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Roberto Toapanta"
__email__ = "robertocarlos.toapanta@gmail.com"
__status__ = "Production"
__date__ = 16/9/22 10:58
__description__ = "This project is based on an ESP32-S2 general-purpose development board 
                    with micropython to connect to the local network. "
__information__ : 
"""

import network
import wifi_credentials
import ubinascii

def do_connect():
    wlan = network.WLAN(network.STA_IF)     # create station interface
    wlan.active(True)                       # activate the interface
    if not wlan.isconnected():              # check if the station is connected to an AP
        print('connecting to network...')
        wlan.connect(wifi_credentials.ssid, wifi_credentials.password)      # connect to an AP
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())       # get the interface's IP/netmask/gw/DNS addresses    
    wlan_mac = wlan.config('mac')
    print('MAC address', ubinascii.hexlify(wlan_mac, ':').decode().upper())

do_connect()