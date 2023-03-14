def main():
    intInput = int(input("Por favor digite um numero:"))

    numero0, numero1, numero2 = 0, 1, 1
    
    if intInput in set([numero0, numero1, numero2]):
        print("Pertence a sequencia")

    while numero0 < intInput:
        numero0 = numero1 + numero2
        numero2 = numero1
        numero1 = numero0

    if numero0 == intInput:
        print("Pertence a sequencia")
    else:
        print("NÃO Pertence a sequencia")


if __name__ == "__main__":
    main()