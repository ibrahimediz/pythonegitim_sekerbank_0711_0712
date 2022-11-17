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
i=0
y=100
while i<y:
  if k<(y/2):
    y=int((y+1)/2)
    print(y)
  else:
    i=int((y+1)/2)
    print(i)