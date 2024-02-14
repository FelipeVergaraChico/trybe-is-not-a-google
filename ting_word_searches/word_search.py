from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    fr = list()
    for index in range(len(instance)):
        lines = list()
        res = instance.search(index)
        data = txt_importer(res)
        for position in range(len(data)):
            if word in data[position].lower():
                lines.append({'linha': position + 1})
        if len(lines) == 0:
            return []
        dict = {
            "palavra": word,
            "arquivo": res,
            "ocorrencias": lines
        }
        fr.append(dict)
        return fr


def search_by_word(word, instance):
    fr = list()
    for index in range(len(instance)):
        lines = list()
        res = instance.search(index)
        data = txt_importer(res)
        for position in range(len(data)):
            if word in data[position].lower():
                new_dict = {
                    "linha": position + 1,
                    "conteudo": data[position]
                }
                lines.append(new_dict)
        if len(lines) == 0:
            return []
        dict = {
            "palavra": word,
            "arquivo": res,
            "ocorrencias": lines
        }
        fr.append(dict)
    return fr
