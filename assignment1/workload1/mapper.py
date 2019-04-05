import sys



def mapper():
    for line in sys.stdin:
        parts = line.strip().split(",")

        if len(parts) != 12:
            continue

        video_id = parts[0].strip()
        category = parts[3].strip()
        country = parts[-1].strip()
        if video_id == 'video_id':
            continue

        print("{}\t{}\t{}".format(category, video_id, country))


if __name__ == '__main__':
    mapper()