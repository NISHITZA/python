from collections import OrderedDict
if __name__=='__main__':
    n=int(input())
    od=OrderedDict()
    for i in range(n):
        *items,price=input().split()
        price=int(price)
        item=' '.join(items)
        if(od.get(item)):
            od[item]=od[item]+price
        else:
            od[item]=price
    for i,v in od.items():
        print(i,v)       
        
        
