from data.dataProcess import dataProcess
from models.bigram import bigram
#########数据清洗

if __name__=="__main__":
    bigram=bigram()
    bi=bigram.cut("我爱北京天安门")
    print(bi)