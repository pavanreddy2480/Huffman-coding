from heapq import heapify, heappop,heappush

class node:
    def __init__(self,ch,freq,left=None,right=None):
        self.ch=ch
        self.freq=freq
        self.left=left
        self.right=right
        self.st=""
    def __lt__(self,other):
        return self.freq<other.freq

text="AAAAAABBC"

def Huffman(string):
    if len(string)==0:
        return
    freq={ch: string.count(ch) for ch in set(string)}
    lst=[node(p,q) for p,q in freq.items()]
    heapify(lst)
    while len(lst)>1:
        left,right=heappop(lst),heappop(lst)
        newfreq=left.freq+right.freq
        heappush(lst,node(None,newfreq,left,right))
    root=lst[0]
    return root

d={}

def order(main,bin,var):
    main.st=var+bin
    if main.ch!=None:
        d[main.ch]=main.st[1:]
        return
    var=main.st
    order(main.left,"0",var)
    order(main.right,"1",var)
    


n=Huffman(text)
order(n,"0","")
for p,q in d.items():
    print((p,q))


def convertor(book,string):
    compressed=""
    for i in string:
        compressed=compressed+book[i]
    return compressed

print(convertor(d,text))


def decoder(book,str):
    check=""
    message=""
    l=[i for i in str]
    l=l[::-1]
    # print(l)
    while len(l)>0:
        check=check+l.pop()
        for p,q in book.items():
            if check==q:
                message=message+p
                check=""
                break
                # print("ran")
    return message

print(decoder(d,convertor(d,text)))    
