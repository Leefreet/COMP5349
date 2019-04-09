from pyspark import SparkContext
from operations import *
import argparse


if __name__ == '__main__':
    sc = SparkContext(appName="Trending-Category Correlation")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='file:///home/hadoop/COMP5349/assignment1/')
    parser.add_argument("--output", help="the output path",
                        default='file:///home/hadoop/COMP5349/out/')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    text = sc.textFile(input_path+'AllVideos_short.csv')
    raw_data = text.map(extract)
    header = raw_data.first()
    valid = raw_data.filter(lambda s:s!=header) # to remove the first line of the input .csv

    data = valid.reduceByKey(countries).map(get_length)

    categoryTrendingAverage = data.map(remove_id).aggregateByKey((0.0, 0.0), id_country_number, merge_numbers, 1).map(get_average_trending)
    categoryTrendingAverage.map(to_string).saveAsTextFile(output_path)

