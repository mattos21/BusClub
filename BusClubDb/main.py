# -*- coding: utf-8 -*-
from BusStopClubServer import BusStopClubServer

menu = True
BusStopClubServer.build()

while(menu):
    print ("Menu principal: \n")
    print ("1 - Login")
    print ("2 - Cadastro")
    opcao = input("Escolha sua opção: ")
    print opcao
    if opcao == 1:
        Email = input("Seu email: ")
        Senha = input("Sua senha: ")
        if BusStopClubServer.login(Email,Senha):
            menu = False
        else:
            print("Não foi possível fazer o login, tente novamente.")
    if opcao == 2:
        Nome = input("Nome: ")
        Email = input("Email: ")
        Senha = input("Senha: ")
        BusStopClubServer.cadastro(Nome,Email,Senha)
    else:
        print ("Não foi escolhida nenhuma opção válida. Tente novamente.")