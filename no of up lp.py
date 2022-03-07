string =str(input("enter the string\n"));
count = 0
c=0
for i in string:

  if(i.islower()):
   count = count+1


  if (i.isupper()):
      c = c+1

print("the number of uppercase is",c)
print("the no of lowercase is",count)



