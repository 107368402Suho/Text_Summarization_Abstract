#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from textrank4zh import TextRank4Keyword, TextRank4Sentence, Segmentation
import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)


def get_textrank4zh_keywords(contents):
    """
    获取文本关键字
    :param contents: string
    :return: dict of list [{x},{x}]
    """
    # 定义返回前10个关键词
    topK = 10
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=contents, lower=True)

    # logger.info('使用textrank4zh提取关键词，默认提取10个')
    # print('摘要：')
    # for item in tr4w.get_keywords(10, word_min_len=1):
    #     print(item.word, item.weight)
    result_topK = tr4w.get_keywords(topK, word_min_len=1)

    result = []
    # 封装成指定字典格式
    for i, wp in enumerate(result_topK):
        result.append({
            'cat': i,
            'word': wp['word'],  # 关键字
            'weight': round(wp['weight'], 4),  # 权值
            'value': round(wp['weight'] * 10000, 2)  # 用户画图用的，想办法权值差异化更加明显，画图更有区分
        })

    return result


def get_textrank4zh_keywords_phrase(contents):
    """
    获取文本关键字短语，这个功能有点不完善，不好用
    :param contents: string
    :return: dict of list [{x},{x}]
    """
    # 定义返回前20个关键词短语
    topK = 20
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=contents, lower=True)

    # logger.info('使用textrank4zh提取关键词短语，默认提取20个')

    # print('关键短语：')
    # for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num=2):
    #     print(phrase)

    result = tr4w.get_keyphrases(keywords_num=topK, min_occur_num=2)

    return result


def get_textrank4zh_summarization(contents):
    """
    获取文本摘要
    :param contents: string
    :return: dict of list [{x},{x}]
    """
    # 定义返回前5个文本摘要
    topK = 5
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=contents, lower=True, source='all_filters')

    # logger.info('使用textrank4zh提取摘要，默认提取5个')

    # print('摘要：')
    # for item in tr4s.get_key_sentences(num=5):
    #     print('文本位置：{}, 权重：{}，内容：{}'.format(item.index, item.weight, item.sentence))  # index是语句在文本中位置，weight是权重

    result = tr4s.get_key_sentences(num=topK)

    return result


def get_textrank4zh_summarization_str(contents):
    """
    获取文本摘要，返回的是string
    :param contents: string
    :return: string
    """
    # 定义返回前5个文本摘要
    topK = 5
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=contents, lower=True, source='all_filters')

    # logger.info('使用textrank4zh提取摘要，默认提取5个')
    # print('摘要：')
    # for item in tr4s.get_key_sentences(num=5):
    #     print('文本位置：{}, 权重：{}，内容：{}'.format(item.index, item.weight, item.sentence))  # index是语句在文本中位置，weight是权重

    result_topK = tr4s.get_key_sentences(num=topK)

    temp = []
    for item in result_topK:
        sent = item['sentence']
        temp.append(sent)

    return ''.join(temp)


if __name__ == "__main__":
    text = " 随便复制一篇新闻 "
    

if __name__ == '__main__':

    text = text.replace('\u3000', '').replace('\xa0', '').replace('\ufeff', '').replace('\n', '').replace('\\n', '')
    keyWords = get_textrank4zh_keywords(text)
    print('获取关键词：', keyWords)
    keyWords_phrase = get_textrank4zh_keywords_phrase(text)
    print('获取关键短语：', keyWords_phrase)

    extract = get_textrank4zh_summarization(text)
    print('获取摘要：', extract)

    extract_str = get_textrank4zh_summarization_str(text)
    print('获取摘要string：', extract_str)
