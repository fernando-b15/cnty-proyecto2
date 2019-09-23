from sys import stdin

m=[[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,1],[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0]]
v=[6,0,3,5,3,8]
def dinamicaclasica(m,v,t):
    for k in range(t):
        print(v)
        res=[]
        for j in m:
            cont=0
            for i in range(len(v)):
               
                cont+=int(j[i])*int(v[i])
            res.append(cont)

        v=res
    print(res)
def dinamicaprobabilistica(m,v,t):
    for k in range(t):
        res=[]
        for j in m:
            cont=0
            for i in range(len(v)):
               
                cont+=float(j[i])*float(v[i])
            res.append(cont)

        v=res
    print(res)    
def main():
    ope=stdin.readline().strip()
    if ope=="dinamica clasica":
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num5.append(num1)
            num1=stdin.readline().strip()
        print(num5)
        num4=stdin.readline().split()
        num3=int(stdin.readline())
        dinamicaclasica(num5,num4,num3)
    if ope=='dinamica probabilistica':
        num1=stdin.readline().strip()
        num5=[]
        while len(num1)!=0:
            num1=num1.split()
            num5.append(num1)
            num1=stdin.readline().strip()
        print(num5)
        num4=stdin.readline().split()
        num3=int(stdin.readline())
        dinamicaprobabilistica(num5,num4,num3)
main()        
