import json
import os

def calcular_faturamento(dados_faturamento):
    faturamentos = [valor for valor in dados_faturamento if valor > 0]
    
    menor_faturamento = min(dados_faturamento)
    maior_faturamento = max(dados_faturamento)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media_mensal)
    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    nome_arquivo = 'faturamento.json'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados_json = json.load(arquivo)
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return
    
    try:
        dados_faturamento = dados_json['faturamento']
    except KeyError:
        print("O JSON deve conter a chave 'faturamento'.")
        return

    try:
        menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados_faturamento)
        print(f"Menor valor de faturamento: {menor_faturamento}")
        print(f"Maior valor de faturamento: {maior_faturamento}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
