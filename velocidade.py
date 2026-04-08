limite_de_velocidade = 80

velocidade_do_carro = float(input("Qual a velocidade do seu carro? "))

calculo_da_multa = float((velocidade_do_carro-limite_de_velocidade) * 7.00)

if(limite_de_velocidade >= velocidade_do_carro):
    print("Boa viagem, tenha um bom dia")
else:
    print("Você foi multado, a multa é de", calculo_da_multa, "euros" )