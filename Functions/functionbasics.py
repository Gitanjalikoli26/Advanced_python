# print the statement
print("Welcome to the Python class")

for i in range(1,25):
    print(f"the line is {i}")
    
def add(x,y):
    addition=x+y
    
    return addition

print(f'Addition is {add(20,30)}')


def simple_interst(p,r,t):
    si=(p*r*t)/100
    
    return si

print(f'simple interst is {simple_interst(5400,10,2)}')