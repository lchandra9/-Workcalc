'''
Created on Sep 24, 2021

@author: LChandra25
'''

def main():    
    name = input("What is your name")
    if name == 'luke':
        print("That is a cool name")
    else:
        print("Thats a dumb name")


    hours  = input("enter hours")
    dollars5 = input("enter dollers")
    pay = int(hours)*int(dollars5)
    
    
    print("pay is ", str(pay))


#4.1 the answer is: float
#4.2 the answer is: integer
#4.3 the answer is: integer
#4.4 the answer is: 11

    celsius = input("enter celsius")
    
    celsius = float(celsius)
    
    output= (celsius*9/5)+32
    
    
    print(output)



if __name__ == '__main__':
    main()
