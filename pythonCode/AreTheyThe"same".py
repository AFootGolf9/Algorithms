def comp(array1, array2):
    print(array1)
    print(array2)
    if(array1 is None or array2 is None):
        return False
    for elem in array1:
        if array2.count(elem**2) != array1.count(elem):
            return False
    for elem in array2:
        num = pow(elem, 0.5)
        if array1.count(num) != array2.count(elem) and array1.count(-num) != array2.count(elem):
            print(elem)
            return False
    return True
