# coding=UTF-8
from bs4 import BeautifulSoup
import requests
import os

# 使用说明 将py文件放在要保存图包的目录下运行
# number别太贪心 目前主页24个 我也就设置最大24

# 源url number确认要整几个图包
url0 = 'https://www.mzitu.com'
headers = {
    'referer': 'https://www.mzitu.com/188045',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
}
number = int(input('how many:(max=24)'))
while number > 24:
    number = int(input('how many:(max=24)'))

# 打开主页
res0 = requests.get(url0, headers=headers)
soup0 = BeautifulSoup(res0.text, 'html.parser')

# 正式开整
for h in range(number):
    url = soup0.find('div', class_='main').find('div', class_='postlist') \
        .find_all('li')[h].a['href']
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    target_url = soup.find('div', class_='main-image').img['src']
    # filename = target_url.split(r'.net/')[-1]
    # 懒得处理filename里的/了 直接1 2 3 4命名图片完事
    pages = soup.find('div', class_='pagenavi').find_all('a')[-2].span.text
    title = soup.find('div', class_='content').find('h2', class_='main-title').text

    print('正在搞第{}个...'.format(h + 1))
    if title not in os.listdir():
        os.mkdir(title)
    os.chdir(title)

    for i in range(int(pages)):
        url1 = url + r'/' + str(i + 1)
        res1 = requests.get(url1, headers=headers)
        soup = BeautifulSoup(res1.text, 'html.parser')
        main_img = soup.find('div', class_='main-image')
        if main_img:
            target_url = soup.find('div', class_='main-image').img['src']
            res1 = requests.get(target_url, headers=headers)
            with open(str(i + 1) + r'.jpg', 'wb') as f:
                f.write(res1.content)
        res1.close()
    os.chdir('..')
print("------------------工作完成，敬请享用-------------------")
# 我完事了 你们呢
