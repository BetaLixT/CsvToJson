import argparse
import csv
import configparser
import json

parser = argparse.ArgumentParser(description='Convert from CSV to json')
parser.add_argument('--input', dest='inputFile', default="sample.csv", help='csv input file')
parser.add_argument('--output', dest='outputFile', default="sample.json", help='json output file')
parser.add_argument('--config', dest='configFile', default="config.ini", help='config file')

args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.configFile, encoding='UTF-8')
mapping = config["MAPPING"]


with open(args.inputFile, "r", encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    fields = list()
    records = list()
    for row in csv_reader:
        if line_count == 0:
            fields = row
            line_count += 1
        else:
            record = dict()
            for key in mapping.keys():
                record[key] = row[fields.index(mapping[key])]
            records.append(record)
            line_count += 1

jsonStr = json.dumps(records)
with open(args.outputFile, "w", encoding='UTF-8') as text_file:
    text_file.write(jsonStr)