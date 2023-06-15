import math

def operation(op, a, b) -> float:
    if(op == '+'): return a + b
    if (op == '-'): return a - b
    if (op == '*'): return a * b
    if (op == '/'): return a / b
    if (op == '|'): return math.pow(a, b)
    if (op == '&'): return math.pow(a, 1/2)

def main(exp):
    stack = []
    #'(((8 2 2 2 /) 1 +) 2 *) = 4'
    expressao = exp
    vetor_aux = []
    for t in expressao:
        if t != ')':
            if (ord(t) >= 48 and ord(t) <= 57) or t == '+' or t == '-' or t == '*' or t == '/' or t == '|' or t == '&' or t == '(':
                stack.append(t)
        else:
            operador = stack[len(stack) - 1]  # Removes operator
            stack.pop()
            for i in reversed(stack):
                if( i == '('):
                    stack.pop()
                    break
                vetor_aux.append(i)
                stack.pop()
            i = len(vetor_aux)
            total = operation(operador, float(vetor_aux[i-1]), float(vetor_aux[i-2]))
            vetor_aux.pop()
            if(len(vetor_aux) > 1):
                    vetor_aux.pop()
            i = i - 3
            while i >= 0 :
                temp1 = operation(operador, total,  float(vetor_aux[i]))
                total = temp1
                i -= 1
            vetor_aux = []
            stack.append(total)
    print("The result of the expression: " + expressao + " is "+ str(stack[0]))


if __name__ == '__main__':
    #eg. ((3 + 2) * (4 / 1)) = 20
    main('((3 2 +) (4 1 /) *)')
