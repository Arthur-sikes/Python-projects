def gen(r):
    color = [] 
    i = 255
    for col in range(r):
        cols= (i,i,i)
        color.append(cols)
        i -= 1
    return color
    
c=gen(150)
print(c)