print("please Enter the first number")
input_1 = input()   #take the first input from the user.
print("please Enter the second number")
input_2 = input()    #take the second input from the user.
print("please Enter the operation")

input_1=float (input_1)   
input_2=float (input_2)
#convert the inputs from string to numbers

print("please determine the type of the operation") 
input_operation = input()  # take the type of the operation from the user 
 
if input_operation=="+": 
    Sum=input_1 + input_2  #this is the syntax of the summation operation.
    print(" the result is:" ,Sum)

elif input_operation=="-": 
    sub=input_1 - input_2   #this is the syntax of the subtraction operation.
    print(" the result is:" ,sub )

elif input_operation=="*":  
    multiply=input_1 * input_2   #this is the syntax of the multipliction operation.
    print(" the result is:" ,multiply )

elif input_operation=="/":   
    division=input_1 / input_2   #this is the syntax of the division operation.
    print(" the result is:" ,division )

elif input_operation=="%":      
    mod=input_1 % input_2        #this is the syntax of the modlus operation
    print(" the result is:" ,mod )

else :
    print("the operation is false")   #print this statement if user enter an false operation. 