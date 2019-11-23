# x = 50
# n = 1
# while x <= 100: 
#     if n <= 9: 
#         print(x, end=' ')
#         n = n + 1
#     else:
#         n = 1
#         print(x)
#     x = x + 1


# n = int(input())
# x = 0
# while x < n:
#     x = x + 1
#     print(x)

# s = 0
# c = 1

# while c <= 5:
#     n = int(input())
#     s = s + n
#     c = c + 1
#     print(n)
# print('c = %d soma = %d' %(s,c))

rg = int(input('rg:'))
x = 0
while rg > 0:
    x = x + (rg % 10)
    rg = rg // 10 
    ra = rg / 10
    #print('x = %, rg = %, ra = %', %(x) %(rg) %(ra))
    print('x = {}, rg = {}, ra = {}'.format( x, rg, ra))
print(x, ra)
