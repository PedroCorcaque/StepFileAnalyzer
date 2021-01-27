import sys, io, argparse

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
path = args["file"]

# def find_id(text):
#     return([pos for pos, char in enumerate(text) if char == '#'])

# def find_advanced_face():
#     with open(path) as file:
#         for line in file:
#             if line.find('ADVANCED_FACE') != -1:
#                 list_ids = []
#                 aux = ''
#                 for i in line:
#                     if i in ['0','1','2','3','4','5','6','7','8','9','#']:
#                         aux += i
#                     else:
#                         if aux:
#                             list_ids.append(aux)
#                             aux = ''
#                 return list_ids
