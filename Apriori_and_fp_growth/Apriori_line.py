from Apriori_and_fp_growth.Apriori_set import *

def generateRules(L,supportData,minConf=0.7):
    bigRuleList=[]
    for i in range(1,len(L)):
        for freqSet in L[i]:
            #某一层次的候选集合
            H1=[frozenset([item]) for item in freqSet]
            if (i>1):
                H1=calcConf(freqSet,H1,supportData,bigRuleList,minConf)
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList


def calcConf(freqSet,H,supportData,brl,minConf=0.7):
    prunedH=[]
    for conseq in H:
        conf=supportData[freqSet]/supportData[freqSet-conseq]
        if conf>=minConf:
            print(freqSet-conseq,'--->',conseq,'conf:',conf)
            brl.append((freqSet-conseq),conseq,conf)
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    m=len(H[0])
    if (len(freqSet)>(m+1)):
        Hmp1=aprioriGen(H,m+1)
        Hmp1=calcConf(freqSet,Hmp1,supportData,brl,minConf)
        if (len(Hmp1)>1):
            rulesFromConseq(freqSet,Hmp1,supportData,brl,minConf)

"""  
更简单的结构，避免了递归          
def rulesFromConseq(freqSet,H,supportData,brl,minConf=0.7):
    m=len(H[0])
    while (len(freqSet)>m):
        H=calcConf(freqSet,H,supportData,brl,minConf)
        if(len(H)>1):
            H=aprioriGen(H,m+1)
            m+=1
        else:
            break
"""



