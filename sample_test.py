def hifi(nodes):
    s=[]
    for i in range(len(nodes)-1):
        print(nodes[i])
        s+=[(nodes[i],nodes[i+1])]
    s+=[(nodes[len(nodes)-1],nodes[0])]
    return s
print(hifi([1,2,3]))
