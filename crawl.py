# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
from time import sleep

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def crawl_lianjia():
    url = 'https://sh.lianjia.com/zufang/pg{page}/'
    csv_file = open('lianjia.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    print('start fetch linjia..')
    for i in tqdm(range(1, 101)):
        sleep(1)
        response = requests.get(url.format(page=i), headers=header, allow_redirects=False)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            for item in html.select('.info-panel'):
                houseUrl = item.find('h2').a['href']
                title = item.find('h2').a['title']
                location = title.split(' ')[0]
                csv_writer.writerow([title, location, houseUrl])
        else:
            break


def crawl_anjuke():
    url = 'https://sh.zu.anjuke.com/fangyuan/p1/'
    csv_file = open('anjuke.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    print('start fetch anjuke..')
    print('fetching anjuke..')
    while True:
        sleep(1)
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            try:
                url = html.select('.aNxt')[0]['href']
            except:
                url = None
            for item in html.select('.zu-itemmod .zu-info'):
                houseUrl = item.find('h3').a['href']
                title = item.find('h3').a['title']
                try:
                    location = item.address.a.string
                except:
                    location = None
                if location:
                    csv_writer.writerow([title, location, houseUrl])
            if not url:
                break
        else:
            break


def crawl_58():
    url = 'http://sh.58.com/chuzu/pn{page}/'
    csv_file = open('58tongcheng.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    print('start fetch 58 tongcheng..')
    for i in tqdm(range(1, 71)):
        sleep(1)
        response = requests.get(url.format(page=i), headers=header, allow_redirects=False)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            for item in html.select('li .des'):
                houseUrl = item.find('h2').a['href']
                title = item.find('h2').a.string.strip()
                try:
                    locations = item.select('.add')[0].find_all('a')
                    location = locations[0].string + ' ' + locations[1].string
                except:
                    location = None
                if location:
                    csv_writer.writerow([title, location, houseUrl])
            if not url:
                break
        else:
            break


def crawl_ganji():
    url = 'http://sh.ganji.com/fang1/o1/'
    prefix = 'http://sh.ganji.com'
    csv_file = open('ganji.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    print('start fetch ganji..')
    print('fetching ganjiwang..')
    while True:
        sleep(1)
        response = requests.get(url, headers=header, allow_redirects=False)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            try:
                url = prefix + html.select('.next')[0]['href']
            except:
                url = None
            for item in html.select('.f-list-item .f-list-item-wrap'):
                houseUrl = prefix + item.find(class_='dd-item title').a['href']
                title = item.find(class_='dd-item title').a['title']
                try:
                    locations = item.select('.area')[0].find_all('a')
                    location = locations[0].string + ' ' + locations[2].string
                except:
                    location = None
                if location:
                    csv_writer.writerow([title, location, houseUrl])
            if not url:
                break
        else:
            break


def crawl_fangtx():
    url = 'http://zu.sh.fang.com/house/i3{page}/'
    prefix = 'http://zu.sh.fang.com'
    csv_file = open('fangtx.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')
    print('start fetch fangtx..')
    for i in tqdm(range(1, 101)):
        sleep(1)
        response = requests.get(url.format(page=i), headers=header, allow_redirects=False)
        if response.status_code == 200:
            html = BeautifulSoup(response.text, 'lxml')
            for item in html.select('.list .info'):
                try:
                    houseUrl = prefix + item.select('.title')[0].a['href']
                    title = item.select('.title')[0].a['title']
                    locations = item.find_all(class_='gray6 mt20')[0].find_all('a')
                    location = locations[0].string + ' ' + locations[1].string + ' ' + locations[2].string
                    csv_writer.writerow([title, houseUrl, location])
                except:
                    pass
        else:
            break


if __name__ == '__main__':
    try:
        crawl_lianjia()
        print('fetch lianjia done!')
    except:
        print('链家网挂了，需要更新抓取规则～')

    try:
        crawl_anjuke()
        print('fetch anjuke done!')
    except:
        print('安居客挂了，需要更新抓取规则～')

    try:
        crawl_58()
        print('fetch 58 done!')

    except:
        print('58同城挂了，需要更新抓取规则～')

    try:
        crawl_ganji()
        print('fetch ganji done!')
    except:
        print('赶集网挂了，需要更新抓取规则～')

    try:
        crawl_fangtx()
        print('fetch fangtx done!')
    except:
        print('房天下挂了，需要更新抓取规则～')
