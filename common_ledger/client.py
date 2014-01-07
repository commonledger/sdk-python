from .http_client import HttpClient

# Assign all the api classes
from .api.accounts import Accounts
from .api.tax import Tax
from .api.journals import Journals

class Client():

	def __init__(self, auth = {}, options = {}):
		self.http_client = HttpClient(auth, options)

	# Manages data relating to the Chart of Accounts
	#
	# account_id - The account UUID
	def accounts(self, account_id):
		return Accounts(account_id, self.http_client)

	# Collection of different tax rates and their codes
	#
	# tax_id - The tax UUID
	def tax(self, tax_id):
		return Tax(tax_id, self.http_client)

	# Manages journal entries and journal lines
	#
	# journal_id - The journal entry UUID
	def journals(self, journal_id):
		return Journals(journal_id, self.http_client)

