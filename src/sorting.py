
def Sort1(list):
    listSize=len(list)
    for i in range(0,listSize-1,1):
        listMin=list[i]
        pos=i
        for k in range(i+1,listSize,1):
            if list[k]<listMin:
                listMin=list[k]
                pos=k
        aux=list[i]
        list[i]=listMin
        list[pos]=aux
    return list

def Sort2(list):
    listLen=len(list)
    for i in range(0,listLen-1,1):
        min=list[i]
        pos=i
        for k in range(i+1,listLen-1,1):
            if list[k][0]<min[0]:
                min=list[k]
                pos=k
        aux=list[i]
        list[i]=list[pos]
        list[pos]=aux
    return list

list1=[1,5,28,4,'aaa',2,1,'Simone']
list2=[('Tasso',10),('Tasso',9),(1983,'f'),('Petrarca',99),(876,90),(-2,-1),(-1,12,'abc'),(9.4,'Euklid')]

print(list1);
print(list2);
print('Sort1 :',Sort1(list1))
print('Sort1 :',Sort1(list2))
list2=[('Tasso',10),('Tasso',9),(1983,'f'),('Petrarca',99),(876,90),(-2,-1),(-1,12,'abc'),(9.4,'Euklid')]
print('Sort2 :',Sort2(list2))
