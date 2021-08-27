# Aluno: Gabriel Gomes de Sousa 

# RA: 72100111 

# Curso: Algoritmos e Légica de PRogramação -Turma C - 0121 - Virtual - ini: 22/02/2021 

# Professor: Marcelo Carboni Gomes 

  

caixa = []  # Aqui ficar os valores em MS 

  

  

def calculadora(): 

    print() 

    print("Nova operação seja bem vindo") 

    print() 

    a = int(input("1ª numero: "))       # Aqui estou colhendo o valor da variavel "a", que tem ser um numero. 

    b = input("Sinal: ")                # Aqui estou colhendo o valor da variavel "b", que tem ser um sinal de operação 

    c = int(input("2ª numero: "))       # Aqui estou colhendo o valor da variavel "c", que tem ser um numero. 
  
    def memoria_principal(d):                  # Esse metodo é chamado quando coloco MS. 

        caixa.append(d)                        # Aqui adiciono resultado na memoria. 

        print() 

        print("Salvo !")                       # mensagem de confirmação 

        print() 

        calculadora() # Depois que foi salvo o resultado na memória chamo o 

                      # metodo calculadora() e começo todo processo mais com o resultado  

                      # salvo na memoria. 
  

    def ms2(t):                # Esse metodo é chamado quando eu coloco M+ ou M- que  

                               # quero salva o resultado na memoria. 

        

        caixa.append(t)         #Aqui adiciono resultado na memoria. 

        print() 

        print("Salvo !") 

        print() 

        calculadora()   # Depois que foi salvo o resultado na memória chamo o 

                        # metodo calculadora() e começo todo processo mais com o 

                        # resultado salvo na memoria. 


    def adicionar_memoria(d):  # Esse metodo é chamado quando eu coloco m+ 

            t = int(d)+caixa[0] # Aqui eu calculo o ultimo resultado e adiciono com o  

                                # valor que esta na memoria. 

            print("------------------------------------------------------------------") 

            print() 

            print("O resultado de "+  str(caixa[0]) + " + " + str(d) +" ficou "+str(t)) 


            # O cadigo acima mostra o resultado. Logo depois questiono o usuario se ele 

            # quer salva o resultado na memoria.     

        
            print()                

            print("Deseja continuar ?\ns - para sim\nn - para não\nms - Salva na Memoria") 

            p = input("Eu quero: ") 

            print() 

            if p == "s":        # Aqui é uma condição/decisão que eu quero que minha  

                calculadora()   # calculadora execute. Se "p" for igual a "s" então vou 

            elif p == "n":      # vou chamar o metodo principal e valtar todo processo. Se 

                return            # "p" for igual a "n" então o programa retorna para fim do 

                                       # codigo e conclui todo processo. Se "p" for igual a "ms"  

            elif p == "ms":     # então a calculadora vai excluir o valor que esta na  

                caixa.clear()   # memoria e vai chama o metodo ms2() que adiciona esse 

                ms2(t)          # novo resultado. ms2() depois de ter adcionado vai  

                                # chamar o metodo calculadora() e começa tudo de novo. 


    def subtrair_memoria(d):  # Esse metodo é chamado quando eu coloco m- 

        t = int(d)- caixa[0] # Aqui eu calculo o ultimo resultado e subtraiu com o  

                             # valor que esta na memoria. 

        print("O resultado de "+ str(caixa[0]) + " - " + str(d) +" ficou "+str(t)) 

        # O cadigo acima mostra o resultado. Logo depois questiono o usuario se ele 

        # quer salva o resultado na memoria. 
          

        print() 

        print("Deseja continuar ?\ns - para sim\nn - para não\nms - para salva o resultado na memoria") 

        p = input("Eu quero: ") 

        print() 

        if p == "s":            # Aqui é o mesmo processo da decisão de cima para m+ 

                calculadora() 

        elif p == "n": 

            return 

        elif p == "ms": 

            caixa.clear() 

            ms2(t) 
  
       # Aqui é o metodo que chamo quando coloco o sinal "+".  
    def sinais(b):        
        if b == "/":            # então aqui eu separo para qual metodo eu quero que 

            d = int(a) / int(c)         # minha calculadora execute, com sua devida chamada de 
            calcular(d)
        elif b == "-":          # metodo apropriado. 

            d = int(a) - int(c)
            calcular(d)      
        elif b == "+": 

            d = int(a) + int(c)
            calcular(d)
        elif b == "*": 

            d = int(a) * int(c)
            calcular(d)
        else:            
     
            print() 
            print("Não é um sinal invalido, por favor tente novamente.") 

            calculadora()   

    def calcular(d):                  

        print("O resultado é: " + str(d)) #Aqui mostro resultado 

        print() 

        print("Deseja continuar ?\ns - para sim\nn - para não\nv - Ver valor salvo na memoria.\nms - para salva o resultado na memoria\na - Que é para_( M+ )_para adicionar com numero salvo na memoria\nb - Que é para _( M- )_ para subtrair com numero salvo na memoria ") 

        p = input("Eu quero: ") # Aqui pergunto para o usuario quais opções ele deseja 

        print()                 # Deseja continuar ? sim ou não. 

                                    # Deseja ver o valor na memoria ? 

                                    # Deseja salva o resultado na memoria ? 

                                    # Deseja adicionar o ultimo resultado com o valor que  

                                    # esta salvo na memoria ? 

                                    # Deseja subtrair o ultimo resultado com o valor que  

                                    # esta salvo na memoria ? 

        print("------------------------------------------------------------------") 

        if p == "s":        # Se "p" for igual a "s" que é sim então vai chama o 

            calculadora()   #  metodo calculadora() que vai volta o processo todo. 

        elif p == "n":      # Se "p" for igual a "n" que é não, vai retorna e 

            return         # finaliza a calculadora. 

        elif p =="ms":      # Se "p" for igual a "ms" vai excluir o ultimo resultado  

            caixa.clear()   # e vai chamar o metodo_principal() que vai adicionar o   

                                # resultado atual na memoria. 

            memoria_principal(d)  

        elif p == "a":      # Se "p" for a igual a "a" que esta referenciado a 
            if  not caixa:  # se sim então vai mostra a mensagem "Não tem numero na  

                                # memória". 

                print("Não tem numero na memória") 

                print() # depois pergunto se o usuario quer salva esse 

                            #resultado atual. 

                print("mais você gostaria de salva o ultimo resultado ?\ns - para sim.\nn - para não.") 

                print() 

                q = input("Eu quero: ") 

                if q == "s":        # Se sim então salvo o resultado na memoria. 

                    caixa.append(d) 

                    print() 

                    print("Salvo!") 

                    calculadora()   # Depois reinicio o todo processo. 

                else: 

                    calculadora()   # Se não valto ao inicio de todo processo. 

            else: 

                adicionar_memoria(d) # Se a memoria estiver ocupada então chamo o  

                                         # metodo adicionar_memoria() 

        elif p == "b": # O "b" esta referênciado o m- e o processo é o mesmo do "a". 

            if  not caixa: 

                print("Não tem numero na memoria") 

                print() 

                print("mais você gostaria de salva o ultimo resultado ?\ns - para sim.\nn - para não.") 

                print() 

                q = input("Eu quero: ") 

                if q == "s": 

                    caixa.append(d) 

                    print() 

                    print("Salvo!") 

                    calculadora() 

                else: 

                    calculadora() 

            else: 

                subtrair_memoria(d) 

                                             

        elif p == "v": # Se "p" for igual "v" então vou conseguir ver o    

                           # valor salvo na memoria. 

            if len(caixa) == 0: # Se estiver vazio vai mostra as messagem abaixo. 

                print("Não tem numero na memoria") 

                print() # Vou pergunta se o usuario quer salva ou não. 

                print("mais você gostaria de salva o ultimo resultado ?\ns - para sim.\nn - para não.") 

                q = input("Eu quero: ") 

                if q == "s": #  Se sim  

                    caixa.append(d) # Vai ser adicionado o resultado na memoria. 

                    print() 

                    print("Salvo!") # mostro a confirmação 

                    calculadora() # Depois vai chamar o metodo principal e  

                                      # recomeça o processo. 

                else: 

                    calculadora() # Se não quero salva chamo calculadora() e vai 

                                          # recomeça todo o processo.     

            else: # Se a memória estive ocupado então vou mostra o resultado atual. 

                print("O valor salvo na memoria é: "+ str(caixa[0])) 

                print("Você gostaria de salva o ultimo resultado ?\ns - para sim.\nn - para não.") 

                q = input("Eu quero: ") # Vou pergunta se o usuario quer salva o 

                                            # resultado. 

                if q == "s": #  Se sim  

                    caixa.append(d) # Vai ser adicionado o resultado na memoria. 

                    print() 

                    print("Salvo!") # mostro a confirmação 

                    calculadora()  # Depois vai chamar o metodo principal e recomeça  

                                       # todo o processo. 

                else: 

                    calculadora() # Se não quero salva chamo calculadora() que vai 

                                          # recomeça todo processo.     

        else:            

            calculadora() # Se eu colocar alguma imformação diferente, vou valta para  

                              # metodo principa e recomeça tudo denovo. 

    sinais(b)           

calculadora()  

            

# Quando é acionado o return o programa vem para a linha depois da chamada de função 

# e meu programa encerra. 