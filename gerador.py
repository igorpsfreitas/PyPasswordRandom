import random

def SorLetras(nLetras):
    letras = ("a","b","c","d","e","f","g","h","i","j","l","m","n",
                "o","p","q","r","s","t","u","v","x","z","w","y","k")
    solucao = ""
    while nLetras != 0:
        index = random.randrange(0,len(letras))
        solucao += letras[index]
        nLetras -= 1  

    return solucao

def UpLetras(letras):
    solucao = ""
    for letra in letras:
        razao = random.randrange(0,2)
        if razao == 1:
            solucao += letra.upper()
        else:
            solucao += letra
    
    return solucao

def SorNumeros(nNumeros):
    numeros = ("0","1","2","3","4","5","6","7","8","9")
    solucao = ""
    while nNumeros != 0:
        index = random.randrange(0,len(numeros))
        solucao += numeros[index]
        nNumeros -= 1  

    return solucao

def SorEspecial(nChar):
    charEspecial = ["!","@","#","$","%","*","(",")","'","-","=","´","`","<",
                ">",":","?",",",".",";","/","]","}","[","{","\\","|"]
    
    solucao = ""
    while nChar != 0:
        index = random.randrange(0,len(charEspecial))
        solucao += charEspecial[index]
        nChar -= 1  

    return solucao



def GerarSenha(digitos, caixaAlta, numeros, especial):
    
    if (not caixaAlta and not numeros and not especial):
        solucao = SorLetras(digitos)
        return solucao

    elif (caixaAlta and not numeros and not especial):
        solucao = UpLetras(SorLetras(digitos))
        return solucao

    elif (not caixaAlta and numeros and not especial):
        solucao = SorNumeros(digitos)
        return solucao

    elif (caixaAlta and numeros and not especial):
        if (digitos % 2 == 0):
            l1 = int(digitos/2)
            l2 = l1
        else:
            l1 = digitos//2
            l2 = l1 + 1
            
        lgeral = UpLetras(SorLetras(l2)) + SorNumeros(l1)
        
        lList = []
        for l in lgeral:
            lList.append(l)
            random.shuffle(lList)
        
        resultado = ""
        for l in lList:
            resultado += l
        
        return resultado

    elif (not caixaAlta and not numeros and especial):
        if (digitos % 2 == 0):
            l1 = int(digitos/2)
            l2 = l1
        else:
            l1 = digitos//2
            l2 = l1 + 1
            
        lgeral = SorLetras(l2) + SorEspecial(l1)
        
        lList = []
        for l in lgeral:
            lList.append(l)
            random.shuffle(lList)
        
        resultado = ""
        for l in lList:
            resultado += l
        
        return resultado

    elif (caixaAlta and not numeros and especial):
        if (digitos % 2 == 0):
            l1 = int(digitos/2)
            l2 = l1
        else:
            l1 = digitos//2
            l2 = l1 + 1
            
        lgeral = UpLetras(SorLetras(l2)) + SorEspecial(l1)
        
        lList = []
        for l in lgeral:
            lList.append(l)
            random.shuffle(lList)
        
        resultado = ""
        for l in lList:
            resultado += l
        
        return resultado

    elif (not caixaAlta and numeros and especial):
        if (digitos % 3 == 0):
            l1 = int(digitos/3)
            l2 = l1
            l3 = l2
        else:
            l1 = digitos//3
            l2 = l1
            l3 = l2 + 1

        lgeral = SorLetras(l3) + SorNumeros(l2) + SorEspecial(l1)

        lList = []
        for l in lgeral:
            lList.append(l)
            random.shuffle(lList)
        
        resultado = ""
        for l in lList:
            resultado += l
        
        return resultado

    elif (caixaAlta and numeros and especial):
        if (digitos % 3 == 0):
            l1 = int(digitos/3)
            l2 = l1
            l3 = l2
        else:
            l1 = digitos//3
            l2 = l1
            l3 = l2 + 1

        lgeral = UpLetras(SorLetras(l3)) + SorNumeros(l2) + SorEspecial(l1)

        lList = []
        for l in lgeral:
            lList.append(l)
            random.shuffle(lList)
        
        resultado = ""
        for l in lList:
            resultado += l
        
        return resultado