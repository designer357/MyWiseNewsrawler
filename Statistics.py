__author__ = 'chengmin'
import os
import chardet
import time
start=time.clock()
folders=[x for x in os.listdir(os.getcwd()) if os.path.isdir(x)==True and '10-' in x]
print(folders)
def Initlization():
    dict_name={}
    list_name=[]
    title_weight=1
    with open("name.txt")as fin1:
        for eachline1 in fin1:
            val1=eachline1.split(' ')
            dict_name[val1[0]]='0'
            list_name.append(val1[0])
    return dict_name,list_name,title_weight

#dict_name,list_name,title_weight=Initlization()

for eachfolder in folders:
    print(eachfolder+" is processing")

    dict_name,list_name,title_weight=Initlization()

    eachfolder_size=len(os.listdir(os.path.join(os.getcwd(),eachfolder)))

    for eachfile in os.listdir(os.path.join(os.getcwd(),eachfolder)):
        eachfolder_size-=1
        print(str(eachfolder_size)+"left...^_^")
        list_temp=[0 for x in range(len(dict_name))]

        with open(os.path.join(os.path.join(os.getcwd(),eachfolder),eachfile),"rb")as fin2:#unicode step1: rb
            eachlines=fin2.readlines()
            mytype=chardet.detect(eachlines[0])["encoding"]#unicode step2:detect type using chardet
            eachlines=eachlines[0].decode(mytype)
            #eachlines=eachlines[0].decode(mytype).encode("utf-8").decode("utf-8")#unicode step3:first decode from mytype to unicode/which is str

            for x in range(len(dict_name)):#find the company name is shown in content and compute the times
                list_temp[x]=list_temp[x]+eachlines.count(list_name[x].strip())
                list_temp[x]=list_temp[x]+eachfile.count(list_name[x].strip())*title_weight#compute the value that company name shown in title

            if max(list_temp)==0:
                pass
            else:
                y_indexes=[i for i,v in enumerate(list_temp) if v==max(list_temp)]
                for y in y_indexes:
                    dict_name[list_name[y]]=str(int(dict_name[list_name[y]])+1)

    with open(eachfolder+".txt",'w')as fout2:
        for (k,v) in dict_name.items():
            fout2.write(k+'\t\t'+v+'\n')

end=time.clock()
print("The total time is "+str(end-start)+" secs...")


