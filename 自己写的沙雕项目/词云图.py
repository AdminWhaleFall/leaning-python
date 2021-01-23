'''
Author: whalefall
Date: 2021-01-22 14:42:59
LastEditors: whalefall
LastEditTime: 2021-01-23 21:11:14
Description: 生成百度热点词云图
'''
from wordcloud import WordCloud
import jieba  # 中文分词
import syss+

path = sys.path[0]

def draw(text):
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/simyou.ttf",  # SIMYOU.TTF simkai.ttf
                          # background_color="white",
                          width=1080,
                          height=720,
                          max_font_size=80,
                          # min_font_size=15,
                          # 词语水平方向排版出现的频率
                          prefer_horizontal=1,
                          # relative_scaling=True
                          # stopwords="我,的"
                          max_words=1000,
                          scale=2.0,
                          # stopwords=STOPWORDS.add('的')

                          ).generate(text)

    img = wordcloud.to_image()
    save = wordcloud.to_file("{}//平洲二中2018届名字.jpg".format(path))
    img.show()


def ch_jieba(text):
    wordList = jieba.cut(text)
    result = " ".join(wordList)
    print(result)
    return result


# with open("{}//撒野.txt".format(path), "r", encoding="utf8") as f:
#     t = f.read().replace("\n", "").replace("\r", "").replace(" ", "").replace("-", "")
#     # print(t)
#
# r=ch_jieba(t)
# draw(r)

with open("{}//pzez_name.txt".format(path), "r", encoding="utf8") as f:
    n = f.readlines()
    name_str = ""
    for name in n:
        name = name.replace("\n", "")
        name_str = name_str+name+","
    print(name_str)
    draw(name_str)
