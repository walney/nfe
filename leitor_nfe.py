from bs4 import BeautifulSoup as bs

with open("nfe.xml","r") as arquivo:
    soup = bs(arquivo,"xml")
    
#for prod in soup.find_all('cProd'):
#    print(prod.text)
    
print("-----LEITOR DA NFE em Python---")
print("")
print("")

#print(soup.find_all('dest'))

ide = soup.find_all('ide')

print("-----IDE-----------------------------------")
for data in ide: 
    #print(data.get_text())
    print(data.cUF.text)                                                                                                                                                                                                                                                 
    print(data.cNF.text)                                                                                                                                                                                                                                           
    print(data.natOp.text)                                                                                                                                                                                                                                          
    print(data.mod.text)                                                                                                                                                                                                                                                 
    print(data.serie.text)                                                                                                                                                                                                                                              
    print(data.nNF.text)                                                                                                                                                                                                                                          
    print(data.dhEmi.text)                                                                                                                                                                                                                      
    print(data.dhSaiEnt.text)                                                                                                                                                                                                                
    print(data.tpNF.text)                                                                                                                                                                                                                                                
    print(data.idDest.text)                                                                                                                                                                                                                                            
    print(data.cMunFG.text)                                                                                                                                                                                                                                      
    print(data.tpImp.text)                                                                                                                                                                                                                                             
    print(data.tpEmis.text)                                                                                                                                                                                                                                           
    print(data.cDV.text)                                                                                                                                                                                                                                                 
    print(data.tpAmb.text)                                                                                                                                                                                                                                             
    print(data.finNFe.text)                                                                                                                                                                                                                                           
    print(data.indFinal.text)                                                                                                                                                                                                                                       
    print(data.indPres.text)                                                                                                                                                                                                                                         
    print(data.procEmi.text)                                                                                                                                                                                                                                         
    print(data.verProc.text)


print("----Emitente-------------------------------")

emitente = soup.find_all('emit')

for data in emitente: 
    #print(data.get_text())
    print(data.CNPJ.text)
    print(data.xNome.text)
    print(data.xFant.text)
    print(data.xLgr.text)
    print(data.nro.text)
    print(data.xCpl.text)
    print(data.xBairro.text)
    print(data.cMun.text)
    print(data.xMun.text)
    print(data.UF.text)
    print(data.CEP.text)
    print(data.cPais.text)
    print(data.xPais.text)
    print(data.fone.text)
    print(data.IE.text)
    print(data.CRT.text)

print("----Cliente------------------------------------")

cliente = soup.find_all('dest')

for data in cliente: 
    #print(data.get_text())
    print(data.xNome.text)
    print(data.xLgr.text)
    print(data.nro.text)
    print(data.xCpl.text)
    print(data.xBairro.text)
    print(data.cMun.text)
    print(data.xMun.text)
    print(data.UF.text)
    print(data.CEP.text)
    print(data.cPais.text)
    print(data.xPais.text)
    print(data.fone.text)
    print(data.indIEDest.text)
    print(data.IE.text)
    print(data.email.text)

print("----Produtos---------------------------------")

produtos = soup.find_all('prod')

for data in produtos: 
    #print(data.get_text())
    print("Produto: "+data.cProd.text+ " - "+data.xProd.text)
    print(data.cEAN.text)                                                                                                                                                                                                                                                
    print(data.NCM.text)
    print(data.CFOP.text)
    print(data.uCom.text)
    print(data.qCom.text)
    print(data.vUnCom.text)
    print(data.vProd.text)
    print(data.cEANTrib.text)
    print(data.uTrib.text)
    print(data.qTrib.text)
    print(data.vUnTrib.text)
    print(data.vFrete.text)
    print(data.vDesc.text)
    print(data.indTot.text)
    print("-------------------------")

print("---------------------------------------------------")


