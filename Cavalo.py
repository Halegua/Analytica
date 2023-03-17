h = ["A", "B", "C", "D", "E", "F", "G", "H"]

def test(n):
    ini_h,ini_v,fim_h, fim_v = n[0], n[1], n[3], n[4]

    ini_h, fim_h = str.upper(ini_h), str.upper(fim_h)
    x_ini_h, x_fim_h = h.index(ini_h), h.index(fim_h)

    checker_h = abs(x_ini_h - x_fim_h)
    checker_v = abs(int(ini_v)-int(fim_v))

    if checker_h not in [1,2]:
        print("Inválido.")
    elif checker_v not in [1,2]:
        print("Inválido.")
    elif checker_h == checker_v:
        print("Inválido.")
    else:  
        print("Válido")
    #print(ini_h, ini_v, fim_h, fim_v)

def checker(n):
    # Testa se os inputs de fato são casas de xadrez válidas.
    if len(inp) !=5:
        return False
    else:
        ini_h,ini_v,fim_h, fim_v = n[0], n[1], n[3], n[4]
        ini_h, fim_h = str.upper(ini_h), str.upper(fim_h)
    if str.upper(ini_h) not in h or str.upper(fim_h) not in h:
        return False
    elif int(ini_v) not in range(1,9) and int(fim_v) not in range(1,9):
        return False
    else:
        return True

while True:
    inp = input("Digite a casa inicial e final do cavalo: ")
    if inp == 'f':
        print("Fim...")
        break
    if checker(inp):
        test(inp)
    else:
        print("Inválido")

