from data.dataProcess import dataProcess

#########数据清洗

if __name__=="__main__":
    dp=dataProcess()
    datas=dp.data_clean()
    datas=datas[:30]
    print(datas)