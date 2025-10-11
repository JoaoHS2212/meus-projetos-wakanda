import os
import shutil

pasta = '.'  # Pasta atual, ~/codes git
subpasta = 'python'

# Cria a subpasta se não existir
if not os.path.exists(os.path.join(pasta, subpasta)):
    os.makedirs(os.path.join(pasta, subpasta))
    print(f'Subpasta "{subpasta}" criada!')

movidos = 0
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.py') and not arquivo.startswith('.'):
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(pasta, subpasta, arquivo)
        shutil.move(origem, destino)
        print(f'Movido {arquivo} pra {subpasta}/')
        movidos += 1

if movidos == 0:
    print('Nenhum .py encontrado. Adiciona um teste!')
else:
    print(f'{movidos} arquivos .py movidos com sucesso!')
