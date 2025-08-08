l=[1,2,1,2,3,4]
c=l.count(1)
p=l.index(3)
c=l.copy()


l=[1,2,3,4]
l2=l. copy()
l2.pop()
print(l)
print(l2)

# for loop in list
no=int(input('enter number of students:'))
students=[]
for i in range(no):
    name=input('enter name:')
    students.append(name)
print(students)