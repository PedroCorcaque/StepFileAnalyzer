import sys, io, argparse
from steputils import p21
import numpy as np 

'''
Deve chamar uma função recursiva para eliminar as possibilidades das formas.

1º - Especificar cada forma;
2º - Função de abertura de arquivo;
3º - Função de chamada recursiva - Mostrar quais formas possiveis a cada revolução;
4º - Ter uma única saída
'''

argumentos = argparse.ArgumentParser(
    formatter_class=argparse.MetavarTypeHelpFormatter,
    description="Features recognition of the step files",
    )
argumentos.add_argument("-f", "--file", required=True, help="path of the input step file")
args = vars(argumentos.parse_args())
arquivo = args["file"]

def carregar_arquivo_step():
    
    try:
        arquivoStep = p21.readfile(arquivo)
    except IOError as e:
        print(str(e))
    except ParseError as e:
        print(str(e))
    else: # Arquivo carregado
        # Inicia mapeamento com id inicial
        linha = str(arquivoStep.__getitem__('#1040')) # Busca a linha de id # 1040
        inicio_valores = linha.find('(') # Busca o indice de inicio dos dados depois do título
        valores = linha[inicio_valores:-1] # Sepada os dados
        separadores = [pos for pos, char in enumerate(valores) if char == ','] # Busca os indices onde há virgula

        nome = valores[inicio_valores:separadores[0]] # Geralmente vazio
        descricao = valores[separadores[0]+1:separadores[1]] # ID da posição
        raio = valores[separadores[1]+1:-2] # Raio do circulo

        # Inicia busca pelo próximo ID
        linha = str(arquivoStep.__getitem__(descricao))
        inicio_valores = linha.find('(')
        valores = linha[inicio_valores:-1]
        separadores = [pos for pos, char in enumerate(valores) if char == ',']

        nome = valores[inicio_valores:separadores[0]]
        id_location = valores[separadores[0]+1:separadores[1]]
        id_z_axis = valores[separadores[1]+1:separadores[2]]
        id_x_axis = valores[separadores[2]+1:-2]

        # Inicia busca pelo location
        linha = str(arquivoStep.__getitem__(id_location))
        inicio_valores = linha.find('(')
        valores = linha[inicio_valores:-1]
        separadores = [pos for pos, char in enumerate(valores) if char == ',']

        coordenadas_location = valores[separadores[0]+1:-2]
        separadores_coord = [pos for pos, char in enumerate(coordenadas_location) if char == ',']
        coordenadas_location_tratadas = [float(coordenadas_location[1:separadores_coord[0]]) , float(coordenadas_location[separadores_coord[0]+1:separadores_coord[1]]) , float(coordenadas_location[separadores_coord[1]+1:-2])]
        array = np.array(coordenadas_location_tratadas)
        location = array*1000 # location pronto

        # Inicia busca pelo eixo z
        linha = str(arquivoStep.__getitem__(id_z_axis))
        inicio_valores = linha.find('(')
        valores = linha[inicio_valores:-1]
        separadores = [pos for pos, char in enumerate(valores) if char == ',']

        valores_eixo = valores[separadores[0]+1:-2]
        separadores_valores = [pos for pos, char in enumerate(coordenadas_location) if char == ',']
        eixo_z = valores_eixo[0:separadores_valores[0]]
        
        # Inicia busca pelo eixo x
        linha = str(arquivoStep.__getitem__(id_x_axis))
        inicio_valores = linha.find('(')
        valores = linha[inicio_valores:-1]
        separadores = [pos for pos, char in enumerate(valores) if char == ',']

        valores_eixo = valores[separadores[0]+1:-2]
        separadores_valores = [pos for pos, char in enumerate(coordenadas_location) if char == ',']
        eixo_x = [
            valores_eixo[0:separadores_valores[0]],
            valores_eixo[separadores_valores[0]:separadores_valores[1]],
        ]

        resposta = {
            "location: ":location,
            "radius: ":raio,
            "type: ":"Circle",
            "x_axis: ":eixo_x,
            "z_axis: ":eixo_z
        }
        for titulo,valor in resposta.items():
            print(titulo, valor)        
                

carregar_arquivo_step()