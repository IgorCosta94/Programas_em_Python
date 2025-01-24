from dataclasses import dataclass
@dataclass

class informacoes:
    codigo: int
    area: int
    doado: int
    nome_obra: str
    nome_autor: str
    editora: str
    n_paginas: int

exatas = [0] * 5
humanas = [0] * 5
biologicas = [0] * 5

##################################################################################################################################################

for w in range(0,5,1):
    codigo = int(input("Informe o código da obra: "))
    area = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
    doado = int(input("Informe se o livro é doado (1 - Sim, 2 - Não): "))
    nome_obra = input("Informe o nome da obra: ")
    nome_autor = input("Informe o nome do autor: ")
    editora = input("Informe o nome da editora: ")
    n_paginas = int(input("Informe o número de paginas: "))
    print()

    if area == 1:
        exatas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
    else:
        exatas[w] = informacoes(0,0,0, '','' , '', 0)
        
    if area == 2:
        humanas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
    else:
        humanas[w] = informacoes(0,0,0, '','' , '', 0)
        
    if area == 3:
        biologicas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
    else:
        biologicas[w] = informacoes(0,0,0, '','' , '', 0)


###################################################################################################################################################
print("CONSULTAR LIVRO\n")
estado = 0
estado = int(input("Para encerrar digite -1: "))
while estado != -1:
    
    cod = int(input("Informe o código da obra: "))
    nom = input("Informe o nome do livro: ")
    are = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
    
    if are == 1:
        x = 0  
        for w in range(0,5,1):
            if exatas[w].codigo == cod:
                print(f"Nome da obra:      {exatas[w].nome_obra}\n"
                      f"Nome do autor:     {exatas[w].nome_autor}\n"
                      f"Editora:           {exatas[w].editora}\n"
                      f"Número de paginas: {exatas[w].n_paginas}\n"
                      f"Código:            {exatas[w].codigo}\n"
                      f"area:              {exatas[w].area}\n")
                print("===============================================================================")
                x = 1
            elif exatas[w].nome_obra == nom:
                print(f"Nome da obra:      {exatas[w].nome_obra}\n"
                      f"Nome do autor:     {exatas[w].nome_autor}\n"
                      f"Editora:           {exatas[w].editora}\n"
                      f"Número de paginas: {exatas[w].n_paginas}\n"
                      f"Código:            {exatas[w].codigo}\n"
                      f"area:              {exatas[w].area}\n")
                print("===============================================================================")
                x = 1
                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")

                
    if are == 2:
        x = 0  
        for w in range(0,5,1):
            if humanas[w].codigo == cod:
                print(f"Nome da obra:      {humanas[w].nome_obra}\n"
                      f"Nome do autor:     {humanas[w].nome_autor}\n"
                      f"Editora:           {humanas[w].editora}\n"
                      f"Número de paginas: {humanas[w].n_paginas}\n"
                      f"Código:            {humanas[w].codigo}\n"
                      f"area:              {humanas[w].area}\n")
                print("===============================================================================")
                x = 1
            elif humanas[w].nome_obra == nom:
                print(f"Nome da obra:      {humanas[w].nome_obra}\n"
                      f"Nome do autor:     {humanas[w].nome_autor}\n"
                      f"Editora:           {humanas[w].editora}\n"
                      f"Número de paginas: {humanas[w].n_paginas}\n"
                      f"Código:            {humanas[w].codigo}\n"
                      f"area:              {humanas[w].area}\n")
                print("===============================================================================")
                x = 1
                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")

    if are == 3:
        x = 0  
        for w in range(0,5,1):
            if biologicas[w].codigo == cod:
                print(f"Nome da obra:      {biologicas[w].nome_obra}\n"
                      f"Nome do autor:     {biologicas[w].nome_autor}\n"
                      f"Editora:           {biologicas[w].editora}\n"
                      f"Número de paginas: {biologicas[w].n_paginas}\n"
                      f"Código:            {biologicas[w].codigo}\n"
                      f"area:              {biologicas[w].area}\n")
                print("===============================================================================")
                x = 1

            elif biologicas[w].nome_obra  == nom:
                print(f"Nome da obra:      {biologicas[w].nome_obra}\n"
                      f"Nome do autor:     {biologicas[w].nome_autor}\n"
                      f"Editora:           {biologicas[w].editora}\n"
                      f"Número de paginas: {biologicas[w].n_paginas}\n"
                      f"Código:            {biologicas[w].codigo}\n"
                      f"area:              {biologicas[w].area}\n")
                print("===============================================================================")
                x = 1
                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")
            
    estado = int(input("Para encerrar digite -1: "))

########################################################################################################################################################
    
print("Lista de Livros doados\n")   
print("Livro da área de exatas\n")
for w in range(0,5,1):
    if exatas[w].doado == 1:
        print(f"Nome da obra:     {exatas[w].nome_obra}\n"
             f"Nome do autor:     {exatas[w].nome_autor}\n"
             f"Editora:           {exatas[w].editora}\n"
             f"Número de paginas: {exatas[w].n_paginas}\n"
             f"Código:            {exatas[w].codigo}\n"
             f"area:              {exatas[w].area}\n")
        print("===============================================================================")
        
print("Livro da área de humanas\n")        
for w in range(0,5,1):    
    if humanas[w].doado == 1:
        print(f"Nome da obra:     {humanas[w].nome_obra}\n"
             f"Nome do autor:     {humanas[w].nome_autor}\n"
             f"Editora:           {humanas[w].editora}\n"
             f"Número de paginas: {humanas[w].n_paginas}\n"
             f"Código:            {humanas[w].codigo}\n"
             f"area:              {humanas[w].area}\n")
        print("===============================================================================")

print("Livro da área de Biologicas\n")         
for w in range(0,5,1):
    if biologicas[w].doado == 1:
        print(f"Nome da obra:     {biologicas[w].nome_obra}\n"
             f"Nome do autor:     {biologicas[w].nome_autor}\n"
             f"Editora:           {biologicas[w].editora}\n"
             f"Número de paginas: {biologicas[w].n_paginas}\n"
             f"Código:            {biologicas[w].codigo}\n"
             f"area:              {biologicas[w].area}\n")
        print("===============================================================================")

##########################################################################################################################################################

print("Lista de Livros comprados e com páginas entre 100 e 300\n")   
print("Livro da área de exatas\n")
for w in range(0,5,1):
    if exatas[w].doado == 2:
        if exatas[w].n_paginas >= 100 and exatas[w].n_paginas <= 300:
           print(f"Nome da obra:     {exatas[w].nome_obra}\n"
                 f"Nome do autor:     {exatas[w].nome_autor}\n"
                 f"Editora:           {exatas[w].editora}\n"
                 f"Número de paginas: {exatas[w].n_paginas}\n"
                 f"Código:            {exatas[w].codigo}\n"
                 f"area:              {exatas[w].area}\n")
           print("===============================================================================")
        
print("Livro da área de humanas\n")        
for w in range(0,5,1):    
    if humanas[w].doado == 2:
        if humanas[w].n_paginas >= 100 and humanas[w].n_paginas <= 300:
            print(f"Nome da obra:     {humanas[w].nome_obra}\n"
                 f"Nome do autor:     {humanas[w].nome_autor}\n"
                 f"Editora:           {humanas[w].editora}\n"
                 f"Número de paginas: {humanas[w].n_paginas}\n"
                 f"Código:            {humanas[w].codigo}\n"
                 f"area:              {humanas[w].area}\n")
            print("===============================================================================")

print("Livro da área de Biologicas\n")         
for w in range(0,5,1):
    if biologicas[w].doado == 2:
        if biologicas[w].n_paginas >= 100 and biologicas[w].n_paginas <= 300:
            print(f"Nome da obra:     {biologicas[w].nome_obra}\n"
                 f"Nome do autor:     {biologicas[w].nome_autor}\n"
                 f"Editora:           {biologicas[w].editora}\n"
                 f"Número de paginas: {biologicas[w].n_paginas}\n"
                 f"Código:            {biologicas[w].codigo}\n"
                 f"area:              {biologicas[w].area}\n")
            print("===============================================================================")


############################################################################################################################################################
print()
estado = 0
estado = int(input("Para encerrar digite -1: "))
while estado != -1:
    
    cod = int(input("Informe o código da obra que deseja alterar: "))
    are = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
    
    if are == 1:
        x = 0  
        for w in range(0,5,1):
            if exatas[w].codigo == cod:
                codigo = int(input("Informe o código da obra: "))
                area = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
                doado = int(input("Informe se o livro é doado (1 - Sim, 2 - Não): "))
                nome_obra = input("Informe o nome da obra: ")
                nome_autor = input("Informe o nome do autor: ")
                editora = input("Informe o nome da editora: ")
                n_paginas = int(input("Informe o número de paginas: "))

                if area == 1:
                    exatas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                elif area == 2:
                    humanas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                if area == 3:
                    biologicas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                x = 1
                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")

                
    if are == 2:
        x = 0  
        for w in range(0,5,1):
            if humanas[w].codigo == cod:
                codigo = int(input("Informe o código da obra: "))
                area = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
                doado = int(input("Informe se o livro é doado (1 - Sim, 2 - Não): "))
                nome_obra = input("Informe o nome da obra: ")
                nome_autor = input("Informe o nome do autor: ")
                editora = input("Informe o nome da editora: ")
                n_paginas = int(input("Informe o número de paginas: "))

                if area == 1:
                    exatas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                elif area == 2:
                    humanas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                if area == 3:
                    biologicas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                    
                x = 1

                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")

    if are == 3:
        x = 0  
        for w in range(0,5,1):
            if biologicas[w].codigo == cod:
                codigo = int(input("Informe o código da obra: "))
                area = int(input("Informe a área da  obra (1 - exatas, 2 - humanas, 3 - biologicas): "))
                doado = int(input("Informe se o livro é doado (1 - Sim, 2 - Não): "))
                nome_obra = input("Informe o nome da obra: ")
                nome_autor = input("Informe o nome do autor: ")
                editora = input("Informe o nome da editora: ")
                n_paginas = int(input("Informe o número de paginas: "))

                if area == 1:
                    exatas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                elif area == 2:
                    humanas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)
                if area == 3:
                    biologicas[w] = informacoes(codigo,area,doado, nome_obra,nome_autor , editora,n_paginas)

                x = 1

                
        if x == 0:
            print("Não foi possivel encontrar o livro\n")
        else:
            print("Livro encontrado\n")
            
    estado = int(input("Para encerrar digite -1: "))

#########################################################################################################################################################################

print("FIMMMMMMMMMMMMMMMMMMMMMMMMMMM.........................................")

