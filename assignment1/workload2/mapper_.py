import sys




def mapper():
    for lines in sys.stdin:
        line = lines.strip().split(",")

        if len(line) != 12:
            continue

        video_id, trending_dates, likes, dislikes, category, country = line[0], line[1], line[6], line[7], line[3], line[-1]

        if video_id == "video_id":
            continue

        idandcountry = video_id+","+country
        trending_date = re.sub("\D", "", trending_dates)
        str2 = trending_date[:-4] + trending_date[-2:] + trending_date[-4:-2]
        print("{}\t{}\t{}\t{}\t{}".format(idandcountry, str2, likes, dislikes, category))


if __name__ == '__main__':
    mapper()