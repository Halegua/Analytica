l = []
while True:
    imp = input("Digite um número qualquer: ")

    try:
        float(imp)
        l.append(imp)
    except:
        None
    if imp == "f":
        print("\n")
        n = list(set(l))
        n.sort()
        for i in n:
            if l.count(i) > 1:
                print("O número",i,"apareceu",str(l.count(i)), "vezes")
            else:
                print("O número",i,"apareceu 1 vez")
        print("Fim...")
        break
    
