"""
Weather API configure
常规预报输出示例： 输出示例：
"c":{
"c1":"101010100",
"c2":"beijing",
"c3":" 北京 ",
"c4":"beijing",
"c5":" 北 京",
"c6":"beijing",
"c7":" 北京 ",
"c8":"china",
"c9":" 中 国",
"c10":"1",
"c11":"010",
"c12":"100000",
"c13":"116.391",
"c14":"39.904",
"c15":"33",
"c16":"AZ9010"
}
"f":{
"f0":"201203061100",
"f1":[
{# 第一天预报数据
"fa":"01",
"fb":"01",
"fc":"11",
"fd":"0",
"fe":"4",
"ff":"4",
"fg":"1",
"fh":"0",
"fi":"06:44|18:21"
},
{# 第二天预报数据
...
}
{# 第三天预报数据
...
}
]
"""

APPID = "3388beda72527eef"
PRIVATE_KEY = b"69e840_SmartWeatherAPI_cfb6f90"
WEATHER = {
    '00': '晴',
    '01': '多云',
    '02': '阴',
    '03': '阵雨',
    '04': '雷阵雨',
    '05': '雷阵雨伴有冰雹',
    '06': '雨夹雪',
    '07': '小雨',
    '08': '中雨',
    '09': '大雨',
    '10': '暴雨',
    '11': '大暴雨',
    '12': '特大暴雨',
    '13': '阵雪',
    '14': '小雪',
    '15': '中雪',
    '16': '大雪',
    '17': '暴雪',
    '18': '雾',
    '19': '冻雨',
    '20': '沙尘暴',
    '21': '小到中雨',
    '22': '中到大雨',
    '23': '大到暴雨',
    '24': '暴雨到大暴雨',
    '25': '大暴雨到特大暴雨',
    '26': '小到中雪',
    '27': '中到大雪',
    '28': '大到暴雪',
    '29': '浮尘',
    '30': '扬沙',
    '31': '强沙尘暴',
    '53': '霾',
    '99': '无'
}

WINDS_DIRECT = {
    '0': '无持续风向',
    '1': '东北风',
    '2': '东风',
    '3': '东南风',
    '4': '南风',
    '5': '西南风',
    '6': '西风',
    '7': '西北风',
    '8': '北风',
    '9': '旋转风'
}
WINDS_LEVEL = {
    '0': '微风',
    '1': '3-4级',
    '2': '4-5级',
    '3': '5-6级',
    '4': '6-7级',
    '5': '7-8级',
    '6': '8-9级',
    '7': '9-10级',
    '8': '10-11级',
    '9': '11-12级'
}


def query_by_areaid(areaid, forecast_type='forecast_v'):
    import hmac
    from hashlib import sha1
    from base64 import b64encode
    from datetime import datetime
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from http.client import IncompleteRead
    public_key_template = 'http://open.weather.com.cn/data/?areaid={areaid}&type={t}&date={date}&appid={appid}'
    public_key = public_key_template.format(appid=APPID, areaid=areaid,
                                            t=forecast_type,
                                            date=datetime.now().strftime(
                                                "%Y%m%d%H%M"))

    key_str = urlencode({'key': b64encode(hmac.new(PRIVATE_KEY, public_key.encode(), sha1).digest()).decode()})
    url = public_key_template.format(
        appid=APPID[0:6], areaid=areaid,
        t=forecast_type,
        date=datetime.now().strftime(
            "%Y%m%d%H%M")) + '&' + key_str
    for i in range(5):
        try:
            f = urlopen(url, timeout=200)
            content = f.read().decode()
        except (IncompleteRead, ConnectionResetError):
            print('urlopen temp times '+str(i))
            continue
        except:
            raise ValueError('cannot connect the openweather server')
        break
    f.close()
    if content == "data error":
        raise ValueError('query date error')
    return content
