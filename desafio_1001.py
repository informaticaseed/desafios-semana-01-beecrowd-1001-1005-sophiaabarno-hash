"""
Beecrowd 1001 - Extremamente Básico

Leia 2 valores inteiros e armazene-os nas variáveis A e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo.
Não apresente mensagem alguma além daquilo que está sendo especificado e
não esqueça de imprimir o fim de linha após o resultado, caso contrário,
você receberá "Presentation Error".
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1001

# Escreva sua solução abaixo

# Lê os dois valores inteiros da entrada
A = int(input())
B = int(input())

# Efetua a soma
X = A + B

# Imprime o resultado no formato exato solicitado: "X = [resultado]"
# O f-string facilita a formatação mantendo o espaço antes e depois do igual
print(f"X = {X}")
