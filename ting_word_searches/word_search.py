def exists_word(word, instance):
    result = []
    for i in range(0, len(instance)):
        file = instance.search(i)
        lines = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for line in file:
            if word.casefold() in line.casefold():
                lines["ocorrencias"].append({"linha": file.index(line) + 1})
        if lines["ocorrencias"]:
            result.append(lines)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
