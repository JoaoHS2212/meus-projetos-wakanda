import os
import shutil

pasta = '.'  # Pasta atual, ~/codes git – tem teus .py pra testar
subpasta = 'python'  # Nome da subpasta pra .py

# Cria a subpasta se não existir
if not os.path.exists(os.path.join(pasta, subpasta)):
    os.makedirs(os.path.join(pasta, subpasta))
    print(f'Subpasta "{subpasta}" criada!')

movidos = 0
for arquivo in os.listdir(pasta):
    if arquivo.endswith('.py') and not arquivo.startswith('.'):  # Só .py, ignora ocultos como .git
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(pasta, subpasta, arquivo)
        shutil.move(origem, destino)
        print(f'Movido {arquivo} pra {subpasta}/')
        movidos += 1

if movidos == 0:
    print('Nenhum .py encontrado na pasta. Adiciona um teste e roda de novo!')
else:
    print(f'{movidos} arquivos .py movidos com sucesso!')