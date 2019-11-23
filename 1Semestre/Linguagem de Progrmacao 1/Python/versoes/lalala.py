# n = float(input())
# soma = 0
# qtd = 0
# while n != -999:
#     soma += n
#     qtd += 1
#     n = float(input())
# m = soma / qtd
# print(m)

# a = int(input())
# b = int(input())
# for i in range(a-1, b, -1):
#     print(i)

num = int(input())
while num < 0:
    print('numero invalido, digite outro:', end='')
    num = int(input())
if num % 2 == 1:
    print('nao primo')
else:
    print('primo')