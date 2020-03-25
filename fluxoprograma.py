
import os 
import shutil
import extrairtaxas
import csvimportacao
import leituracsv


#file inside a git repo

def mover_arquivo():
    dir = 'C:/Users/thiag/Downloads'
    destination  = 'C:/Users/thiag/Desktop/bacen/Arquivosbacen'
    file = os.listdir(dir)
    files = []
    for i in file:
        files.append(i)
    for i in files:
        if i[-4:]=='.csv':
            print(i)
            shutil.move(os.path.join(dir,i) , destination)
    return("Arquivos prontos para processamento")





def rodar_programa():
    extrairtaxas.main()
    mover_arquivo()    
    csvimportacao.main()
    leituracsv.main()


if __name__=='__main__':
    rodar_programa()





