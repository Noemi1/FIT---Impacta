# -*- coding: utf-8 -*-
# pequena = int(input('quantas garrafas pequenas(350ml) vc comprou?'))
# media = int(input('quantas garrafas pequenas(600ml) vc comprou?'))
# grande = int(input('quantas garrafas pequenas(2000ml) vc comprou?'))
# 
# # -----------------------------------------------------------
# total_p = pequena * 350
# total_m = media * 600
# total_g = grande * 2000
# 
# print(total_p, total_m, total_g)
# 
# total = total_p + total_m + total_g
# conversor = total / 1000
# print('vc comprou ',conversor,' litros de refri',)
# 

# # -----------------------------------------------------------
#lista = [1,2,3,4,5,6]
#for x in lista:
#    print(x)


# # -----------------------------------------------------------
# dicti = {'noemi': 1, 'joep': 2, 'josenilton': 5, 'ana':3}
# for i, v in dicti.items():
#     print(i, ':', v)
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# n4 = int(input())
# n5 = int(input())

# n = [n1,n2,n3,n4,n5]
# print ('maior:', max(n))
# print ('menor:', min(n))

# -----------------------------------------------------------
# n = int(input())
# arr = []
# for i in range(n):
#     x = input()
#     arr.append(x)
# print('n', n)
# print('list', arr)

# # -----------------------------------------------------------
# dia = int(input())
# def day_week(dia):

#     if dia <= 7 and dia > 0:
#         if dia == 1: 
#             print('domingo')
#         elif dia == 2: 
#             print('segunda')
#         elif dia == 3: 
#             print('terca')
#         elif dia == 4: 
#             print('quarta')
#         elif dia == 5: 
#             print('quinta')
#         elif dia == 6: 
#             print('sexta')
#         elif dia == 7: 
#             print('sabado')
#     else:
#         print('data invalida')
#     return

# day_week(dia)

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())

# media = (n1 + n2 + n3) / 3
# quant = 0

# print(media)

# if n1 > media:
#     quant = quant + 1
# if n2 > media:
#     quant = quant + 1
# if n3 > media: 
#     quant = quant + 1

# print(quant)

# -----------------------------------------------------------
# n = int(input())

# def impar(n):
#     if n % 2 == 0:
#         print('par')
#     else:
#         print('impar')
#     return
# impar(n)

# -------------------------------------------------------------------------------

n = 10
lista = []
while n >= 5:
    arr = input()
    lista.append(arr)
    n = n - 1
print(lista)

# n = 50
# while n <= 100:
#     print(n)
#     n = n + 1

