from pyspark import SparkContext
from operations import *
import argparse


if __name__ == '__main__':
    sc = SparkContext(appName="Trending-Category Correlation")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='~/asm1/')
    parser.add_argument("--output", help="the output path",
                        default='~/asm1/out_script/')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    text = sc.textFile(input_path+'AllVideos_short.csv')
    raw_data = text.map(extract)
    header = raw_data.first()
    valid = raw_data.filter(lambda x:x!=header)

    data = valid.reduceByKey(countries).map(get_length)

    categoryTrendingAverage = data.map(remove_id).aggregateByKey((0.0, 0.0), id_country_number, merge_numbers, 1).map(get_average_trending)
    categoryTrendingAverage.saveAsTextFile(output_path)

