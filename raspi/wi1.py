from wifi import Cell, Scheme
import sys
import requests
import os

passkey = '12345678'
cell = Cell()

cells = list(Cell.all('wlan0'))
for i in cells:
    if i.ssid == 'HealthCareSystem':
        cell = i
        print(cell)
        break
scheme = Scheme.for_cell('wlan0','health',cell,passkey)
scheme.save()

