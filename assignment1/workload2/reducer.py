import sys
import re


def read_map_output(file):

    for line in file:
        yield line.strip().split("\t")




def reducer():
    data_for_each_id = {}

    for video_id, trending_dates, likes, dislikes, country, category in read_map_output(sys.stdin):
        if "video_id" == video_id:
            continue

        key = tuple((video_id, country))

        if key not in data_for_each_id.keys():
            data_for_each_id[key] = [[], ]

        trending_date = re.sub("\D", "", trending_dates)
        str2 = trending_date[:-4] + trending_date[-2:] + trending_date[-4:-2]

        one_day = [str2, int(dislikes), int(likes)]
        data_for_each_id[key][0].append(one_day)
        data_for_each_id[key].append(category)

    dislikes_growth = []
    keys = data_for_each_id.keys()
    for key in keys:
        if data_for_each_id[key][0].__len__() < 2:
            continue

        dates = sorted(data_for_each_id[key][0], key=lambda s: s[0])
        init_dislike = dates[0][1]
        second_dislike = dates[1][1]
        init_like = dates[0][2]
        second_like = dates[1][2]

        if (second_dislike - init_dislike) > (second_like - init_like):
            gap = (second_dislike - init_dislike) - (second_like - init_like)
            if gap > 0:
                each = [key[0], gap, data_for_each_id[key][1], key[1]]
                dislikes_growth.append(each)

    output = ""

    new_dislikes_growth = sorted(dislikes_growth, key=lambda s: s[1], reverse=True)
    for each in new_dislikes_growth[:10]:
        output += '"{}" , {} , "{}" , "{}"\n'.format(each[0], each[1], each[2], each[3])

    print(output.strip())



if __name__ == '__main__':
    reducer()
