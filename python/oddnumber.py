# a=int(input('enter starting number')) 
# b=int(input('enter ending number'))

# for i in range(a,b):
#     if(i%2==1):
#      print(i)



# a=int(input('enter starting number'))
# b=int(input('enter ending number'))
# sum = 0
# for i in range(a,b+1):
#     sum = sum + i
# print('sum=',sum) 





a = int(input('enter starting number: '))
b = int(input('enter ending number: '))
sum = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        sum += i
print('Sum of odd numbers:', sum)


