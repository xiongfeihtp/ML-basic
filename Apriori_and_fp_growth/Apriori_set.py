import numpy as np

def loadDataSet():
    return [[1,3,4],[2,3,4],[1,2,3,5],[2,5]]

def createC1(dataSet):
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #frozenset 不可更改，存在hash值，可以做为字典中的键值
    return list(map(frozenset,C1))

def scanD(D,Ck,minSupport):
    ssCnt={}
    #每一次都要扫描全部数据集
    for tid in D:
        for can in Ck:
            #测试can中每一个元素都在t中
            if can.issubset(tid):
                #去除字典中的value，默认值设为0
                ssCnt[can]=ssCnt.get(can,0)+1

    numItems=float(len(D))
    retList=[]
    supportData={}

    for key in ssCnt:
        support=ssCnt[key]/numItems
        if support>=minSupport:
            #为什么要在零的位置插入
            retList.insert(0,key)
            supportData[key]=support
    return retList,supportData
#生成无重复组合
def aprioriGen(Lk,k):
    reList=[]
    lenLk=len(Lk)
    #遍历两两集合
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1=list(Lk[i])[:k-2];L2=list(Lk[j])[:k-2]
            L1.sort();L2.sort()
            if L1==L2:
                #集合的并
                reList.append(Lk[i]|Lk[j])
        return reList

def apriori(dataSet,minSupport=0.5):
    C1=createC1(dataSet)
    D=map(set,dataSet)
    L1,supportData=scanD(D,C1,minSupport)
    L=[L1]
    k=2
    while (len(L[k-2])>0):
        Ck=aprioriGen(L[k-2],k)
        Lk,supK=scanD(D,Ck,minSupport)
        supportData.update(supK)
        L.append(Lk)
        k+=1
    return L,supportData












