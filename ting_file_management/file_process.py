from ting_file_management.file_management import txt_importer


import sys


def process(path_file, instance):
    original_file = txt_importer(path_file)
    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(original_file),
        "linhas_do_arquivo": original_file,
    }

    for i in range(0, len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(dict_file)
    print(dict_file, file=sys.stdout)
    return dict_file


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)

    file_removed = instance.dequeue()
    print(
        f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout
    )


def file_metadata(instance, position):
    try:
        return print(instance.search(position), file=sys.stdout)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
