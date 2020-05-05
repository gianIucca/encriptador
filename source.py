#cria as 3 variáveis e atribui um valor vazio
resultado = ''
mensagem = ''
escolha = ''

#Cria um loop enquanto a escolha não for 0, o programa continua a rodar
while escolha != 0:
  escolha = input('\nVocê deseja criptografar ou descriptografar a mensagem?\nDigite 1 para criptografar, 2 para descriptografar e 0 para sair do programa.\n')

  #Se a escolha for 1, ele pede ao usuário a mensagem que será criptografada
  if escolha == '1':
    mensagem = input('\nDigite a mensagem que será criptografada\n')
    
    #A função de criptografia pega cada caractere da mensagem, volta duas posições na tabela e atribui este valor na variável resultado
    for i in range(0, len(mensagem)):
      resultado = resultado + chr(ord(mensagem[i]) - 2)

    #Imprime o resultado, pula uma linha e esvazia a string resultado
    print(resultado + '\n')
    resultado = ''

  #Se a escolha for 2, pede ao usuário a mensagem que será descriptografada
  elif escolha == '2':
    mensagem = input('\nDigite a mensagem que será descriptografada\n')
    for i in range (0, len(mensagem)):
      #Utiliza a função oposta que foi utilizada na criptografia para descriptografar
      resultado = resultado + chr(ord(mensagem[i]) + 2)

    #Imprime na tela o resultado(a mensagem descriptografada)
    print('A sua mensagem descriptografada é: \n' + resultado + '\n')

  #Se a escolha for diferente de zero, imprime um erro de valor inválido
  elif escolha != '0':
    print('Você entrou com um valor inválido, por favor tente novamente. \n')
