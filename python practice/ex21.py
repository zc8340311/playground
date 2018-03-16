def add(a,b):
    print "adding %d+%d" %(a,b)
    return a+b

def substract(a,b):
    print "substracting %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "multiplying %d*%d" %(a,b)
    return a*b
def divide(a,b):
    print "deviding %d / %d" % (a,b)
    return a/b

print "let's do some math with just functions!"

age=add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq =divide(100,2)

print "here is a puzzle."

what=add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:", what, "can you do it by hand?"
