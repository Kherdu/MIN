import random
import operator
import time

def operacion():
    name = "Rafa"
    global f
    print 'presiona una tecla para iniciar...'
    while raw_input() != "quit":
        op1 = random.randint(1, 99)
        op2 = random.randint(1, 99)

        ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv}
        op = random.choice(list(ops.keys()))
        oper = random.choice(op)

        print '{0} {1} {2}= '.format(op1, oper, op2)
        tiempooperacion = time.time()
        answer = int(ops.get(oper)(op1, op2))
        useranswer = '' # siempre entre en bucle, respuesta nunca vacia
        while answer != useranswer:
            useranswer = int(raw_input())
            if answer == useranswer:
                timer = time.time()-tiempooperacion
                formato_f = '{0};{1};{2};{3};{4} \n'.format(name, op1, oper, op2, timer)
                f.write(formato_f)
                print 'Correcto!'
            else:
                print 'repuesta incorrecta'
        print 'cualquier para continuar, quit para salir'


with open("operaciones2.csv", 'w') as f:
    operacion()
    f.close()
