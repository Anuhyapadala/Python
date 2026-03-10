CGPA=float(input("Enter your CGPA: "))
fee=80000
if CGPA>=9:
    totalfee=fee-(fee*0.3)
    print("Your discounted fee is: ",totalfee)
elif CGPA>=8 and CGPA<9:
    totalfee=fee-(fee*0.2)
    print("your discounted fee is:",totalfee)
elif CGPA>=7.5 and CGPA<8:
    totalfee=fee-(fee*0.1)
    print("your discounted fee is:",totalfee)
else:
    print("No discount,you have to pay ",fee)