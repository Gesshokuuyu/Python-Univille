def chop(l):
    del l[0]
    del l[-1]

l = [1,2,3,4]
chop(l)
print(l)