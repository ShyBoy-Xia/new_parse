# -*- coding: utf-8 -*-

from utils import getStopwords, loadDate, loadDate2Root, create_root

def new_parse(rootName, dictName, fileName, N):
    """短语抽取
    :param rootName:字典树，用于存储单词和统计词频。
                如果root.pkl文件存在则直接读取。
                如果没有就生成字典树，并存储模型到文件root.pkl
    :param dictName: 所使用的字典。
    :param fileName：需要分析的文本文件。
    :param N：设置结果显示的个数。即返回前多少个结果。

    :return： 结果列表
    :rtype: list

    """
    stopwords = getStopwords()
    root = create_root(rootName, dictName)
    # 加载新的文章
    data = loadDate(fileName, stopwords)
    # 将新的文章插入到Root中
    loadDate2Root(data, root)

    result, add_word = root.wordFind(N)
    final_result = []
    for word, score in add_word.items():
        final_result.append(word + ',' + str(score))
    return final_result
