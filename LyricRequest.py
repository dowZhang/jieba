#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup
import re
import lyricCloud

#获取html文件
def getJsonObjWithArtistId(artist_id):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID-WYYY=UFoDlOIjiQ34BuD13JaTX5CkZKGpI%5Ck1kIIOvE5RzcoPNh8w%2F0pf6Ekt8CkFInVlzAAI%2FEFjGx1Y0DBSe88mS%2FMSKr9e1MqkGbfSv7V52M3PWDwxde%2FBG6qG7Ck7qypk9lrUUEkrKooPUJBnC8krC3vJItP%2B96SebxIdZkaeVCmj3ifw%3A1519654639112; _iuqxldmzr_=32; _ntes_nnid=6cb71378e7fcf19ffc17c2115d0f4aa7,1518243330713; _ntes_nuid=6cb71378e7fcf19ffc17c2115d0f4aa7; __utma=94650624.153865058.1518243331.1519645879.1519651992.6; __utmz=94650624.1519645879.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=94650624; __utmb=94650624.4.10.1519651992',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0'
    }
    url = 'http://music.163.com/artist?id=' + str(artist_id)
    r = requests.get(url, headers=headers)
    wrapJsonObj(r.text)


#解析html文件
def wrapJsonObj(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find('ul', class_='f-hide')
    songs = []
    for child in ul.find_all('li'):
        href = child.a['href']
        pattern = re.compile(r'\d+')
        songs.append(pattern.findall(href)[0])

    for song_id in songs:
        getDataWithSongId(song_id)

#获取歌词
def getDataWithSongId(song_id):

    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + song_id + '&lv=1&kv=1&tv=-1'
    r = requests.get(url=url)
    json_obj = r.text
    j = json.loads(json_obj)
    text = (j['lrc']['lyric'])

    with open('lyric.txt', 'a') as f:
        f.write(text)

getJsonObjWithArtistId(62888)
#6452 62888
lyricCloud.creatWordCloud()