
#Forma base de se trabahar com acesso a esse tipo de estrutura apresentada
emails = {
    "caio": ["caiogmail.com", "caio222@gmail.com", ["caioTerceiro"]],
    "marcelo": "marcelo@gmail.com.com"
}
#print(emails["caio"][2][0])

list = ["ipad", "computador", "samsung Galaxy", "BYD"]
 
#Passar uma lista para um dicionário, onde cada indice da lista é uma chave do dicionário
def passaLista(list):
   
   i=0
   dicionario = {}

   while i < len(list):
      dicionario[i] = list[i]
      i += 1  
   return (dicionario)      
