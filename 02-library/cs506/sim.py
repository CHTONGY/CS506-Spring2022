def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    # raise NotImplementedError()
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    # raise NotImplementedError()
    length = min(len(x), len(y))
    if length == 0:
        return 0
    intersect_num = 0
    for i in range(length):
        if x[i] == y[i]:
            intersect_num += 1
    
    return 1- (intersect_num / length)

def cosine_sim(x, y):
    # raise NotImplementedError()
    a = x
    b = y
    numerator = dot(a,b)
    denominator = (dot(a,a) **.5) * (dot(b,b) ** .5)
    if denominator == 0:
        return 0
    return  numerator / denominator

def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

# Feel free to add more
