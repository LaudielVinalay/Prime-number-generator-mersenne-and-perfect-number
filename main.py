def prime_numbers_generator():
    divisores = 0
    prime_numbers_list = []
    
    for number in range (1,1000):
        for divisor in range(1,1000):
            if number % divisor == 0:
                divisores += 1
        if divisores <= 2:
            prime_numbers_list.append(number)
        divisores = 0
    
    return prime_numbers_list    

def es_primo(numero):
    divisores = 0
   
    for i in range(1,1000):
        
        if (numero % i) == 0:
            divisores += 1
            
    if divisores == 2:
        return True
    
    return False

def es_numero_perfecto(numero):
    suma_divisores = []

    for i in range(1,100000):
        
        if numero % i == 0:
            suma_divisores.append(i)
            if i == numero:
                suma_divisores.pop()
    
    if sum(suma_divisores) == numero:
        return True
    
    return False

def main():
        for numero in prime_numbers_generator():
            mersenne_number = (2**numero) - 1
        
            if mersenne_number in prime_numbers_generator():
                print("\nNumero de mersenne: ", mersenne_number)
        
                prime_number= es_primo(numero)
        
            if prime_number == True:
                print("\nNumero primo: ", numero)
            
            perfect_number = (2**(numero-1))*(mersenne_number)
            
            comprobation_perfect_number = es_numero_perfecto(perfect_number)
            
            if comprobation_perfect_number == True:
                print("\nNumero perfecto: ", perfect_number)

main()
