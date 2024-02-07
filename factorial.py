## recursion

def factorialNum(numero):
    
    if (numero == 1):
        
        return 1
            #resultado = numero*(numero-1)
    
    else:
        return numero * factorialNum(numero-1)
    
print(factorialNum(5))
print(factorialNum(7))

# iterating 
def factorialDos(myNum):
    resultado = 1
    if (myNum == 0):
        return
    
    else:
        for i in range(1, myNum + 1):
            resultado = resultado * i
            
        return resultado
    
print(factorialDos(5))
print(factorialDos(7))