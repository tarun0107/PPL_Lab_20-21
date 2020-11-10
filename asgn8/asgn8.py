#Handling zero division error
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

def divide(x, y): 
    try:  
        result = x // y 
        print(" answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 

divide(x,y)


def raiserror(x):
	if x > 5:
		raise Exception('x should not exceed 5.\n The value of x was: {}'.format(x))


def handlerror(x):
    try:
        raiserror(x)
    except:
        print("You can't enter greater than 5")
        
handlerror(x)