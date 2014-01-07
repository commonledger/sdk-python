from .http_client import HttpClient

# Assign all the api classes
from .api.accounts import Accounts

class Client():

	def __init__(self, auth = {}, options = {}):
		self.http_client = HttpClient(auth, options)

	# Manages data relating to the Chart of Accounts
	#
	# account_id - The account UUID
	def accounts(self, account_id):
		return Accounts(account_id, self.http_client)

