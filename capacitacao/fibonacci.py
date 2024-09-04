def fibonacci(n):
    if n < 0:
        return False
    def quadrado_perfeito(x):
        s = int(x**0.5)
        return s * s == x
    return quadrado_perfeito(5 * n * n + 4) or quadrado_perfeito(5 * n * n - 4)

def main():
    try:
        num = int(input("Digite um número: "))
        
        if fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
