"""
Este módulo é uma projeto de aprendizado, no qual desenvolvemos uma calculadora basica com
quatro operações.

This module is a learning project, in which we developed a basic calculator with
four operations.

autor/author lucas jesus de moura
lucas.j.m@outlook.com 
versão/version: 0.0.3
 
"""
'''
#Biblioteca de parâmetros e funções específicos do sistema
'''
import sys
 '''
Função que recebe os valores e os converte para float

Library of system-specific parameters and functions
'''
def validar_valor(valor):
	valor = valor
	try:
		valor_convertido= float(valor)
		return valor_convertido
	except ValueError:
		return False
 
'''
Funções que recebe os valores e chama a função de calculo correspondente ao operador.

Functions that receive the values ​​and call the calculation function corresponding to the operator.
'''
def valida_operador(operador,primeiro_valor_float,segundo_valor_float):
	operadores = {"+":adicao,"-":subtracao,"*":multiplicacao,"/":divisao}
	try:
		print(operadores[operador](primeiro_valor_float,segundo_valor_float))
	except KeyError:
		return False
 
'''
Funções para efetuar os calculos juntamente com a função para finalizar ou continuar o programa.

Functions to perform calculations together with the function to end or continue the program.
'''
def adicao(valor1, valor2):
	return valor1 + valor2
	
def subtracao(valor1, valor2):
	return valor1 - valor2
	
def multiplicacao(valor1, valor2):
	return valor1 * valor2
	
def divisao(valor1, valor2):
	try:
		return valor1 / valor2
	except ZeroDivisionError:
		return "ops nao dividimos por zero"
	
'''
Função que valida os valores de entrada
em forma de split e chama para os a validadores.

Function that validates the input values
in the form of split and flame for the validators.
'''
def validar_entradas():
	print("Para começarmoa digite os valores a ser calculado,\
    juntamente com o operador desejado como mostra o exemplo abaixo:\n ""45 + 89""")
    #while que valida os valores juntamente com o operador
	x = True
	while x == True:
		try:
			primeira_entrada,entrada_operador,segunda_entrada=input("").split()
			x = False
		except ValueError:
			print("Ops, se atente ao espaço entre os valores e o operador")
 
    #chamada das funções que valida os valores e os retorna convertidos
	primeira_entrada = validar_valor(primeira_entrada)
	segunda_entrada = validar_valor (segunda_entrada)
	entrada_operador = valida_operador(entrada_operador,primeira_entrada,segunda_entrada)
	
    #laço que valida os valores individualmente caso, haja algum errado
	while primeira_entrada == False or entrada_operador == False or segunda_entrada == False:
		if primeira_entrada == False:
			primeira_entrada=input("Ops acho que você digitou o primeiro valor errado ")
			primeira_entrada = validar_valor(primeira_entrada)
		elif segunda_entrada == False:
			segunda_entrada = input("Ops acho que você digitou o segundo valor errado ")
			segunda_entrada = validar_valor(segunda_entrada)
		elif entrada_operador == False:
			entrada_operador = input("Ops acho que você digitou o operador valor errado ")
			entrada_operador = valida_operador(entrada_operador,primeira_entrada,segunda_entrada)
 
'''
Função que valida que inicia o programa em forma de loop até que o usario deseje sair.

Validating function that starts the program in a loop until the user wants to exit.
'''
def main():
    print("Olá, bem vindo a calcular, se trata de um\n projeto de aprendizado\
		onde desenvolvemos uma calculadora que realiza quatro operações básicas:\
        Multiplicação, Divisão, Adição e subtração.Vamos nessa? \n(""S"" para SIM\
		""N"" para Não)")
    #Função que os primeiros valores
    prime_vez = 0
    while True:
    	if prime_vez == 1:
    		print("quer calcular de novo?")
    	prime_vez = 1
    	x = True
    	while x == True:
    		calculo_de_novo= input("")
    		if calculo_de_novo.upper() == 'S':
    			print("Então vamos lá")
    			x = False
    			validar_entradas()	
    		elif calculo_de_novo.upper() == 'N':
    			print('Tudo bem até a proxima!')
    			return sys.exit()
    		else:
    			print("Opa só aceitamos ""N"" ou ""S""")
    	    				
if __name__ == '__main__':
    main()