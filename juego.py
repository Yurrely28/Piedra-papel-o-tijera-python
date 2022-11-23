import random

print("PIEDRA PAPEL O TIJERA")

punmaq=0
punuser=0
intentos =0
n=int(input("Cuantas veces desea jugar: "))

while  intentos < n:
    maq = random.randint(1,3)
    print("Seleccione la opcion")
    print("""1. PIEDRA
2. PAPEL
3. TIJERA""")
    us= int(input())
    if us >=1 and us <=3:

        if (maq == 1 and us== 2) or (maq==2 and us== 3) or (maq==3 and us== 1):
            punuser +=1
            print("Ganaste")
        elif (maq == 1 and us == 3) or (maq== 2 and us== 1) or (maq== 3 and us== 2):
            punmaq +=1
            print("Perdiste") 
        elif maq == us:
            print("Empate")
            punmaq = punmaq
            punuser = punuser
    else:
        print("Digito una opcion incorrecta")
    intentos+=1

print(f"puntos Maquina {punmaq}")
print(f"puntos usuario {punuser}")