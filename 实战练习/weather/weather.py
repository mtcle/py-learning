# 天气预报
import urllib.request
import gzip
import json
import re

print("------天气预报查询------")


def get_weather_data(city_name):
    url1 = "http://wthrcdn.etouch.cn/weather_mini?city=" + urllib.parse.quote(city_name)
    # print("请求url： %s" % url1)

    # 获取到网页数据
    weather_data = urllib.request.urlopen(url1).read()

    # 解压缩网页数据
    weather_data = gzip.decompress(weather_data).decode("utf-8")

    # 正则匹配，移除掉特殊字符，替换
    re_cdata = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")  # 匹配CDATA
    m = re_cdata.search(weather_data)
    if m and m.lastindex > 0:
        weather_data = re_cdata.sub(m.group(1), weather_data)

    # 将返回数据转换为json
    weather_dic = json.loads(weather_data)
    # print(weather_dic)
    return weather_dic


def show_weather_data(city, dic):
    if dic.get("desc") == "OK":
        data_dic = dic.get("data")
        cast_dic = data_dic.get("forecast")
        print('城市：', data_dic.get('city'))
        print('日期：', cast_dic[0].get('date'))
        print('温度：', data_dic.get('wendu') + '℃ ')
        print('风向：', cast_dic[0].get('fengxiang'))
        print('风级：', cast_dic[0].get('fengli'))
        print('高温：', cast_dic[0].get('high'))
        print('低温：', cast_dic[0].get('low'))
        print('天气：', cast_dic[0].get('type'))
        print('感冒：', data_dic.get('ganmao'))
        print('*******************************')
        is_need_four_day = input("是否需要显示未来4天数据，是/否:")
        if is_need_four_day == "是" or is_need_four_day == "Y" or is_need_four_day == "y":
            for index in range(1, 5):
                print('日期：', cast_dic[index].get('date'))
                print('风向：', cast_dic[index].get('fengxiang'))
                print('风级：', cast_dic[index].get('fengli'))
                print('高温：', cast_dic[index].get('high'))
                print('低温：', cast_dic[index].get('low'))
                print('天气：', cast_dic[index].get('type'))
                print('--------------------------')
        else:
            print("取消继续查询")
    elif dic.get("desc") == "invilad-citykey":
        print("该输入 % s 未录入，请检查输入" % city)
    else:
        print("其他未知错误")
    print("--------------------查询结束---------------------")
    # 继续下次查询
    main_method()


def main_method():
    city_name = input("请输入要查询的城市名称：")
    if city_name.strip() != "":
        resp = get_weather_data(city_name)
        if len(resp) > 0:
            show_weather_data(city_name, resp)
        else:
            print("请求应答数据为空，请检测网络！")
    else:
        print("请输入要查询的城市名称！")


main_method()
