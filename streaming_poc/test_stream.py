import csv
import sys
import getopt
import re
import jsonlines
import urllib.parse as urlparse
import json

def main(argv):
	csv_filename = ''	
	json_filename = ''
	p_type = ''	
 
	try:
		opts, args = getopt.getopt(argv,"hi:o:t:",["ifile=","ofile=","type="])

	except getopt.GetoptError:
		print ('test.py -i <csv path to inputfile> -o <json path to outputfile> -t <batch/stream>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <csv path to inputfile> -o <json path to outputfile> -t <batch/stream>')
			sys.exit(2)
		elif opt in ("-i","--ifile"):
			csv_filename = arg
			print (csv_filename)
		elif opt in ("-o", "--ofile"):
			json_filename = arg
			print (json_filename)
		elif opt in ("-t","--type"):
			p_type = arg
			print (p_type)
 
	if p_type == 'batch':
		start_batch_processing(csv_filename,json_filename)
	elif p_type == 'stream':
		start_stream_processing(csv_filename,json_filename)

def start_batch_processing(csv_file,json_file):
	csv_data = []
	anonymous_user_id_value=""
	url_value=""
	time_value=""
	browser_value=""
	os_value=""
	screen_resolution_value=""
	utm_source_value=""
	utm_medium_value=""
	url_path_value=""

	with open(csv_file) as csvfile:
		csv_reader = csv.DictReader(csvfile)
		csv_header = csv_reader.fieldnames
		for row in csv_reader:
			for i in range(len(csv_header)):
				if csv_header[i] == 'anonymous_user_id':
	 				anonymous_user_id_value = row[csv_header[i]] 
				elif csv_header[i] == 'url':
					try:
						url_value = row[csv_header[i]] 
						parsed = urlparse.urlparse(row[csv_header[i]])
						url_path_value = parsed.path
						params = urlparse.parse_qs(parsed.query) 
						utm_source_value = params['utm_source'][0]
						utm_medium_value = params['utm_medium'][0]
					except KeyError:
	  					pass
				elif csv_header[i] == 'time':
	 				time_value = row[csv_header[i]]
				elif csv_header[i] == 'browser':
	 				browser_value = row[csv_header[i]]
				elif csv_header[i] == 'os':
	 				os_value = row[csv_header[i]]
				elif csv_header[i] == 'screen_resolution':
	 				screen_resolution_value = row[csv_header[i]]
			if utm_source_value != "":
					csv_data.extend([{'anonymous_user_id':anonymous_user_id_value,\
					      		  'url':url_value,\
			                      'time':time_value,\
			                      'browser':browser_value,\
			                      'os':os_value,\
			                      'screen_resolution':screen_resolution_value,\
			                      'utm_source':utm_source_value,\
			                      'utm_medium':utm_medium_value,\
			                      'path':url_path_value}])
					anonymous_user_id_value=""
					url_value=""
					time_value=""
					browser_value=""
					os_value=""
					screen_resolution_value=""
					utm_source_value=""
					utm_medium_value=""
					url_path_value=""
					write_json(csv_data,json_file)

def start_stream_processing(csv_file,json_file):
	csv_data = []
	anonymous_user_id_value=""
	url_value=""
	time_value=""
	browser_value=""
	os_value=""
	screen_resolution_value=""
	utm_source_value=""
	utm_medium_value=""
	url_path_value=""
	line_ctr=0
	min_time_value=0
	max_time_value=0
	unique_user_count=0
	anon_user_ids=[]

	with open(csv_file) as csvfile:
		csv_reader = csv.DictReader(csvfile)
		csv_header = csv_reader.fieldnames
		for row in csv_reader:

			for i in range(len(csv_header)):
				if csv_header[i] == 'anonymous_user_id':
					anonymous_user_id_value = row[csv_header[i]]
					
				elif csv_header[i] == 'url':
					try:
						url_value = row[csv_header[i]] 
						parsed = urlparse.urlparse(row[csv_header[i]])
						url_path_value = parsed.path
						params = urlparse.parse_qs(parsed.query) 
						utm_source_value = params['utm_source'][0]
						utm_medium_value = params['utm_medium'][0]

					except KeyError:
						pass
				elif csv_header[i] == 'time':
					time_value = row[csv_header[i]]
				elif csv_header[i] == 'browser':
					browser_value = row[csv_header[i]]
				elif csv_header[i] == 'os':
					os_value = row[csv_header[i]]
				elif csv_header[i] == 'screen_resolution':
					screen_resolution_value = row[csv_header[i]]			
   				
			if utm_source_value != "":


				if not anonymous_user_id_value in anon_user_ids:
					unique_user_count = unique_user_count+1
					anon_user_ids.extend([{anonymous_user_id_value}])
				if min_time_value == 0 or max_time_value == 0:
					min_time_value=time_value
					max_time_value=time_value
				else:
					if int(time_value)<int(min_time_value):
						min_time_value=time_value
					if int(time_value)>int(max_time_value):
						max_time_value=max_time_value

				csv_data.extend([{'anonymous_user_id':anonymous_user_id_value,\
								'url':url_value,\
								'time':time_value,\
								'browser':browser_value,\
								'os':os_value,\
								'screen_resolution':screen_resolution_value,\
								'utm_source':utm_source_value,\
								'utm_medium':utm_medium_value,\
								'path':url_path_value}])
				anonymous_user_id_value=""
				url_value=""
				time_value=""
				browser_value=""
				os_value=""
				screen_resolution_value=""
				utm_source_value=""
				utm_medium_value=""
				url_path_value=""

				line_ctr = line_ctr + 1

				if line_ctr == 1000:
					csv_data.append({'min_time_value':min_time_value,\
									'max_time_value':max_time_value,\
									'unique_user_count':unique_user_count})
					write_json(csv_data,json_file)
					line_ctr=0
					# min_time_value=0
					# max_time_value=0
					# unique_user_count=0
					anon_user_ids=[]
					print(min_time_value)
					print(max_time_value)
					print(unique_user_count)

def write_json(csv_data,json_file):
	with jsonlines.open(json_file, 'w') as writer:
		writer.write_all(csv_data)

if __name__ == '__main__':
	main(sys.argv[1:])
