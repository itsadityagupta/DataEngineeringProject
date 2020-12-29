import sys
import os
from config import BUCKET_NAME, FOLDER
from datetime import datetime

class DataRead:
	'''
	Reads data from publicly accessible google cloud bucket.
	'''
	def __init__(self, bucket_name, folder):
		'''
		Initializing the bucket details.
		'''
		self.bucket_name = bucket_name
		self.folder = folder

		#create a file for storing marked files.
		if not os.path.exists('marked_files.txt'):
			with open('marked_files.txt', 'w+') as file:
				pass

		#create a folder for downloading files, if it doesn't exists.
		if not os.path.exists('files'):
			os.mkdir('files')

	def mark_read(self, file):
		'''
		Mark the give file as read.
		'''
		with open('marked_files.txt', 'a+') as f:
			
			#store the names of marked files along with the timestamp.
			timestamp = str(datetime.now())
			log = f'{file} {timestamp} \n'
			f.write(log)

	def get_file_list(self):
		'''
		Returns list of all files present inside the given folder.
		'''
		return os.popen(f'gsutil ls -r gs://{self.bucket_name}/{self.folder}/*.json').read().split('\n')

	def get_file(self, filename, path_to_store= 'files/.'):
		'''
		Downloads the given file to specified path and mark it.
		'''
		os.system(f'gsutil cp {filename} {path_to_store}')
		self.mark_read(filename)
		print('File downloaded successfully!')

	def get_previous_files(self):
		'''
		Returns a list of files that were marked and processed.
		'''
		files = []
		with open('marked_files.txt', 'r') as f:
			for line in f:
				file_name = line.split(' ')[0]
				files.append(file_name)
		return files