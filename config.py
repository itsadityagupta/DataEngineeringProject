from gremlin_python.driver import client

# google cloud bucket details
BUCKET_NAME = 'data-engineering-intern-data'
FOLDER = 'graph-data'

#cosmosdb database details
ENDPOINT = ''
DATABASE = ''
COLLECTION = ''
PRIMARY_KEY = ''

# utility functions
def insert_vertices(gremlin_client, nodes):
	'''
	Inserts nodes in the database.
	'''
	succ = 0
	failed = 0
	print('Inserting Nodes...')

	for node in nodes:
		callback = gremlin_client.submitAsync(node)
		if callback.result() is not None:
			succ += 1
		else:
			failed += 1
	print('Nodes Inserted.')
	print(f'Successfull: {succ}; Failed: {failed}')

def insert_edges(gremlin_client, edges):
	'''
	Inserts relationships in the database.
	'''
	succ = 0
	failed = 0
	print('Inserting Edges...')

	for edge in edges:
		callback = gremlin_client.submitAsync(edge)
		if callback.result() is not None:
			succ += 1
		else:
			failed += 1
	print('Edges Inserted.')
	print(f"Successful: {succ}; Failed: {failed}")

def initialize_gremlin_client():
	'''
	Initializes a gremlin client to execute queries on.
	'''
	return client.Client(ENDPOINT, 'g', username="/dbs/" + DATABASE + "/colls/" + COLLECTION, password=PRIMARY_KEY )
