import operator

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.floordiv
}
    
def zero(x = 0):
    if x == 0 : return x 
    return ops[x[0]](0,int(x[1]))
def one(x = 1):
    if x == 1 : return x
    return ops[x[0]](1,int(x[1]))
def two(x = 2): 
    if x == 2 : return x
    return ops[x[0]](2,int(x[1]))
def three(x = 3): 
    if x == 3 : return x
    return ops[x[0]](3,int(x[1]))
def four(x = 4): 
    if x == 4 : return x
    return ops[x[0]](4,int(x[1]))
def five(x = 5):
    if x == 5 : return x
    return ops[x[0]](5,int(x[1]))
def six(x = 6): 
    if x == 6 : return x
    return ops[x[0]](6,int(x[1]))
def seven(x = 7):
    if x == 7 : return x
    return ops[x[0]](7,int(x[1]))
def eight(x = 8): 
    if x == 8 : return x
    return ops[x[0]](8,int(x[1]))
def nine(x = 9): 
    if x == 9 : return x
    return ops[x[0]](9,int(x[1]))

def plus(x):
    return str("+" + str(x))
def minus(x): 
    return str("-" + str(x))
def times(x): 
    return str("*" + str(x))
def divided_by(x):
    return str("/" + str(x))
