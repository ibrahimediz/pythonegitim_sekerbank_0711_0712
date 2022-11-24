metin = "Şekerbank"
metinIter = iter(metin)
print(next(metinIter))

sozluk = {"1":"a","2":"b"}
print(isinstance(sozluk, dict))
print(isinstance(sozluk, tuple))

distance = int(input())
time = int(input())
velocity = int(input())
fuel = int(input())
fuel_consumption = int(input())


if velocity * time < distance:
        print("Failure, Not enough time")
if fuel * fuel_consumption < distance:
        print("Failure, Not enough fuel")
if velocity * time < distance and fuel * fuel_consumption < distance:
        print("Failure, Not enough time")
else:
        print("Welcome to Mars")
