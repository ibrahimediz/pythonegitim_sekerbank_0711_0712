tcid = input("TC GİRİNİZ")
def tcid(value):
    value = str(value)
    if len(value) != 11:
        return False
    if value.isdigit():
        return True
    if int(value[0]) == 0:
        return False
    return True