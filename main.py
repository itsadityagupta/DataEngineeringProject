from fetch_data import DataRead
from config import BUCKET_NAME, FOLDER
from gremlin_python.driver import client
from read_json import ReadJson
from config import initialize_gremlin_client
from config import insert_vertices, insert_edges

print('-------------------Program Started---------------------------')

#get files present in the given folder of the given bucket
print('Reading files from the bucket...')
read = DataRead(BUCKET_NAME, FOLDER)
files = read.get_file_list()[:-1]
print('Files Read!')

print('Downloading Files...')
#get the already marked files
marked_files = read.get_previous_files()
new_files = []
#download the files which are not marked and mark them
for file in files:
  if file not in marked_files:
    read.get_file(file)
    new_files.append(file)

if len(new_files) != 0:

	print('Files Downloaded!')

	#initializing a gremlin client for executing queries on the database.
	print('Initialising client...')
	gremlin_client = initialize_gremlin_client()
	print('Client initialised!')

	print('Querying DataBase...')
	for file in new_files:
		file_path = 'files/'+file.split('/')[-1]
		compute = ReadJson(file_path)
		compute.compute_queries()
		insert_vertices(gremlin_client, compute.nodes)
		insert_edges(gremlin_client, compute.edges)

	print('Querying Finished!')
	
else:
	print('No New Files Found!')
	
print('-------------------------Program Terminated!--------------------')