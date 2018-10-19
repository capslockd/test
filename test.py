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
  start_batch_processing(csv_filename,json_filename,p_type)
 elif p_type == 'stream':
  print ('Start Stream processing')

def start_batch_processing(csv_file,json_file,processing_type):
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

def write_json(csv_data,json_file):
 with jsonlines.open(json_file, 'w') as writer:
  writer.write_all(csv_data)

if __name__ == '__main__':
 main(sys.argv[1:])
