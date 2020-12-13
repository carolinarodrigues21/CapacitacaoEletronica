# -*- coding: utf-8 -*-  

import numpy as np    #biblioteca importada 

#soma
def soma(a,b):
  """
  Função para realizar uma soma
  -------
  Input
  a = float, primeiro numero
  b = float, segundo numero
  ------
  Output
  a + b
  """
  return a + b

#subtração
def subtracao(a,b):
  """
  Função para realizar uma subtração
  -------
  Input
  a = float, primeiro numero
  b = float, segundo numero
  ------
  Output
  a - b
  """
  return a - b
  
  #multiplicação
  def multiplicacao(a,b):
  """
  Função para realizar uma multiplicação
  -------
  Input
  a = float, primeiro numero
  b = float, segundo numero
  ------
  Output
  a*b
  """
  return a*b
  
  #divisão
  def divisao(a,b):
  """
  Função para realizar uma divisão
  -------
  Input
  a = float, numerador
  b = float, denominador
  ------
  Output
  a/b
  """
  if b == 0:   
    print("não é possível calcular essa divisão")
  else:
    r = a/b
  return r

#potenciação
def potencia(a,b):
  """
  Função que eleva um número a uma potencia desejada
  -------
  Input
  a = float, base
  b = float, potência
  ------
  Output
  a**b
  """
  return a**b

#raiz
def raiz_quadrada(x):
  """
  Função que calcula a raiz quadrada de x
  -------
  Input
  x = float
  ------
  Output
  sqrt(x)
  """
  if x<0:
    print("não é possível achar a raiz real de um número negativo")
  return np.sqrt(x)
  
#seno
def seno(x):
  """
  Função que calcula o seno do angulo x em graus
  -------
  Input
  x = float
  ------
  Output
  seno(x)
  """
  s = np.radians(x) #converte o número para radianos para poder fazer o cálculo com a função da biblioteca
  return np.sin(s)
  
  #cosseno
  def cosseno(x):
  """
  Função que calcula o cosseno do angulo x em graus
  -------
  Input
  x = float
  -------
  Output
  cos(x)
  """
  c = np.radians(x)
  return np.cos(c)

#tangente
def tangente(x):
  """
  Função que calcula a tangente do angulo x em graus
  -------
  Input
  x = float
  -------
  Output
  tan(x)
  """
  t = np.radians(x)
  return np.tan(t)
  
#fatorial
def fatorial(x):
  """
  Função que calcula o fatoria de x
  -------
  Input
  x = float
  -------
  Output
  x!
  """
  fat=1
  contador=1

  while contador <= x:
      fat *= contador    #começa no 1 e multiplica por 2,3,... até chegar ao numero desejado, gerando seu fatorial
      contador += 1
  return resultado
