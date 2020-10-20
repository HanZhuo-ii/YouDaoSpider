# -*- coding: utf-8 -*-
import requests
import time
import random
import hashlib


class HTMLParser(object):
    @staticmethod
    def parser(data_result):
        if data_result['errorCode'] is not 0:
            raise Exception('翻译异常，检查输入')
        for data in data_result['translateResult']:
            yield {
                "src": data[0]['src'],
                "tgt": data[0]['tgt']
            }


def get_param(kwd):
    r = int(time.time() * 1000)  # Python中的时间戳是精确到秒的浮点型，JS中是毫秒整型
    salt = str(random.randint(0, 9) + r)
    str1 = "fanyideskweb" + kwd + salt + "]BjuETDhU)zqSxf-=B#7m"
    sign = hashlib.md5(str1.encode()).hexdigest()
    return {
        'i': kwd,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': salt[:-1],
        'bv': '50bb7d203385bb098ccf4c3e9502c021',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }


def master(kwd):
    html_parser = HTMLParser()
    api = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1608111447@121.28.142.130; OUTFOX_SEARCH_USER_ID_NCOO=1006821066.3087116; "
                  "JSESSIONID=aaay_RaFnLz2s8dEEPWux; ___rl__test__cookies=1602843516016",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Pragma": "no-cache",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38",
    }

    res = requests.post(api, headers=headers, params=get_param(kwd), timeout=5)
    if res:
        data_set = res.json()
    data = html_parser.parser(data_set)
    for i in data:
        print(i['src'] + ": " + i['tgt'])


if __name__ == '__main__':
    kwd = input("请输入要翻译的词语：")
    master(kwd)
