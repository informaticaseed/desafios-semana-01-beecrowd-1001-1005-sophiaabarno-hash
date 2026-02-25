"""
Beecrowd 1003 - Soma Simples

Leia dois valores inteiros, no caso para variáveis A e B.
A seguir, calcule a soma entre elas e atribua à variável SOMA.
A seguir escrever o valor desta variável.

Entrada: O arquivo de entrada contém 2 valores inteiros.

Saída: Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço
em branco antes e depois da igualdade seguido pelo valor correspondente à soma
de A e B.
"""

# Link do problema: https://judge.beecrowd.com/pt/problems/view/1003

# Escreva sua solução abaixo
# Lê os dois valores inteiros
A = int(input())
B = int(input())

# Realiza a soma e armazena na variável solicitada
SOMA = A + B

# Exibe o resultado respeitando os espaços e letras maiúsculas
print(f"SOMA = {SOMA}")
