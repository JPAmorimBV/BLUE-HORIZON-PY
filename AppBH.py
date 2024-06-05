import os

# listas  pessoas
email =["roberzinho@terra"]
nome = ["Roberto Junior Souza"]
nickName = ["rober"]
senha = ["123"]

#lista instituição 
cNPJ = []
emailINST = []
nomeINST = []
senhaINST = []

# lista quiz
respCERT = [1, 2, 3, 1, 3, 1, 1, 3, 1, 3]
jogadorRESP = []


# menu cadastro 
def cadastro():
    while True:
        # opções menu cadastro
        os.system("cls")
        print("BEM VINDO A BLUE HORIZON\n")
        print("1 - Ainda não tem cadastro? Faça seu cadastro aqui!")
        print("2 - Já tem cadastro? Faça o login aqui!")
        print("3 - Sair do app\n")
        
        try:
            num = int(input("Selecione uma opção: "))
           
            #opcao cadastrar    
            if num == 1:
                while True:
                    # opções cadastrar-se
                    print("Você é:\n")
                    print("1 - Sou adolescente")
                    print("2 - Sou professor")
                    print("3 - Sou uma instituição")
                    print("4 - Voltar ao menu de cadastro")
                    
                    try:
                        # cadastro adolescente
                        num2 = int(input("\nSelecione uma opção:"))
                        if num2 == 1:
                            email.append(input("\nInforme seu email: "))          
                            nome.append(input("Informe o seu nome completo: "))
                            nickName.append(input("Crie um nome de usuário (Esse nome ficará visível a outras pessoa): "))
                            nomeINST.append(input("Informe o nome da escola que estuda (caso não esteja mais estudando deixe em branco): "))
                            senhaCRIA = input("Digite uma senha: ")
                            senhaCONF = input("Confirme sua senha: ")
                           
                            # confirmação senha 
                            if senhaCRIA == senhaCONF:
                                senha.append(senhaCRIA)
                                print("\nCadastro efetuado com sucesso!")
                                input("Aperte ENTER para ser redirecionado para o menu")
                                menu()
                                break # para sair do loop 
                            
                            # erro senha
                            else:
                                print("As informações não estão de acordo")
                                input("Aperte ENTER para preencher novamente")

                        # cadastro professor
                        elif num2 == 2:
                            email.append(input("\nInforme o email institucional: "))
                            nome.append(input("Informe o seu nome completo: "))
                            nickName.append(input("Crie um nome de usuário (Esse nome ficará visível a outras pessoa): "))
                            nomeINST.append(input("Informe o nome da instituição a qual faz parte: "))
                            senhaCRIA = input("Digite uma senha: ")
                            senhaCONF = input("Confirme sua senha: ")
                          
                            # confirmação senha 
                            if senhaCRIA == senhaCONF:
                                senha.append(senhaCRIA)
                                print("\nCadastro efetuado com sucesso!")
                                input("Aperte ENTER para ser redirecionado para o menu")
                                menu()
                                break # para sair do loop 
                            
                            # erro senha
                            else:
                                print("As informações não estão de acordo")
                                input("Aperte ENTER para preencher novamente")

                        # cadastro escola
                        elif num2 == 3:
                            emailINST.append(input("\nInforme o email institucional: "))
                            nomeINST.append(input("Informe o nome da instituição: "))
                            cNPJ.append(input("Informe o CNPJ: "))
                            senhaCRIA = input("Digite uma senha: ")
                            senhaCONF = input("Confirme sua senha: ")
                            # confirmação senha 
                            if senhaCRIA == senhaCONF:
                                senha.append(senhaCRIA)
                                print("\nCadastro efetuado com sucesso!")
                                input("Aperte ENTER para ser redirecionado para o menu")
                                menu()
                                break # para sair do loop 
                            
                            # erro senha
                            else:
                                print("As informações não estão de acordo")
                                input("Aperte ENTER para preencher novamente")

                        # voltar ao cadastro
                        elif num2 == 4: 
                            cadastro()
                            break # sair do loop
                        
                        #exibir mensagem de erro numero    
                        else: 
                            print("Opção inválida!")
                            input("Aperte ENTER para voltar ao cadastro")
                    
                    #exixbir mensagem de erro letra
                    except ValueError:
                        print("Opção inválida! Digite apenas números.")
                        input("Aperte ENTER para voltar ao menu de cadastro")
                
            # opcao logar 
            elif num == 2:
                while True:
                    # opcaos logar
                    print("\n1 - Logar como adolescente/professor")
                    print("2 - Logar como instituição")
                    print("3 - Voltar ao menu de cadastro")
                    
                    try:
                        numero = int(input("\nSelecione uma opção: "))
                        
                        # Login adolescente professor    
                        if numero == 1:
                            print("\nLogin adolescente/professor\n")
                            nomeJogador = input("Digite o nome de usuário: ")
                            senhaJogador = input("Digite sua senha: ")
                            
                            # verificação verdadeira
                            if nomeJogador in nickName and senhaJogador in senha:
                                print("\nLogin bem sucedido!")
                                input("Aperte ENTER para ser redirecionado")
                                menu()
                                break # para sair do loop

                            #verificação falsa
                            elif nomeJogador != nickName and senhaJogador != senha: 
                                print("\nCredenciais inválidas. Tente novamente.\n")
                                input("Aperte ENTER para voltar e tente novamente")  
                            
                            else:
                                print("Opção inválida!")
                                input("Aperte ENTER para voltar e tente novamente")    
                            
                        # login instituição 
                        elif numero == 2:
                            print("\nLogin Instituição\n")
                            cnpjINST = input("Digite o CNPJ da escola: ")
                            cenhaINST = input("Digite senha: ")
                            
                            # verificacao verdadeira
                            if cnpjINST in  cNPJ and cenhaINST in senhaINST:
                                print("\nLogin bem sucedido!")
                                input("Aperte ENTER para ser redirecionado")
                                menu()
                                break # para sair do loop 

                            # verificação falsa
                            elif nomeJogador != nickName and senhaJogador != senha: 
                                print("\nCredenciais inválidas. Tente novamente.")
                                input("Aperte ENTER para voltar e tente novamente")  
                        
                        # opcao voltar menu cadastro 
                        elif numero == 3:
                            cadastro()
                            break

                        # exibir mensagem de erro numero (opcao logar)
                        else:
                            print("Opção inválida! Digite apenas números")
                            input("Aperte ENTER para voltar")    
                    # exibir mensagem de erro letra (opcao logar)
                    except ValueError:
                        print("Opção inválida! Digite apenas números.")
                        input("Aperte ENTER para voltar ao cadastro")        
          
            elif num == 3:
                os.system("cls")
                print("Sessão finalizada!")
                break
            
            # exibir mensagem de erro numero (def cadastro)
            else:
                print("Opção inválida!")
                input("Aperte ENTER para voltar ao menu de cadastro")
        
        # exibir mensagem de erro letra (def cadastro)
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            input("Aperte ENTER para voltar ao menu de cadastro")


def menu():
    while True:
        #opcoes menu
        os.system("cls")
        print(f"SEJA BEM VINDO USUÁRIO • {nickName[-1]} •\n\n")
        print("1 - Conheça os 10 principais problemas ambientais marinhos e suas causas")
        print("2 - Quiz")
        print("3 - Conheça o objetivo da Blue Horizon")
        print("4 - Perfil")
        print("5 - Sair da conta")
        

        try:  
            nunA = int(input("Selecione uma opção: "))
            
            # opcao causas ambientais 
            if nunA == 1:
                os.system("cls")
                print("""10 principais problemas dos oceanos

Estima-se que 8 milhões de toneladas de lixo por dia chegam aos oceanos por ação do Homem. 80 porcento da poluição marinha tem origem em terra, com consequências desastrosas na biodiversidade marinha. No Dia Nacional do Mar, que foi ontem (16 de novembro), a Quercus destacou os 10 principais problemas a afetar os Oceanos: 
 
1) Sobreexploração da pesca

Estudos indicam que há uma considerável redução nas populações de algumas espécies de peixes. Como exemplo, a sobrepesca do bacalhau nas águas do Canadá quase levou à extinção deste peixe e a pesca da sardinha em Portugal que tem recomendações de organismo científico internacional para que termine totalmente já este ano. Para além da sobrepesca, também existe uma grave falta de gestão da atividade ou incumprimento de regras. Falta de definição das dimensões dos animais ou da época de captura o que permita a captura de juvenis ou fêmeas com ovos são alguns dos problemas recorrentes.
 

2) Captura excessiva de espécies com ciclos de vida longos, tais como alguns tubarões e atuns

Algumas destas espécies são utilizadas para culinária de luxo ou com fins de terapias alternativas para tratamentos de saúde (exemplo, a barbatana de alguns tubarões é muito apreciada na Ásia). As espécies no topo das cadeias alimentares têm, normalmente um ciclo de vida mais longo, com reprodução mais espaçada, logo menos resistente à recuperação das espécies.
 

3) Aquacultura não sustentável

A aquicultura intensiva no mar promove a proliferação de agentes poluentes nas águas marinhas. A produção de peixes e bivalves implica a utilização de antibióticos e outros produtos químicos, alguns deles tóxicos para o ecossistema. Esta situação é facilmente visível nas águas da Ásia devido à produção intensiva de amêijoa vietnamita.
 

4) Lixo

A quantidade de lixos deixados nas praias ou atirados para as linhas de águas terrestres, tais como rios e ribeiras, têm como destino final o oceano. A situação é mais grave quando se tratam de resíduos não biodegradáveis, tais como os plásticos, que se vão fragmentando em partículas mais pequenas, os microplásticos, e que são confundidos com alimento por muitas espécies marinhas. Os microplásticos presentes em produtos de higiene e de limpezas domésticas e industriais também terão os mesmos destinos. As ilhas de lixo de plástico são já uma realidade em algumas zonas dos oceanos.
 

5) Aquecimento das águas

O aumento da temperatura dos mares causa imensas alterações nos ecossistemas marinhos, com consequências gravosas e letais para muitas espécies. É também responsável por alteração de rotas migratórias provocando desequilíbrios nas cadeias alimentares. Para se ter uma noção, o aquecimento de 0,5ºC nas águas dos recifes de coral, provoca a sua morte. Os recifes de coral saudáveis funcionam como “maternidades” e zonas de abrigo para variadíssimas espécies usadas na alimentação humana e das quais dependem algumas comunidades de povos pescadores.
 

6) Poluição

Muitos fertilizantes e pesticidas utilizados sistematicamente na agricultura acabam por ir parar ao oceano. Alguns desses produtos provocam alterações irreversíveis e fatais para as espécies (por exemplo, afetam no processo de reprodução). Além disso, se ingeridos pelo ser humano podem trazer problemas de saúde ao mesmo.
 

7) Concentrações elevadas de mercúrio

O mercúrio em excesso causa doenças graves nos seres vivos e no Homem. É um poluente que se acumula na cadeia alimentar (bioacumulação) e chega ao Homem através da ingestão de peixes, e que em excesso pode causar graves doenças. Daí o consumo de determinados peixes dever ser regrado, como o peixe-espada preto, o atum, entre outros.
 

8) Destruição de habitats

Existem habitats muito importantes como local de abrigo para a reprodução, por exemplo as pradarias marinhas e as florestas marinhas, que estão a ser destruídas por várias causas, entre as quais a utilização de artes de pescas agressivas como a pesca de arrasto.
 

9) Obras de engenharia e extração de petróleo

Todas as alterações do meio marinho provocadas por construções, perfurações em profundidade, e tantas outras (incluindo a poluição sonora) causam, alterações no habitat, provocam perturbações várias e produzem poluentes. Estes fatores contribuem para a destruição do habitat e comprometem a sobrevivência das espécies marinhas.
 

10) Acidificação dos Oceanos e corais

Algumas das mudanças verificadas com as alterações climáticas ao nível dos oceanos implicam alterações do Ph, devido ao aumento da concentração de CO2 na atmosfera. Esta situação é bem notória nas zonas tropicais, onde os ecossistemas marinhos são extremamente sensíveis e ricos em biodiversidade, e cujos habitats estão a sofrer alterações que se podem revelar irreversíveis, nomeadamente do caso dos recifes de corais.
""")
                input("Aperte ENTER para voltar ao menu principal")
            
            # opcao quiz
            elif nunA == 2:
                while True:
                    os.system("cls")
                    print("•QUIZ AMBIENTAL•\n")
                    print("COMO O QUIZ FUNCIONA?\nSerá apresentado uma pergunta para o jogador e algumas alternativas mas somente uma é a correta.")
                    input("Aperte ENTER para começar")
                    try:
                        # questao 1 
                        os.system("cls")
                        print("QUIZ - 1 \n")
                        print("O qual o poluente mais encontrado no mar?")
                        print("1 - Plástico")
                        print("2 - Borracha")
                        print("3 - Papel")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 2
                        os.system("cls")
                        print("QUIZ - 2 \n")
                        print("Qual a duração do lixo no mar?")
                        print("1 - 150 anos")
                        print("2 - 500 anos")
                        print("3 - 1 ano")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 3
                        os.system("cls")
                        print("QUIZ - 3 \n")
                        print("De onde vem o lixo marinho?")
                        print("1 - Das praias")
                        print("2 - Dos rios")
                        print("3 - Do descarte inadequado")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 4
                        os.system("cls")
                        print("QUIZ - 4\n")
                        print("Quantas toneladas de lixo são descartadas no mar todo ano?")
                        print("1 - 8 milhoes de toneladas")
                        print("2 - 10 mil toneladas")
                        print("3 - 100 mil toneladas")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 5
                        os.system("cls")
                        print("QUIZ - 5\n")
                        print("Dentre os países que mais descartam lixo no oceano, o Brasil está em qual posição?")
                        print("1 - 1° lugar")
                        print("2 - 10° lugar")
                        print("3 - 6° lugar")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 6
                        os.system("cls")
                        print("QUIZ - 6\n")
                        print("Por que o plástico é tão perigoso paras os animais marinhos?")
                        print("1 - Porque ele vira micro plásticos que eles acabam comendo e morrendo")
                        print("2 - Porque libera substâcias tóxicas")
                        print("3 - Porque o plástico impede as algas de crescerem")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 7
                        os.system("cls")
                        print("QUIZ - 7\n")
                        print("Por que a presença de lixo nos oceanos é um problema?")
                        print("1 - Porque afeta a vida de todos os seres vivos")
                        print("2 - Porque afeta somente o ser humano")
                        print("3 - Porque afeta as aves que se alimentam de peixes")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 8
                        os.system("cls")
                        print("QUIZ - 8\n")
                        print("Para evitar esse problema o que devemos fazer?")
                        print("1 - Jogar o lixo no chão")
                        print("2 - Jogar o lixo no mar")
                        print("3 - Descarte correto do lixo")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))
                                                                                                                                       
                        # questao 9
                        os.system("cls")
                        print("QUIZ - 9\n")
                        print("Quantos porcento do planeta é coberto por água?")
                        print("1 - 93%")
                        print("2 - 87%")
                        print("3 - 71%")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # questao 10
                        os.system("cls")
                        print("QUIZ - 10\n")
                        print("De toda a água no planeta qual que é a porcentagem de água potavel?")
                        print("1 - 10%")
                        print("2 - 5%")
                        print("3 - 3%")
                        jogadorRESP.append(int(input("Selecione uma alternativa: ")))

                        # pontuação
                        pontuacao = 0
                        for i in range(len(respCERT)):
                            if jogadorRESP[i] == respCERT[i]:
                                pontuacao += 1

                        # Mostra a pontuação final do jogador
                        print("\n\nSeu resultado final é:", pontuacao, "de 10")  
                        input("Aperte ENTER para voltar ao menu principal")
                        break
                    
                    # msg de erro letra 
                    except ValueError:
                        print("Opção inválida! Digite apenas números.")
                        input("Aperte ENTER para voltar ao quiz.")    

            # opcao objetivo blue horizon
            elif nunA == 3:
                os.system("cls")
                print("Blue Horizon\n")
                print("Buscamos criar uma plataforma interativa onde o jovem possa se sensibilizar, conscientizar-se e educar outros sobre a causa. Contendo jogos, quizzes, animações, histórias, personagens cativantes com quem podem conversar através de uma AI, rankings com premiações como viagens para incentivar o amor pelo meio ambiente, customização de perfil para o jovem poder se expressar através de suas conquistas, as possibilidades são infinitas dentro dessa plataforma. Durante nossa juventude tivemos a oportunidade de assistir e interagir com programas de televisão, histórias e jogos, mas poucos deles traziam formas de conscientização ambiental e diferente deles esse é o nosso intuito. Fazer com que durante toda essa experiência gamificada e sensibilizante, eles possam absorver a dor que nós causamos ao meio ambiente. Com isso, a plataforma conscientizará os adolescentes para que eles percebam por si mesmos os erros que nós cometemos com o meio ambiente. E, caso no dia-a-dia, vejam uma situação acontecendo vão repreender e também evitar de fazer esses erros. Como dito antes, a conscientização vem do filho para o pai, assim temos o intuito de criar uma sociedade que se importe com o meio ambiente, para que gerações futuras se importem cada vez mais. Criando um futuro com mais soluções e pessoas lutando pelo ecossistema.")
                input("\nAperte ENTER para voltar ao menu")

            # opcao informacoes do perfil
            elif nunA == 4:
                while True:
                    os.system("cls")
                    print("1 - Visualizar informações do perfil")
                    print("2 - Alterar informações")
                    print("3 - Voltar ao menu\n")
                    try: 
                        numb = int(input("Selecione uma opção: "))
                        
                        # informacoes o perfil
                        if numb == 1:
                            print("INFORMAÇÕES DO PERFIL\n")
                            print(f"Nome completo - {nome[-1]}")
                            print(f"Nome de usuário - {nickName[-1]}")
                            print(f"E-mail - {email[-1]}\n")
                            input("Aperte Enter para voltar ao menu")
                            break


                        # alterar informacoes perfil
                        elif numb == 2:
                            while True:
                                os.system("cls")
                                print("Quais informações deseja alterar?\n")
                                print("1 - Nome")
                                print("2 - Nome de usuário")
                                print("3 - E-mail")
                                print("4 - Senha")
                                print("\nPara voltar digite: 5 \n")
                                try:
                                    perfil = int(input("Selecione uma opção:"))
                                    
                                    # alterar nome
                                    if perfil == 1:
                                        emon = input("\nDigite novo nome: ")
                                        nome[-1] = emon 
                                        print("\nAlteração feita com sucesso!")
                                        input("Aperte ENTER para voltar")
                                        break

                                    # alterar nickname
                                    elif perfil == 2:
                                        nick = input("Digite novo nome de usuário: ")
                                        nickName[-1] = nick 
                                        print("\nAlteração feita com sucesso!")
                                        input("Aperte ENTER para voltar")
                                        break

                                    # alterar email
                                    elif perfil == 3:
                                        liame = input("Digite novo E-mail: ")
                                        email[-1] = liame 
                                        print("\nAlteração feita com sucesso!")
                                        input("Aperte ENTER para voltar")
                                        break

                                    # alterar senha 
                                    elif perfil == 4:
                                        ahnes = input("Digite a senha atual: ")
                                        if ahnes in senha:
                                            cenha = input("Digite nova senha: ")
                                            cenhaCONF = input("Confirme nova senha: ")
                                            
                                            # confirmacao de senha
                                            if cenha == cenhaCONF:
                                                senha[-1] = cenha
                                                print("Alteração feita com sucesso!")
                                                input("Aperte ENTER para voltar")
                                                break

                                            # senha diferente 
                                            else:
                                                print("As informações não estão de acordo")
                                                input("Aperte ENTER e tente novamente")
                                        else:
                                            print("As informações não estão de acordo")
                                            input("Aperte ENTER e tente novamente")
                                    # voltar ao menu anterior 
                                    elif perfil == 5:
                                        break


                                    # erro numero
                                    else:
                                        print("Opção inválida!")
                                        input("Aperte ENTER e tente novamente")

                                                                       
                                
                                # erro letra
                                except ValueError:
                                    print("Opção inválida! Digite apenas números.")
                                    input("Aperte ENTER para voltar")
                        
                        # voltar ao menu
                        elif numb == 3:
                            break
                            
                        # msg erro numero
                        else:
                            print("Opção inválida!")
                            input("Aperte ENTER e tente novamente")

                    # msg de erro letra
                    except ValueError:   
                        print("Opção inválida! Digite apenas números.")
                        input("Aperte ENTER para voltar") 
                
                
                



            # opcao sair da conta
            elif nunA == 5:
                break



        except ValueError:
            print("Opção inválida! Digite apenas números.")
            input("Aperte ENTER para voltar")
cadastro()