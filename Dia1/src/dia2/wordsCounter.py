texto = input("Introduce un texto para hacer el analsis: ")
texto = texto.lower()
letras = []

# Input de las letras que se quieren contar
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
print("\n")

# Contamos las letras que se ingresaron
print("Cantidad de Letras:")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

# Imprimimos las cantidades para el usuario
print(f"Se a encontrado la letra {letras[0]}, {cantidad_letras1} veces")
print(f"Se a encontrado la letra {letras[1]}, {cantidad_letras2} veces")
print(f"Se a encontrado la letra {letras[2]}, {cantidad_letras3} veces")
print("\n")

# Contamos la cantidad de palabras y lo imprimimos para el usuario
texto_list = texto.split()
cantidad_palabras = len(texto_list)
print(f"El texto tiene {cantidad_palabras} palabras")
print("\n")

# Encontramos he imprimimos la primera y ultima letra
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es {primera_letra}")
print(f"La ultima letra del texto es {ultima_letra}")

