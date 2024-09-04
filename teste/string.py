def inverter_string(s):
    resultado = ''
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

entrada_usuario = input("Digite uma string para inverter: ")

string_invertida = inverter_string(entrada_usuario)

print("String:", entrada_usuario)
print("String invertida:", string_invertida)