import random
n=random.randint(1,100)
for i in range(5):
    g=int(input("enter guess number:"))
    if g<n-10:
        print("you entered lessthan number")
    elif (g>=n-10 and g<n):
        print("you entered closer lessthan")
    elif g>n+10:
        print("you entered greatest number")
    elif (g<=n+10 and g>n):
        print("you entered closer greater value")
    elif g==n:
        print("you win")
        break
else:
    print("you lose")

print("system takes",n)