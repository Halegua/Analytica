#Calculador de ângulo entre ponteiros de um relógio.

def test(inp):
    """ Testa se um input é válido """
    try:
        horas = int(inp[:2])
        minutos = int(inp[-2:])
    except:
        return 0
    if horas >= 24 or minutos >= 60:
        return 0        
    else:
        if horas > 12:
            horas -= 12
#Formata a hora caso esteja no sistema de 24 horas.
        return horas, minutos
        

def calculador():
    horas, minutos = test(inp)

    angle_min = 6 * minutos
    angle_hora = 30 * horas + 0.5 * minutos
    angulo = abs(angle_min - angle_hora)

    if angulo >= 180:
        angulo = 360 - angulo
    print("O menor ângulo é de", str(angulo) + "°")

# Lógica:
# O ponteiro minutos move 6 graus por minuto
# O ponteiro hora move 30 graus a cada hora, e meio grau por minuto adicional.
# A diferença do ângulo é o ângulo entre os dois ponteiros.
    
while True:
    inp = input("Digite a hora: ")
    if inp == 'f':
        print("Fim...")
        break
    else:
        if test(inp) == 0:
            print("Input Inválido")
        else:
            calculador()
        


