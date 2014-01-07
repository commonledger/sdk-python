# Collection of different tax rates and their codes
#
# tax_id - The tax UUID
class Tax():

	def __init__(self, tax_id, client):
		self.tax_id = tax_id
		self.client = client

	# Add a new tax rate
	# '/core.tax/add' POST
	#
	# organisation_id - The UUID of the organisation this tax rate belongs to
	# name - The name of this tax rate
	# type - The tax type (tax code)
	# display_rate - The rate to display this tax at
	# effective_rate - The rate that gets applied for this tax
	def add(self, organisation_id, name, type, display_rate, effective_rate, options = {}):
		body = options['body'] if 'body' in options else {}
		body['organisation_id'] = organisation_id
		body['name'] = name
		body['type'] = type
		body['display_rate'] = display_rate
		body['effective_rate'] = effective_rate

		response = self.client.post('/core.tax/add', body, options)

		return response

	# View a tax rate
	# '/core.tax/view/:tax_id' GET
	#
	def view(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/core.tax/view/' + self.tax_id + '', body, options)

		return response

	# Update an existing tax rate
	# '/core.tax/update/:tax_id' POST
	#
	# organisation_id - The UUID of the organisation this tax rate belongs to
	# name - The name of this tax rate
	# type - The tax type (tax code)
	# display_rate - The rate to display this tax at
	# effective_rate - The rate that gets applied for this tax
	def update(self, organisation_id, name, type, display_rate, effective_rate, options = {}):
		body = options['body'] if 'body' in options else {}
		body['organisation_id'] = organisation_id
		body['name'] = name
		body['type'] = type
		body['display_rate'] = display_rate
		body['effective_rate'] = effective_rate

		response = self.client.post('/core.tax/update/' + self.tax_id + '', body, options)

		return response

