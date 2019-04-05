import sys




def mapper():
    for lines in sys.stdin:
        line = lines.strip().split(",")

        if len(line) != 12:
            continue

        video_id, trending_date, likes, dislikes, country, category = line[0], line[1], line[6], line[7], line[-1], line[3]

        print("{}\t{}\t{}\t{}\t{}\t{}".format(video_id, trending_date, likes, dislikes, country, category))


if __name__ == '__main__':
    mapper()