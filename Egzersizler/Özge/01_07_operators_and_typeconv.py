a = -3
b = -2
print(a and b, a or b, b and a,not a, not b) 

liste = [1,2,3,4]
print(*liste,sep=";")

x = 10        # 1010
y = 4         # 0100
print(x & y)  # 0000  0
print(x | y)  # 1110  14
print(x ^ y)  # 1110  14  #XOR
print(~y)     # 0100 ->  -0100
print(x<<y)   #0100  ->  10000
print(x>>y)   #0100  ->  00001