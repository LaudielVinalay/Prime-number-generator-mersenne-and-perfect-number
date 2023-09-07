def main():
    numeros_primos = tuple([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])    
    for numero in numeros_primos:
        merssenne_number = (2**numero)-1

        if merssenne_number in numeros_primos:
            print(merssenne_number)
main()