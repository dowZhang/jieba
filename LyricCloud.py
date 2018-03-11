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

def getChineseWords():
    text = []

def creatWordCloud():
    katy_color = np.array(Image.open(path.join(d, "backgroundGirl.png")))

    stop_words = set(STOPWORDS)
    stop_words.add(" ")

    wc = WordCloud(background_color="white", max_words=200, mask=katy_color, stopwords=stop_words, max_font_size=120,
                   random_state=42)
    wc.generate(getKeyWords())

    image_colors = ImageColorGenerator(katy_color)

    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.show()
