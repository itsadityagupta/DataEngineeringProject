import json

class ReadJson:
	def __init__(self, file_path):
		'''
		Initialise the instance with file_path
		'''
		self.file_path = file_path

	def load_file(self):
		'''
		load the file in the memory
		'''
		with open(self.file_path, 'r') as f:
			self.file_content = json.load(f)

	def vertex_query(self, data):
		'''
		Returns the gremlin query equivalent of "add a node"
		'''
		return f'g.addV("{data["Label"][0]}")'

	def id_query(self, data):
		'''
		Returns the gremlin query equivalent of "add an id"
		'''
		return f'.property("id", "{data["IdUnique"]}")'

	def property_query(self, data):
		'''
		Returns the gremlin query equivalent of adding all the mentioned properties.
		'''
		query = []

		for property_key, property_value in data['Property'].items():
			query.append(f'.property("{property_key}", "{property_value}")')

		return "".join(query)

	def from_vertex_query(self, data):
		'''
		Returns the gremlin query equivalent of "right node of an edge".
		'''
		return f'g.V("{data["FromLabel"]}")'

	def to_vertex_query(self, data):
		'''
		Returns the gremlin query quivalent of "left node of an edge".
		'''
		return f'.to(g.V("{data["ToLabel"]}"))'

	def relationship_query(self, data):
		'''
		Returns the gremlin query equivalent of "add an edge".
		'''
		return f'.addE("{data["Type"]}")'

	def label_query(self, data):
		'''
		Returns the gremlin query equivalent of adding all the labels as a single string.
		'''
		if len(data['Label']) < 2:
			return ""

		label = " ".join([label for label in data['Label'][1:]])

		return f'.property("label", "{label}")'

	def compute_queries(self):
		'''
		Computes the gremlin queries of nodes and relationships from the file content.
		'''
		#load the file contents.
		self.load_file()

		#lists to store queries for nodes and edges.
		self.nodes = []
		self.edges = []

		for data in self.file_content:

			if data['Kind'] == 'node':
				#computing different parts of a query to create a node.
				vertex_part = self.vertex_query(data)
				id_part = self.id_query(data)
				property_part = self.property_query(data)
				label_part = self.label_query(data)
				
				self.nodes.append(vertex_part+id_part+property_part+label_part)
				
			else:

				#computing different parts of a query to create an edge.
				from_vertex = self.from_vertex_query(data)
				to_vertex = self.to_vertex_query(data)
				relationship = self.relationship_query(data)
				id_part = self.id_query(data)

				self.edges.append(from_vertex+relationship+to_vertex+id_part)