def es_primo(numero):
    divisores = 0
   
    for i in range(1,1000):
        
        if (numero % i) == 0:
            divisores += 1
            
    if divisores == 2:
        return True
    
    return False
    

def main():
    number = int(input("Ingrese un numero: "))
    prime_number = es_primo(number)

    if prime_number == True:
        print("El numero ", number, "es primo")
    else:
        print("El numero ", number, "no es primo")

main()