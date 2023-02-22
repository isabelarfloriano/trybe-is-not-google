def exists_word(word, instance):
    result = []
    for i in range(0, len(instance)):
        file = instance.search(i)
        lines = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for item, line in enumerate(file["linhas_do_arquivo"]):
            if word.casefold() in line.casefold():
                lines["ocorrencias"].append({"linha": item + 1})
        if lines["ocorrencias"]:
            result.append(lines)

    return result


def search_by_word(word, instance):
    result = exists_word(word, instance)

    for i, element in enumerate(result):
        for occurrence in element["ocorrencias"]:
            lines = instance.search(i)
            occurrence["conteudo"] = (
                lines["linhas_do_arquivo"][occurrence["linha"] - 1]
            )

    return result
