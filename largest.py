a=int(input("Enter the first number: "));
b=int(input("Enter the second number: "));
c=int(input("Enter the Third number: "));

def largest():
    if(a>b):
        if(a>c):
             largest=a
        else:
             largest=c
    else:
        if b>c:
            largest=b
        else:
            largest=c
         
        print(largest);
largest();
