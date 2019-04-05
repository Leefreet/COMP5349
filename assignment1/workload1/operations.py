import csv

def extract(record):
    try:
        row = record.split(",")
        video_id, category, country = row[0], row[3], row[-1]
        return ((category, video_id), country)
    except:
        return ()



def countries(countries, country):

    if country not in countries:
        countries = countries + "|" + country

    return countries


def id_country_number(pair, current_country_number):
    total_country_number, total_id_number = pair
    total_country_number += current_country_number
    total_id_number += 1
    return (total_country_number,total_id_number)


def merge_numbers(pair1, pair2):
    country_number1 ,id_number1 = pair1
    country_number2 ,id_number2 = pair2
    return (country_number1+country_number2, id_number1+id_number2)


def get_average_trending(line):
    category, total_countries_ids = line

    average_trending = total_countries_ids[0] / total_countries_ids[1]
    return (category, round(average_trending,2))


def get_length(tuple):
    country_list = tuple[1].strip().split("|")
    return (tuple[0], len(set(country_list)))


def remove_id(tuple):
    t0, t1 = tuple[0], tuple[1]
    new_t0 = t0[0]
    return (new_t0, t1)