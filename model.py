#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import MySQLdb as mdb
from SQLManager import *
from DUZZ import *
from __login__ import login

class Planejamento():
    def __init__(self):
        pass
        
    def salario(self, valor):
        self.soma_saldo += valor

    def aluguel(self, valor):
        self.soma_saldo -= valor

    def gastos(self, valor):
        self.soma_saldo -= valor

    def poupando_valor(self, valor):
        self.soma_saldo -= valor
        #self.saldo_poupado += valor

    def saldo(self, valores):
        self.salario(valores[0])
        self.aluguel(valores[1])
        self.gastos(valores[2])
        self.poupando_valor(valores[3])
        

    
