import MySQLdb as mdb
from SQLManager import SQLManager

class duzz(SQLManager):

      def __init__(self, lista):
            self.conn = None
            self.cursor = None
            self.lista = lista
            try:
                  self.conn = mdb.connect(self.lista[0], self.lista[1], self.lista[2], self.lista[3])
            except:
                  raise Exception("Algo de Errado Não Esta Certo!")
            else:
                  conectado = True
                  self.cursor = self.conn.cursor()

      def colunas(self, table):
            """
            Descobrindo as Colunas da Tabela
            :param nome_da_tabela:
            :return:

            """
            # para criar o comando em mysql
            super().query_columns(table)

            # Recebendo a lista com os nomes das colunas
            result = self.final_com_retorno()

            # Retornando a lista com os nomes das colunas
            return [r[0] for r in result]

    #FUNÇÃO PARA SALVAR DADOS NO BD
            
      def final_sem_retorno(self):
            try:
                  self.cursor.execute(self.query)
            except:
                  raise Exception("Não Foi Possível Salvar Dados no Banco de Dados!")
            else:
                  self.conn.commit()
                  print("Dados Salvos com Sucesso!")

      #FUNÇÃO PARA LER DADOS DO BD

      def final_com_retorno(self):
            try:
                  self.cursor.execute(self.query)
            except:
                  raise Exception("Não Foi Possível Usar Dados do Banco de Dados!")
            else:
                  return self.cursor.fetchall()

      def criar_table(self, dia):
            try:
                  super().create_table(name = dia)
            except:
                  print("NAO FOI POSSIVEL CRIAR A TABELA")
            else:
                  print("Tabela Criada")
            self.final_sem_retorno()
