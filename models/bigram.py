from data.dataProcess import dataProcess
import numpy


class bigram():
    def __init__(self):
        pass
    #构建DAG图
    def getDAG(self, sentence):
        s_len = len(sentence)

        DAG = [([0] * (s_len + 1)) for i in range((s_len + 1))]

        for i in range(s_len + 1):
            s_t = self.findWord(sentence[i:])
            if i != s_len:
                DAG[i][i + 1] = 1
            for t in s_t:
                DAG[i][i + t] = 1
        return DAG

    # DAG图怎么构建，是需要传进来的
    # 计算DAG的最大概率路径
    def maxProbPath(self, sentence, DAG):
        sent_len = len(sentence)
        # dp矩阵
        dp = []
        for i in xrange(sent_len + 1):
            dp.append({})
        dp[0]['prob'] = 0
        dp[0]['word'] = '<s>'
        dp[0]['prenode'] = -1
        for i in range(1, sent_len + 1):
            prelist = list(x[i] for x in DAG)
            dp[i]['prob'] = None
            for j in xrange(len(prelist)):
                if prelist[j] == 1:
                    prob = dp[j]['prob'] + self.dict.get2GramProbLog(dp[j]['word'], sentence[j:i])
                    if dp[i]['prob'] == None or (dp[i]['prob'] != None and prob > dp[i]['prob']):
                        dp[i]['prob'] = prob
                        dp[i]['word'] = sentence[j:i]
                        dp[i]['prenode'] = j
        result_list = []
        node = sent_len
        while node != -1:
            result_list.append(node)
            node = dp[node]['prenode']
        result_list.reverse()
        return result_list

class tool_tire():

    def __init__(self):
        self.root = {}
        pass

    def addWord(self, word):
        p = self.root
        for i in word:
            if i in p.keys():
                p = p[i]
            else:
                p[i] = {}
                p[i]['flag'] = False
                p = p[i]
        p['flag'] = True
        pass

    def isContain(self, word):
        p = self.root
        for i in word:
            if i in p.keys():
                p = p[i]
            else:
                return False
        if p['flag']:
            return True
        else:
            return False

    def getWrodN(self, word):
        N = []
        p = self.root
        flag = True
        for i in range(0, len(word)):
            c = word[i]
            if c in p.keys():
                p = p[c]
                if p['flag']:
                    N.append(i + 1)
            else:
                flag = False
                break
        return N, flag

    def getData(self):
        return self.root

    def setData(self, root):
        self.root = root