p = float(input("enter the principal amount\n"));
r = float(input("enter the intrest\n"));
n = float(input("enter the no.of years\n"));
j = (1+r/100)**n
a = p*j
c = a - p
print("the compont intrest is",c);
print("the amount is",a);