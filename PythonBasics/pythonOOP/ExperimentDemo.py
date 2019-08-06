

def DivUpdate(func):
      def Inner(a,b):
        if type(a) and type(b)=='str':
            print("Unable to compute")
            a=int(a)
            b=int(b)
        else:
            return func(a,b)
      return Inner

@DivUpdate
def Div(x,y):
    x= input("Enter a number:")
    y=input("enter another number:")
    print("Sum,",x+y)
    return x+y

Div(int,int)
#print(Div(x,y))       
#print(Div(12,1))
#print(Div(2,2))
#print(Div(2,0))  #Zero Division Error
