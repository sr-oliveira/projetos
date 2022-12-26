import os
import shutil


src = input("Insira a origem: ")
dst = input("Insira o destino: ")

def backup_folder(src, dst):
    # Verifica se a pasta de destino já existe
    if not os.path.exists(dst):
        # Se a pasta de destino não existir, cria a pasta
        os.makedirs(dst)

    # Lista todos os arquivos e pastas na pasta de origem
    items = os.listdir(src)

    # Para cada item na pasta de origem, copia para a pasta de destino
    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            # Se for um arquivo, copia o arquivo
            shutil.copy2(src_path, dst_path)
        else:
            # Se for uma pasta, chama a função de backup novamente recursivamente
            backup_folder(src_path, dst_path)

# Executa o backup da pasta "src" para a pasta "dst"
backup_folder("src", "dst")
