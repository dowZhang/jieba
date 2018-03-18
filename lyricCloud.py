#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba

d = path.dirname(__file__)

def getKeyWords():
    text = open(path.join(d, 'lyric.txt')).read()
    return text

def creatWordCloud():
    katy_color = np.array(Image.open(path.join(d, "backgroundGirl.png")))

    stop_words = ['作曲', '作词', 'oh', 'doo', 'and', 'you', 'in', 'ho', 'it', 'that', 'by', 'But', 'so', 'to', 'the', 'na', 'of', 'don', 'from']

    wc = WordCloud(font_path=path.join(d, 'youyuan.TTF'), background_color="white", max_words=200, mask=katy_color, stopwords=stop_words, max_font_size=120,
                   random_state=42)
    text = getKeyWords()
    word_generate = jieba.cut(text, cut_all=False)
    for word in word_generate:
        if word not in stop_words:
            text = "/".join(word_generate)
    wc.generate(text)

    image_colors = ImageColorGenerator(katy_color)

    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()
