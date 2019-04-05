import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split("\t")


def reducer():
    category_ids = {}
    ids_countrys = {}
    average_country_number = {}
    category_country_number = {}


    for cat, id, country in read_map_output(sys.stdin):
        if cat not in category_ids.keys():
            category_ids[cat] = []
        if id not in ids_countrys.keys():
            ids_countrys[id] = []
        if cat not in average_country_number.keys():
            average_country_number[cat] = 0
        if cat not in category_country_number.keys():
            category_country_number[cat] = 0

        category_ids[cat].append(id)
        ids_countrys[id].append(country)

    for cat in category_ids.keys():
        category_ids[cat] = list(set(category_ids[cat]))

    for id in ids_countrys.keys():
        ids_countrys[id] = list(set(ids_countrys[id]))

    category_id_number = {}
    ids_country_number = {}
    for id in ids_countrys.keys():
        if id not in ids_country_number.keys():
            ids_country_number[id] = 0
        ids_country_number[id] = ids_countrys[id].__len__()

    for category in category_ids.keys():
        if category not in category_id_number.keys():
            category_id_number[category] = 0
        category_id_number[category] = category_ids[category].__len__()

    for category in category_country_number.keys():
        sum = 0
        for id in category_ids[category]:
            sum += ids_country_number[id]
        category_country_number[category] = sum

    for category in average_country_number.keys():
        average_country_number[category] = category_country_number[category] / category_id_number[category]

    output = ""
    for category, average in average_country_number.items():
        output += "{} : {:.2f}\n".format(category, average)

    print(output.strip())



if __name__ == '__main__':
    reducer()