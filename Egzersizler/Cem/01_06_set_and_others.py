
while True:
    try:
        number = int(input("Plese enter a number: "))
        print("basarili",number)
        break
    except ValueError:
        print("Please enter a valid integer")