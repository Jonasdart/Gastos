#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import MySQLdb as mdb
from pynput import keyboard
from datetime import datetime
from time import sleep

class Interacao_usuario():
    def __init__(self):
        self.cred = list()

    def data(self):
        data = datetime.now()
        return [data.strftime('%Y'), data.strftime('%m'), data.strftime('%d')]
    def credencia(self):
        data = datetime.now()
        self.cred.append("localhost")
        self.cred.append(input("Informe o Usuario: "))
        self.cred.append(input("Informe a Senha: "))
        self.cred.append(f"{self.data()[0]}")
        print(self.cred)
        return self.cred

    def inicio(self):
        self.valores = list()
        self.carregamento(2)
        print("Bem Vindo à Interface de Atualização Dos Valores!")
            
        return self.solicita_valores()

    def carregamento(self, segundos = 3):
        sleep(0.5)
        print(".", end="")
        if segundos is not 0:
            self.carregamento(segundos-1)
        else:
            print("\n\n")

    def fim(self, saldo):
        print(f"Saldo Final: R${saldo}")

    def solicita_valores(self):
        #implementar aqui o menu interativo para escolher o mês
        print(f"\n\n\t\tValores Referentes ao Mês {self.data()[1]}\n\n")
        self.salario()
        self.aluguel()
        self.gastos()
        self.poupando_valor()
        return self.valores

    def salario(self):
        try:
            self.valores.append(float(input(f"Salario Recebido: ")))
        except:
            print("Valor Inválido! Tente Novamente")
            self.salario()
        else:
            pass

    def aluguel(self):
        try:
            self.valores.append(float(input(f"Valor Aluguel: ")))
        except:
            print("Valor Inválido! Tente Novamente")
            self.aluguel()
        else:
            pass

    def gastos(self):
        try:
            self.valores.append(float(input(f"Ademais Gastos: ")))
        except:
            print("Valor Inválido! Tente Novamente")
            self.gastos()
        else:            
            pass

    def poupando_valor(self):
        try:
            self.valores.append(float(input(f"Valor Poupado: ")))
        except:
            print("Valor Inválido! Tente Novamente")
            self.poupando_valor()
        else:
            pass
        
    

