#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import json

API_URL = 'http://apistore.baidu.com/microservice/weather'

def get_weather(citypinyin):
    params = {'citypinyin': citypinyin}
    r = requests.get(API_URL, params=params)
    if r.status_code ==  200:
        return r.text
    return None

def parse_json(json_string):
    if json_string is None:
        return
    js = json.loads(json_string)
    if js['errNum'] == -1: # 成功为0， 失败为-1
        return
    result = js["retData"] # 天气信息结果
    return result

def main():
    if len(sys.argv) == 2:
        city = sys.argv[1]
        js_string = get_weather(city)
        msg_dict = parse_json(js_string)
        for k, v in msg_dict.items():
            print("%s => %s" % (k, v))
    else:
        print("USAGE: \n\tpython weather.py CITYPINYIN_NAME")

if __name__ == '__main__':
    main()

