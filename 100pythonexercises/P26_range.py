for i in range(11):
    print(i)

def get_acceleration(v1,v2,t1,t2):
    return (v2-v1)/(t2-t1)

print(get_acceleration(0,10,0,20))
