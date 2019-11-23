# a = int(input())
# b = int(input())
# b += 1

# while a > b:
#     a = a - 1
#     print(a)

# a = int(input())
# b = int(input())
# def decresce(a,b):
#     b += 1

#     while a > b:
#         a = a - 1
#         print(a)

# decresce(a,b)0
# a = int(input())
# b = int(input())

# def decresce(a,b):
#     b +=1
#     while a > b:
#         a -= 1
#         print(a)
# decresce(a,b)

s = 0
c = 0
x = 1

while x <= 7 and s <= 560:
	p = float(input())
	if p == 0: break
   
    elif p > 0:
        s = s + p
        c = c + 1
        x = x + 1

print(c)
print("%.1f" % s)