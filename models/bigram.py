from data.dataProcess import dataProcess
import numpy as np
from math import log
import re
dp=dataProcess()
class bigram():
    def __init__(self):
        #在dataProcess里面建好的词典
        self.wordDict,self.ind2word,self.word2ind=dp.build_dict()
        #datas是去掉停用词的
        self.datas=dp.data_clean()

    #根据worddict维护一个二维矩阵
    def build_matrix(self):
        dictLen=len(self.wordDict)
        trans=np.zeros([dictLen,dictLen], dtype=int)
        for data in self.datas:
            sLen=len(data)
            for i in range(1,sLen):
                if data[i-1] in self.wordDict and data[i] in self.wordDict:
                    trans[self.word2ind[data[i-1]]][self.word2ind[data[i]]]+=1
        return trans

    #构建DAG图
    def build_dag(self,sentence):
        dag={}
        N=len(sentence)
        for k in range(N):
            templist = []
            i = k
            frag = sentence[k]
            while i < N and frag in self.wordDict:  # 如果词语在词典里，则将当前的下标存放
                if self.wordDict[frag]:
                    templist.append(i)
                i += 1
                frag = sentence[k:i + 1]  # 获取下一个词
            if not templist:
                templist.append(k)
            dag[k] = templist
        return dag

    #计算最大概率,bigram的计算公式,加上laplace平滑，还没有evaluate
    def calc(self,sentence):
        N = len(sentence)
        route=[(0,0) for i in range(N+1)]
        DAG=self.build_dag(sentence)
        dictLen=len(self.wordDict)
        # 列表推倒求最大概率对数路径
        # route[idx] = max([ (概率对数，词语末字位置) for x in DAG[idx] ])
        # 以idx:(概率对数最大值，词语末字位置)键值对形式保存在route中
        # route[x+1][0] 表示 词路径[x+1,N-1]的最大概率对数,
        # [x+1][0]即表示取句子x+1位置对应元组(概率对数，词语末字位置)的概率对数
        trans=self.build_matrix()
        word2ind=self.word2ind
        for idx in range(N - 1, -1, -1):
            for x in DAG[idx]:
                now=sentence[idx:x+1]
                then=sentence[x+1:route[x+1][1]]
                if now in self.wordDict and then in self.wordDict:
                    route[idx] = [((log(trans[word2ind[now]][word2ind[then]])+log(sum(trans[word2ind[now]])) or 1)+ route[x + 1][0], x)]
            route[idx] = max(route[idx])
        return route
    #分词接口
    def cut(self,sentence):
        x = 0
        N = len(sentence)
        route=self.calc(sentence)
        words=[]
        pre=0
        for i in range(len(route)):
            next = route[i][1]
            words.append(sentence[pre:next+1])
            pre=next+1
        return words










