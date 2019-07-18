#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import MySQLdb as mdb
from model import Planejamento
from view import Interacao_usuario
from __login__ import login

class Controla_planejamento():
    def __init__(self):
        self.status = bool
        self.view = Interacao_usuario()
        self.model = Planejamento()
        self.controle = login()

    def login(self, cred):
        try:
            self.conn = self.controle.faz_login(cred)
        except:
            raise
        else:
            return True

    def inicio(self):
        if not self.status:
            try:
                self.cred = self.view.credencia()
                self.status = self.login(self.cred)
                
            except:
                self.cred.clear()
                self.inicio()
            else:
                valores = self.view.inicio()
                self.solicitar_valores(valores)
        else:
            valores = self.view.inicio()
            self.solicitar_valores(valores)

    def solicitar_valores(self, valores):
        try:
            self.model.saldo(valores)
        except:
            print("\n!!Algo Deu Errado!!\n\n")
            self.solicitar_valores(valores)
        else:
            saldo = self.model.soma_saldo
            self.view.fim(saldo)

if __name__ == "__main__":
    main = Controla_planejamento()
    main.status = False
    main.model.soma_saldo = 0.0
    main.inicio()
    

    
