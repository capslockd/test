import csv
import sys
import jsonlines

## pip install jsonlines
filename = 'data_sample.csv'
json_filename = 'json_data.jsonl'

def main():
	datafile =  open(filename, 'r')
	jsonl_file = jsonlines.open(json_filename, 'w')

	csv_datafile = csv.DictReader(datafile, delimiter=',', quotechar='"')
	for data_line in csv_datafile:
		userid = data_line['anonymous_user_id']
		url = data_line['url']
		time = data_line['time']
		browser = data_line['browser']
		os = data_line['os']
		screen_resolution = data_line['screen_resolution']
		jsonl_file.write(userid)
		jsonl_file.write(time)



if __name__ == '__main__':
	main()
