notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

while True:
    imp = input("Digite o valor a ser decomposto: ")
    try:
        valor = round(float(imp),2)
        if valor <= 0:
            print("Digite um valor maior que zero.")
            break
    except:
        print("Input Inválido.")
        break

    valor_int = int(valor)
    
    i = 0
    #Cálculo de Notas:
    print("\nNOTAS: \n")
    while valor_int > 1:
        n = int(valor_int / notas[i])
        if n != 0:
            print(str(n) + " nota(s) de " + "R$" + str(notas[i]) + ".00")
            valor_int = valor_int % notas[i]
        i += 1
    valor_moeda = round(valor - int(valor) + valor_int, 2)
    print("\nMOEDAS: \n")

    #Cálculo de Moedas
    i = 0
    while valor_moeda >= 0.01:
        try:
            n = int(valor_moeda / moedas[i])
            if n!= 0:       
                print(str(n) + " moedas de " + "R$" + format(moedas[i], ".2f"))
                valor_moeda = round(valor_moeda % moedas[i], 2)           
            i += 1
        except:
            break
    break
        
        
            
        
