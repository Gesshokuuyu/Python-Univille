usuarioBase = 'Andrei'
senhaBase = 'Pass123'

userInput = input('Usuário: ')
passInput = input('Senha: ')

if userInput == usuarioBase and senhaBase == passInput:
    print('Autenticação realizada com sucesso')
else :
    print('Credenciais inválidas')
