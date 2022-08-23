# A bad example of Python code
def RUN(): #This is the part that does things    
    x1= input() #These lines save the input
    y1= input()
    x2= input()
    y2= input()
    x3= input()
    y3= input()
    if((x1>x2) or (y1<y2)): #This part checks if the rectangle is well-defined
      print("error")
    elif(((x3>=x1) and (x3<=x2)) and ((y3<=y1) and (y3>=y2))): #This checks if the point is in the rectangle
       print("inside")
       
    else :
      print("outside") #If the point is not in the rectangle it is outside of the rectangle

run()