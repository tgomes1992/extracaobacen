import os
import csv




def main():
    path = r"C:\Users\thiag\Desktop\bacen\Arquivosbacen"
    files = os.listdir(path)
    csv_file = []
    for file in files:
        csv_file.append(file)
        csv_importacao = open(r"C:\Users\thiag\Desktop\bacen\csv_import\csv_import.csv","w")
        writer = csv.writer(csv_importacao)
        writer.writerow(csv_file)
    print("Arquivo Gerado")




                    
                    
                
    



        
