def prime_numbers_generator():
    divisores = 0
    prime_numbers = []

    for number in range (1,1000):
        for divisor in range(1,1000):
            if number % divisor == 0:
                divisores += 1
        if divisores <= 2:
            #print("Numero primo: ",number)
            prime_numbers.append(number)
        divisores = 0  
    return prime_numbers  

def main():
    prime_numbers_generator()
    for number in prime_numbers_generator():
        print("Numero primo: ", number)

main()