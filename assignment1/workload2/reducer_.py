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

    boundary_indices = [0,]
    data_for_each_id = []
    for index in range(1, len(data_for_each_id)):
        if data[index][0] != data[index-1][0]:
            boundary_indices.append(index)

    boundary_indices.append(len(data_for_each_id))
    certain_id = []
    for i in range(len(boundary_indices)-1):
        certain_id = data[boundary_indices[i]:boundary_indices[i+1]]
        data_for_each_id.append(certain_id)


    output_data = []
    for each in data_for_each_id:
        if each.__len__() < 2:
            continue

        that_id = sorted(each, key=lambda s:s[1])
        initial_like = that_id[0][3]
        second_like = that_id[1][3]
        initial_dislike = that_id[0][2]
        second_dislike = certain_id[1][2]
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
c