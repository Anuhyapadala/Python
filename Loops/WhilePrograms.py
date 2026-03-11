# print * instead of vowels in a string
# str='python programming'
# i=0
# vowels='aeiouAEIOU'
# while i<len(str):
#     if str[i] in vowels:
#         print('*',end='')
#     else:
#         print(str[i],end='')
#     i+=1



# print each and every digit in a number

# num=1234
# while num>0:
#     res=num%10
#     num=num//10
#     print(res)
# print reverse of a number


# num1=121
# res=0
# while num1>0:
#     rem=num1%10
#     res=res*10+rem
#     num1=num1//10
# print(res)

#check whether a number is palindrom or not

# num2=121
# number=num2
# res=0
# while num2>0:
#     rem=num2%10
#     res=res*10+rem
#     num2=num2//10
# if number==res:
#     print(number,'is a palindrome')
# else:
#     print(number,'is not a palindrome')




# print factors of a number
# a=12
# i=1
# while i<=a:
#     if a%i==0:
#        print(i)
#     i+=1

# print count of factors of a number

# a=12
# i=1
# count=0
# while i<=a:
#     if a%i==0:
#        count+=1
#     i+=1
# print(count)

# check whether a number is prime or not
# a=3
# i=1
# count=0
# while i<=a:
#     if a%i==0:
#        count+=1
#     i+=1
# if count==2:
#     print(a,'is a prime number')
# else:
#     print(a,'is not a prime number')


# print all prime numbers between 1 and 100

i=1
while i<101:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,'is a prime number')
    i+=1
# print reverse of a string

# str1='Anuhya'
# string=str1[::-1]
# print(string)

# str1='Anuhya'
# i=len(str1)-1
# while i>=0:
#     print(str1[i],end='')
#     i-=1
        
# check whether a string is palindrome or not withou using slicing
str2='malayalam'
i=0
j=len(str2)-1
is_palindrome=True
while i<j:
    if str2[i]!=str2[j]:
        is_palindrome=False
        break
    i+=1
    j-=1
if is_palindrome:
    print(str2,'is a palindrome')
else:
    print(str2,'is not a palindrome')
