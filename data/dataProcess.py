import numpy
import os
from config import DefaultConfig
import re
opt=DefaultConfig()



class dataProcess():

    def __init__(self,path_data=opt.path_data):
        self.unclean_path=os.path.join(path_data,"PeopleDaily199801.txt")
        self.clean_path=os.path.join(path_data,"199801.txt")
        self.stopwords_path=os.path.join(path_data,"stopwords.txt")
    #数据清洗
    def data_clean(self):
        stopWords = open(self.stopwords_path, 'r', encoding="utf_8").read().split('\n')
        if os.path.exists(self.unclean_path):
            lines=open(self.unclean_path,"r",encoding="utf-8").readlines()
            datas=[]
            for line in lines:
                if len(line.split())!=0:#去除空行
                    data=[]
                    words=line.split()
                    for unclean_word in words[1:]:
                        clean_word=unclean_word.split('/')[0]
                        #去掉了停用词
                        if clean_word in stopWords:
                            pass
                        else:
                            data.append(clean_word)
                datas.append(data)
        return datas
    def build_dict(self):
        #需要词表有词频。。需要去掉词频太低的;单词：序号;序号：单词;返回三个
        #得把训练集分出来。。8：2
        datas=self.data_clean()
        #data=datas[:len(datas)*0.8]
        wordDict={}
        for data in datas:
            for word in data:
                if word in wordDict:
                    wordDict[word]+=1
                else:
                    wordDict[word]=1
        #对wordDict按词频进行排序
        wordDict=sorted(wordDict.items(),key=lambda item:item[1],reverse=True)
        word2ind={}
        ind2word={}
        for i in range(len(wordDict)):
            word2ind[wordDict[i]]=i
        ind2word={word2ind[w]:w for w in word2ind}
        return wordDict,ind2word,word2ind












