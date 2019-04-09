#!/usr/bin/python3

import sys
import re


def read_map_output(file):

    for line in file:
        yield line.strip().split("\t")



def reducer():
    output = ""
    data= []
    for id_country, date, like, dislike, category in read_map_output(sys.stdin):
        each = [id_country, date, dislike, like, category]
        data.append(each)
    # make a list which contains each line in the input also as a list
    boundary_indices = [0,]
    data_for_each_id = []
    for index in range(1, len(data)):
        if data[index][0] != data[index-1][0]:
            boundary_indices.append(index)

    boundary_indices.append(len(data))
    # get all boundaries of different video_id,
    # for convenience in later computation, added 0 as the first boundary and the length of input data as the final boundary

    for i in range(len(boundary_indices)-1):
        certain_id = data[boundary_indices[i]:boundary_indices[i+1]]
        data_for_each_id.append(certain_id)
    # to seperate the data for each video_id

    output_data = []
    for i in range(len(data_for_each_id)):
        if len(data_for_each_id[i]) >= 2:
            # video_id that has less than 2 records cannot be calculate and hence ignored
            that_id = sorted(data_for_each_id[i], key=lambda s:s[1])
            #sort all record of a certain video_id by date successively
            init_like = int(that_id[0][3])
            second_like = int(that_id[1][3])
            init_dislike = int(that_id[0][2])
            second_dislike = int(that_id[1][2])
            if (second_dislike - init_dislike) > (second_like - init_like):
                gap = (second_dislike - init_dislike) - (second_like - init_like)
                if gap > 0:
                    id_and_country = that_id[0][0].split(",")
                    out = [id_and_country[0], gap, that_id[0][4], id_and_country[1]]
                    output_data.append(out)


    top10 = sorted(output_data, key=lambda s:s[1], reverse=True)[:10]
    for each in top10:
        output += '"{}" , {} , "{}" , "{}"\n'.format(each[0], each[1], each[2], each[3])

    print(output.strip())


if __name__ == '__main__':
    reducer()
