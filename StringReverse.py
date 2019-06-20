def reverse(s):
  str = ""
  for i in s:
   # print(i)
    str = i+" "+ str
    #print(str)
  return str

print("Hello World")
fval = input("Enter your fname: ")
lval = input("Enter your fname: ")

print("----------------------------------------")
print("reverse " + reverse(fval+lval))
