import csv

def extract(record):
    """
    :param record:input data
    :return: a tuple in form of ((category, video_id), country)
    """
    try:
        row = record.split(",")
        video_id, category, country = row[0], row[3], row[-1]
        return ((category, video_id), country)
    except:
        return ()



def countries(countries, country):
    """
    this function is to get all countries where a certain video_id has appeared in.
    :param countries:a string contains countries where a certain video_id has appeared in.
    :param country: current country
    :return: a string of conutries without duplication
    """
    if country not in countries:
        countries = countries + "|" + country

    return countries


def id_country_number(pair, current_country_number):
    """
    this function is to get the amount of ids appeared in a certain category and the total amount of countries corresponding to all ids.
    :param pair:(current total amount of countries, current id amount in a certain category)
    :param current_country_number:
    :return:(the cumulative sum of countries included in each id, all ids appeared in a certain category)
    """
    total_country_number, total_id_number = pair
    total_country_number += current_country_number
    total_id_number += 1
    return (total_country_number,total_id_number)


def merge_numbers(pair1, pair2):
    country_number1 ,id_number1 = pair1
    country_number2 ,id_number2 = pair2
    return (country_number1+country_number2, id_number1+id_number2)


def get_average_trending(pair):
    category, total_countries_ids = pair

    average_trending = total_countries_ids[0] / total_countries_ids[1]
    return (category, round(average_trending,2))


def get_length(pair):
    """
    this function is to get the amount of countries in the string.
    :param pair: ((category, video_id), countries string)
    :return: ((category, video_id), number of countries)
    """
    country_list = pair[1].strip().split("|")
    return (pair[0], len(set(country_list)))


def remove_id(pair):
    """
    this function is to remove video_id from key tuple, after this operation, the number of times that a certain category appears
    can replace the number of ids within this category.
    :param pair: ((category, video_id), number of countries)
    :return: (a category, number of countries )
    """
    t0, t1 = pair[0], pair[1]
    new_t0 = t0[0]
    return (new_t0, t1)


def to_string(pair):
    """
    change output to requried format
    :param pair:
    :return: a string in form of "category: averagetrending"
    """
    res_str = ""
    res_str = pair[0]+": "+str(pair[1])
    return res_str


