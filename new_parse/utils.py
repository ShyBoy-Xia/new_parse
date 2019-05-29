# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午5:20
# @Author  : zhanzecheng
# @File    : utils.py
# @Software: PyCharm
"""
import jieba
import os
from model import TrieNode

def getStopwords():
	stopword = set()
	with open('data/stopword.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			stopword.add(line.strip())
	return stopword


def generate_ngram(data, n):
	"""
	参数ngram特征
	:param data: 数据集
	:param n:    n gram
	:return:
	"""
	result = []
	# 对 n gram 依次进行输出，追加到result, 当发现 数组长度 < n gram，就不计算了
	# i in (1, 2, .. n)
	for i in range(1, n+1):
		# 数组长度 < n gram，我们就停止 n gram 的计算
		if len(data) - i < 0:
			break
		# len(data) - i + 1 找到最后结束的 index
		for j in range(len(data) - i + 1):
			# 顺序截取词的大小( n gram )
			result.append(data[j:j+i])
	return result


def loadWords(filename):
	# 加载外部词频记录
	word_freq = {}
	# print('------> 加载外部词集')
	with open(filename, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line = line.split(' ')
			# 规定最少词频
			if int(line[1]) > 2:
				word_freq[line[0]] = line[1]
	return word_freq


def saveModel(model, filename):
	import pickle
	with open(filename, 'wb') as fw:
		pickle.dump(model, fw)


def loadModel(filename):
	import pickle
	with open(filename, 'rb') as fr:
		model = pickle.load(fr)
	return model

def create_root(rootName, dictName):
    if os.path.exists(rootName):
        root = loadModel(rootName)
        return root
    else:
        word_freq = loadWords(dictName)
        root = TrieNode('*', word_freq)
        saveModel(root, rootName)
        return root

def loadDate(fileName, stopwords):
    # 加载数据集
    data = []
    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = [x for x in jieba.cut(line, cut_all=False) if x not in stopwords]
            data.append(line)

    # 按照行进行切分句子，得到一个数组
    # [[行，切词], [], []]
    # print(data)
    return data


def loadDate2Root(data, root):
    # print('------> 插入节点')
    for i in data:
        # tmp 表示每一行自由组合后的结果（n gram）
        # tmp: [['它'], ['是'], ['小'], ['狗'], ['它', '是'], ['是', '小'], ['小', '狗'], ['它', '是', '小'], ['是', '小', '狗']]
        tmp = generate_ngram(i, 3)
        # print(tmp)
        for d in tmp:
            root.add(d)
            # print(d)
    # print('------> 插入成功')