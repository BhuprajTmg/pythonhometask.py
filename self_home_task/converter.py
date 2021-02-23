#converter from nrp to pound or vise versa.

num1=float(input("Enter the value in Nrp. or pound(£):"))
choose1=input("choose It's either neru or pound'£':").lower()
a=1/163.58
if choose1=="neru":
    pound=a*num1
    print("Your amount in pound'£' is",pound)

elif choose1=="pound":
    neru=163.58* num1
    print("Your amount in Nrp. is",neru)
else:
    print("!!!! !!! !! ! Invald input ! !! !!! !!!!")
