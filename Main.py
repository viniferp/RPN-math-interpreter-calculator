import math

def operacao(op, a, b) -> float:
    if(op == '+'): return a + b
    if (op == '-'): return a - b
    if (op == '*'): return a * b
    if (op == '/'): return a / b
    if (op == '|'): return math.pow(a, b)
    if (op == '&'): return math.pow(a, 1/2)

def main():
    pilha = []
    #'(((8 2 2 2 /) 1 +) 2 *) = 4'
    expressao = '((3 4 +) (4 2 /) *) '
    vetor_aux = []
    for t in expressao:
        if t != ')':
            if (ord(t) >= 48 and ord(t) <= 57) or t == '+' or t == '-' or t == '*' or t == '/' or t == '|' or t == '&' or t == '(':
                pilha.append(t)
        else:
            operador = pilha[len(pilha) - 1]  # Retiro operador
            pilha.pop()
            for i in reversed(pilha):
                if( i == '('):
                    pilha.pop()
                    break
                vetor_aux.append(i)
                pilha.pop()
            i = len(vetor_aux)
            total = operacao(operador, float(vetor_aux[i-1]), float(vetor_aux[i-2]))
            vetor_aux.pop()
            if(len(vetor_aux) > 1):
                    vetor_aux.pop()
            i = i - 3
            while i >= 0 :
                temp1 = operacao(operador, total,  float(vetor_aux[i]))
                total = temp1
                i -= 1
            vetor_aux = []
            pilha.append(total)
    print("O resultado da expressão:" + expressao + "é "+ str(pilha[0]))


if __name__ == '__main__':
    main()