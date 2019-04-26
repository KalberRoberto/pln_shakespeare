import re
from collections import Counter
from operator import itemgetter

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ]+"
data = open("teste.txt").read()
tokens = re.findall(regex, data)
tokens_count = Counter(tokens)
def bigrama(w1, w2):
    count_w1 = tokens_count[w1]
    count_w1w2 = 0
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1
    return count_w1w2/count_w1

def trigrama(w1, w2, w3):
    count_w1w2 = 0
    count_w1w2w3 = 0
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2 and tokens[i+2] == w3:
            count_w1w2w3 += 1
    if(count_w1w2 == 0):
        return 0
    return count_w1w2w3/count_w1w2
  
def b_prob(w1):
    temp = []
    temp2 = []
    for i in tokens:
        temp.append(i)
        temp2.append(bigrama(w1, i))
    data = dict(zip(temp, temp2))
    return max_prob(data)

def t_prob(w1,w2):
    temp = []
    temp2 = []
    for i in tokens:
        temp.append(i)
        temp2.append(trigrama(w1,w2, i))
    data = dict(zip(temp, temp2))
    return max_prob(data)

def max_prob(data):
    lista=[]
    resultado=[]
    for i in sorted(data, key = data.get):
        lista.append(i)
    lista.reverse()
    resultado.append(lista[0])
    resultado.append(lista[1])
    resultado.append(lista[2])
    return resultado    
    

print("Digite 1 para bigrama e 2 para trigrama e X para sair")
cond = input()
if cond == "1":    
    ent=input("Digite a sentença: ").split(' ')
    ent.reverse()
    data = b_prob(ent[0])
    print (data)
elif cond == "2":
    ent=input("Digite a sentença: ").split(' ')
    ent.reverse()
    data = t_prob(ent[0], ent[1])
    print (data)
else:
    exit()
