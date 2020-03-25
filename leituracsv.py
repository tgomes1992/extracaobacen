import csv
import os
import shutil
import time


arquivoLeitura = open(r"C:\Users\thiag\Desktop\bacen\csv_import\csv_import.csv",'r')
linhasEntrada = csv.reader(arquivoLeitura)
itens = []

for i in linhasEntrada:
    itens += i


class Arquivo_entrada():
   
    def __init__(self,filename):
        self.file_i = filename
        self.arquivoentrada = open(os.path.join("C:/Users/thiag/Desktop/bacen/Arquivosbacen",self.file_i),'r')
        self.linhas = csv.reader(self.arquivoentrada, delimiter = ",")
    def mostrarlinhas(self):
         for linha in self.linhas:
             print(linha)
    def closeFile(self):
         self.arquivoentrada.close()

class Arquivo_saida(Arquivo_entrada):

    def __init__(self,filename):
        Arquivo_entrada.__init__(self,filename)
        nfile = "Arquivo Atualizado_" + filename[-12:-4]+ ".csv"
        self.file_o = open(os.path.join("C:/Users/thiag/Desktop/bacen/Scripts/CSVS  -  BANCO DE DADOS",nfile),"w")
        self.cabecalho = ["Data", "Codigo" , "Tipo", "Moeda", "Cotacao em Real: Compra","Cotacao em Real: Venda","Paridades:Compra","Paridades:Compra"]
    def novoarquivo(self):
        writer = csv.writer(self.file_o,delimiter=",")
        writer.writerow(self.cabecalho)
        for linha in self.linhas:
            writer.writerow(linha)
        self.file_o.close()
        Arquivo_entrada.closeFile(self)
        
        #print("Novo Arquivo Gerado")



def main():
    for n in itens:
        fileDownload = Arquivo_entrada(n)
        fileDatabase = Arquivo_saida(n)
        fileDatabase.novoarquivo()
        fileDownload.closeFile()
    print("Arquivos Gerados")
    source = "C:/Users/thiag/Desktop/bacen/Arquivosbacen"
    destination = "C:/Users/thiag/Desktop/bacen/importados"
    for files in itens:
        shutil.move(os.path.join(source,files) , destination)
    return("Arquivos Movidos para - " +   destination )



        
    
    












        


        


