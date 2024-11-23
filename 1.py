print("devops411")
str1="Ggg"
int1=5
float1=7.
float2=7.1
list1=[1,2,3,4,5]
dict1={'Name':"Ivan","Second Name":"Ivanov","BirtthDate":"25/05/1970"}
tuple1=(1,2,3,4,5)
set1={1,2,3,4}
print(type(set1))

for i in list1:
    print(i)


def list_cicle(l):
    for i in l:
        print(i, end=";")

list2=['Имя',"Фамилия","Отчество","Дата рождения"]
list_cicle(list2)
print()
a=int(input())
if a%2==0:
    print(a**2)
else:
    a+=1
    print(a)

print('New_vetka')