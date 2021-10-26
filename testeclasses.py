from validate_docbr import CPF

cpf = CPF()

cpf_usuario = input('digite seu cpf: ')
#print('seu cpf é: '+ cpf)


print(cpf.validate(cpf_usuario))



if cpf.validate(cpf_usuario) == False:
    print('é falso')
else:
    print('é verdadeiro')