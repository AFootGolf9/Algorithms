def array_diff(a, b):
    # select all elements in the first array, starting by the last to the first
    for i in range (len(a),0,-1) :
        # verify if the indexed element is equal to an element in b, and remove it
        for element in b :
            if a[i-1] == element :
                a.pop(i-1)
                #used to avoid errors(invalid index) in case the last element of a is present in b
                break
    return a
