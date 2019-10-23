from sys import stdin
import matplotlib.pyplot as plt
m=[[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,0,1],[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,0,0,0,0]]
v=[6,0,3,5,3,8]
def dinamicaclasica(m,v,t):
    for k in range(t):
        res=[]
        for j in m:
            cont=0
            for i in range(len(v)):
                cont+=j[i][0]*v[i][0][0]
            res.append([[cont,0]])

        v=res
    print(res)
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes

    nombres = ['pto 0','pto 1','pto 2','pto 3','pto 4','pto 5','pto 6','pto 7','pto 8','pto 9','pto 10','pto 11','pto 12']
    datos = [res[0][0][0],res[1][0][0],res[2][0][0],res[3][0][0],res[4][0][0],res[5][0][0],res[6][0][0],res[7][0][0],res[8][0][0],res[9][0][0],res[10][0][0],res[11][0][0],res[12][0 ][0]]
    xx = range(len(datos))

    ax.bar(xx, datos, width=0.5, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)

    plt.show()
    
def dinamicaprobabilistica(m1,m2,v1,v2,t):
     mz=productoTensorial(m1,m2)
     vz=productoTensorialVectores(v1,v2)
     print(mz)
     print(vz)
     for i in range(5):
         vz=accionMatrizSobreVector(vz,mz)
         print("xd",vz)
     print(vz)
     fig = plt.figure(u'Gráfica de barras') # Figure
     ax = fig.add_subplot(111) # Axes

     nombres = ['00','01','02','10','11','12','20','21','22','30','31','32']
     datos = [vz[0][0],vz[1][0],vz[2][0],vz[3][0],vz[4][0],vz[5][0],vz[6][0],vz[7][0],vz[8][0],vz[9][0],vz[10][0],vz[11][0]]
     xx = range(len(datos))

     ax.bar(xx, datos, width=0.5, align='center')
     ax.set_xticks(xx)
     ax.set_xticklabels(nombres)

     plt.show()
def valoresobservables(m,v):
    vp=normaVectorImaginario(v)
    
    vxyz=multiplicacionEscalarVector(((1/vp),0),v)
    
    vfin=[]
    for i in vxyz:
        vfin.append([i])
        
    mz=productoMatricesImaginarias(m,vfin)

    mz2=matrizAdjunta(mz)

    mf=productoMatricesImaginarias(mz2,vfin)
    print(mf)
    my=mf[0][0][0]
    mi=[[[my,0],[0,0],[0,0],[0,0]],[[0,0],[my,0],[0,0],[0,0]],[[0,0],[0,0],[my,0],[0,0]],[[0,0],[0,0],[0,0],[my,0]]]
 
    for i1 in range(len(m)):
        for j1 in range(len(m[0])):
            m[i1][j1][0]=m[i1][j1][0]-mi[i1][j1][0]
            
    mat=productoMatricesImaginarias(m,m)
    vfin3=matrizAdjunta(vfin)
    matx=productoMatricesImaginarias(vfin3,mat)
    matz=productoMatricesImaginarias(matx,vfin)
    print(matz)
    
def main():
    ope=stdin.readline().strip()
    if ope=="valores observables":
        m=[[[0,0],[0,-1/2],[0,-1],[-7/2,0]],
 [[0,1/2],[0,0],[7/2,0],[0,-1]],
 [[0,1],[7/2,0],[0,0],[0,-1/2]],
 [[-7/2,0],[0,1],[0,1/2],[0,0]]
]
        v=[[-2, 1],
 [1, 0],
 [0,-1],
 [3,2]
]
        valoresobservables(m,v)
    elif ope=="particula en recta":
        v1=[[2, -1],
         [-1.5, 2.5],
         [-3.5, 5],
         [-4, 6],
         [-3.5, 2.5],
         [0, 0],
         [-3.5, 2.5],
         [6, -4],
         [0, 2.5],
         [-1, 1]]       
        print(particulaLineaRecta(v1))
def normaImaginario(c1):
    suma = 0
    suma = (c1[0]**2) +(c1[1]**2)
    return suma        
     
def particulaLineaRecta(v1):
    probabilidad=[]
    normaVectorCuadrado = (normaVectorImaginario(v1))**2
   
    for i in v1:
        j =(normaImaginario(i))/normaVectorCuadrado
        probabilidad.append(round(((normaImaginario(i))/normaVectorCuadrado),4))
    
    return probabilidad        
def multiplicacionEscalarVector(c1,v1):
    res = []
    for i in range(len(v1)):
        res.append(productoImaginarios(c1,v1[i]))
    return res        
def normaVectorImaginario(v1):
    suma =0
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            suma += ((v1[i][j])**2)
    return suma**(1/2)        
def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(len(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini

def sumaImaginarios(c1,c2):
    c3 = [0,0]
    c3[0] = c1[0] + c2[0]
    c3[1] = c1[1] + c2[1]
    return (c3[0],c3[1])

def productoImaginarios(c1,c2):
    c3 = [0,0,0,0]
    res = [0,0] 
    m = 0
    for j in c1:
        for i in c2:
            c3[m] = j*i
            m += 1        
    res[0] = c3[0] + (-1*c3[3]) 
    res[1] = c3[1] + c3[2]
    return (res[0],res[1])

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
        
    return v


def multiplicacionMatrizVector(v1,m1):
    vector = [] 
    for i in range(len(m1)):
        suma = 0
        for j in range(len(m1[i])):
            mult= m1[i][j]*v1[j]
            suma += mult
        vector.append(suma)
    return vector 


def productoTensorial(m1,m2):
    matriz = []
    for i in range(len(m1)):
        matM = [[]] *len(m2)
        for j in range(len(m1[i])):
            m3 = complejoPorMatriz(m1[i][j],m2)
            for k in range(len(m2)):
                matM[k] = matM[k] + m3[k]
        for k in range(len(m2)):
            matriz.append(matM[k])
    return matriz



def vectorPorEscalar(n,vector):
    newVector = []
    for i in range(len(vector)):
        comp = n * vector[i]
        newVector.append(comp)
    return newVector
            
def productoTensorialVectores(v1,v2):
    vFinal = [0 for i in range(len(v1)*len(v2))]
    cont = 0
    for i in range(len(v1)):
        v3 = complejoPorvector(v1[i],v2)
        for k in range(len(v3)):
            vFinal[cont] = v3[k]
            cont+=1
    return vFinal
def matrizPorEscalar(n,matriz):
    mat = [[0]*len(matriz) for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            mat[i][j] = n * matriz[i][j]
    return mat
def complejoPorMatriz(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append(productoImaginarios(m1[i][j],c1))
        matriz.append(vector)
    return matriz
def complejoPorvector(c1,m1):
    matriz=[]
    for i in range(0,len(m1)):
        
            matriz.append(productoImaginarios(m1[i],c1))
        
    print(matriz)
    return matriz
def matrizConjugada(m1):
    matriz=[]
    for i in range(0,len(m1)):
        vector=[]
        for j in range(0,len(m1[0])):
            vector.append((m1[i][j][0],m1[i][j][1]*-1))
        matriz.append(vector)
    return matriz


def matrizAdjunta(m1):
    matriz=matrizTranspuesta(m1)
    matriz=matrizConjugada(matriz)
    return matriz


def productoMatricesImaginarias(m1,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(m1[i],columna)
    return matriz

def accionMatrizSobreVector(v1,m1):
    v = []
    for i in range(len(m1)):    
            v.append(productoVectoresImaginarios(v1,m1[i]))
    return v
def matrizTranspuesta(m1):
    matriz=[]
    for i in range(0,len(m1[0])):
        columna = [row[i] for row in m1]
        matriz.append(columna)
    return matriz 
        

main()        
