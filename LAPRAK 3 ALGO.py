# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 00:02:34 2022

@author: Elita
"""

# Program Mencari Akar Persamaan Kuadrat dan Determinan

import math as m

#input
print("program pencari persamaan kuadrat dan determinan")

x1=int(input('nilai a(x²): '))
x2=int(input('nilai b(x): '))
x3=int(input('nilai c: '))

#determinan

if x1==0:
    print('bukan persamaan kuadrat')
else:
    D = pow(x2, 2)-(4*x1*x3)
    if (D>0):
        d1 = ((-x2)+m.sqrt(D))/(2*x1)
        d2 = ((-x2)-m.sqrt(D))/(2*x1)
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('mempunyai akar x yang berbeda')
        print('akar (x) pertama:',d2)
        print('akar (x) kedua:',d1)
    elif D==0:
        d1 = (x2)/(2*x1)
        d2 = (x2)/(2*x1)
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('mempunyai akar x yang sama')
        print('akar (x) pertama:',d2)
        print('akar (x) kedua:',d1)
    elif D<0:
        print('persamaan kuadrat:',x1,'x² +',x2,'x +',x3)
        print('determinan: ',D)
        print('merupakan akar imaginer')
        print('akar (x) pertama: ',x2,'+√',D,'/2',x1)
        print('akar (x) pertama: ',x2,'-√',D,'/2',x1)
    else:
        print('tidak bisa dihitung')
        
print("==========================================")
print("065002200038 - Elita Wahyu Firdasari")