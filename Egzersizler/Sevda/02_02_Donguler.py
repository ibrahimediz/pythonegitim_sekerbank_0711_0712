# s=0
# for i in range(0,201):
#     if i %2==0:
#         s=s+i
# print(s)


# print(sum(range(0,201,2)))

# metin=input("metin:")
# sesliharfler="aeiıoöuü"
# print([i for i in metin if i in sesliharfler])
# print(set(i for i in metin if i in sesliharfler))

k=int(input("a:"))
a=0
b=100
while a<b and a<k<b:
  if a<k<int((a+b)/2):
    b=int((a+b)/2)
    print(a,b)
  else:
    a=int((a+b)/2)
    print(a,b)
else : 
  if int(a)==int(k) :
    print(f"sayi {a}")
  else:
    print(f"sayi {b}")