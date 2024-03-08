def inverter_string(texto):
  texto_invertido = ""
  for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

texto = input("Digite um texto: ")

texto_invertido = inverter_string(texto)

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
