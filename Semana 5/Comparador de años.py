# RETO DE LA SEMANA 5
# Diferenciador de Años

añoUno = int(input("Ingrese de favor el año actual: "))
añoDos = int(input("Ingrese de favor otro año para comparar: "))
comparacion = añoUno - añoDos

if comparacion == 1:
        print(f"A partir del año {añoDos} ha transcurrido 1 año.")
elif comparacion > 1:
        print(f"A partir del año {añoDos} han transcurrido {comparacion} años.")
elif comparacion == -1:
        print(f"Para que sea el año {añoDos} falta 1 año.")
elif comparacion < -1:
        print(f"Para que sea el año {añoDos} faltan {-comparacion} años.")
else:
        print("¡Repetió el mismo año!...XD")



