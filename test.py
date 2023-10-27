#Nhập và một số nguyên dương n, tiếp theo là n số nguyên dương lần lượt là các phần tử của một dãy số a. Hãy kiểm tra xem dãy a có phải là dãy đơn điệu hay không, trả về "YES" nếu có, "NO" nếu không.
# l=[]
# n=int(input('nhap so phan tu:'))
# for i in range(n):
#     l.append(int(input('nhap phan tu: ')))
# print(l)
# for i in range(0,n):
#     if l[i] == l[i-1]:
#         print(' khong phai day don dieu')
#         break
# def getStr(n):
#     dst=True
#     dsg=True
#     for i in range(1,n):
#         if l[i] <= l[i-1]:
#             dst=False
#         if l[i] >= l[i-1]:
#             dsg=False
#     if (dst or dsg):
#         print('yes')
#     else:
#         print('no')
# getStr(n)



# l = []
# a = []

# n = int(input('Nhập số phần tử danh sách l: '))
# for i in range(n):
#     l.append(int(input('Nhập phần tử: ')))

# m = int(input('Nhập số phần tử danh sách a: '))
# for i in range(m):
#     a.append(int(input('Nhập phần tử: ')))

# def tinhTong1(l):
#     count = 0
#     for i in l:
#         count += i
#     return count

# def tinhTong2(a):
#     count2 = 0
#     for t in a:
#         count2 += t
#     return count2

# tong_l = tinhTong1(l)
# tong_a = tinhTong2(a)

# if tong_l < tong_a:
#     print(f'Tổng của danh sách l ({tong_l}) nhỏ hơn tổng của danh sách a ({tong_a})')
# elif tong_l == tong_a:
#     print(f'Tổng của danh sách l ({tong_l}) bằng tổng của danh sách a ({tong_a})')
# else:
#     print(f'Tổng của danh sách l ({tong_l}) lớn hơn tổng của danh sách a ({tong_a})')


#bai1
# n=int(input(' enter a number: '))
# def getNum(n):
#     if n%2==0:
#         print(n,' is even ')
#     if n%2!=0:
#         print(n,' is odd ')
# getNum(n)

#bai2
# Yêu cầu người dùng nhập vào một số thực. Hãy kiểm tra số thực đó có phải là số nguyên hay không.
# Kết quả mong đợi của chương trình:
# n=float(input(' input number: '))
# import math
# def getNum(n):

#     if math.ceil(n)!=math.floor(n):
#      print(n,' is a real number ')
#     else:
#         print(n,' is a integer number ')

# getNum(n)


#BAI3
#Yêu cầu người dùng nhập vào một ký tự. Hãy kiểm tra ký tự đó có phải là một chữ số hay không.
#Kết quả mong đợi của chương trình:
# n=input(' enter: ')
# print(n.isnumeric())


#bai4
# n=int(input(' enter a number: '))
# def getNum(n):

#     if n%3==0 and n%5==0:
#         print(n, 'is divisible by 3 and 5')
#     if n%3==0 and n%5!=0:
#         print(n, 'is divisible by 3 ')
#     if n%3!=0 and n%5==0:
#         print(n, 'is divisible by 5 ')
#     if n%5!=0 and n%3!=0:
#         print(n, 'is not divisible by 3 or 5 ')
# getNum(n)

#bai5
# Username= 'admin'
# Password= 12345
# print('Welcome to The Ultimate Security System')
# n=input('Username: ')
# p=int(input('Password: '))
# def getUP(n,p):
#     if n==Username and p==Password:
#         print('You are logged in, admin.')
#     else:
#         print('Wrong username or password.')
# getUP(n,p)


# #bai6
# a=float(input(' enter 1st line segment: '))
# b=float(input(' enter 2nd line segment: '))
# c=float(input(' enter 3rd line segment: '))
# def getNum(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         print('The 3 line segments can form a triangle.')
#     else:
#         print('The 3 line segments cannot form a triangle.')
# getNum(a,b,c)

#bai7
#bai8
#Kiểm tra số nguyên tố
# n=int(input('enter a number: '))
# def getPrime(n):

#     if n<=1:
#         print(n,'is not a prime number')
#     if n==2:
#         print(n,'is  a prime number')
#     if n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 print(n,'is not a prime number')
#                 break
#             else:
#                 print(n,'is a prime number')
# getPrime(n)


n=int(input(' enter numbers: '))
l=[]
for i in range(n):
    l.append(input())
print(l)
max=0
def getMax(l):
    for i in l:
        if i>max:
            max=i
            print(max)
getMax(l)