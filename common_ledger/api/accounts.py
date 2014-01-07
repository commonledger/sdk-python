# Manages data relating to the Chart of Accounts
#
# account_id - The account UUID
class Accounts():

	def __init__(self, account_id, client):
		self.account_id = account_id
		self.client = client

	# Creates a new account in the chart of accounts
	# '/core.account/add' POST
	#
	# organisation_id - The organisation the account belongs to
	# account_number - The account code
	# name - The account name
	# classification - The account classification
	# type - The type of classification for the account
	# tax - The tax code that applies to the account
	# currency - The currency code that applies to the account
	def add(self, organisation_id, account_number, name, classification, type, tax, currency, options = {}):
		body = options['body'] if 'body' in options else {}
		body['organisation_id'] = organisation_id
		body['account_number'] = account_number
		body['name'] = name
		body['classification'] = classification
		body['type'] = type
		body['tax'] = tax
		body['currency'] = currency

		response = self.client.post('/core.account/add', body, options)

		return response

	# 
	# '/core.account/view/:account_id' GET
	#
	def view(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/core.account/view/' + self.account_id + '', body, options)

		return response

