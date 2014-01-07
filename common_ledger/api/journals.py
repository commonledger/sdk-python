# Manages journal entries and journal lines
#
# journal_id - The journal entry UUID
class Journals():

	def __init__(self, journal_id, client):
		self.journal_id = journal_id
		self.client = client

	# Add a new journal entry
	# '/core.journal/add' POST
	#
	# organisation_id - The UUID of the organisation this journal entry belongs to
	# journal_number - The journal number this journal entry belongs to
	# journal_type - The type of journal entry this is
	# datetime - The timestamp this journal entry was recorded
	# notes - Any notes this journal entry has
	# lines - An array of journal lines that make up this journal entry
	def add(self, organisation_id, journal_number, journal_type, datetime, notes, lines, options = {}):
		body = options['body'] if 'body' in options else {}
		body['organisation_id'] = organisation_id
		body['journal_number'] = journal_number
		body['journal_type'] = journal_type
		body['datetime'] = datetime
		body['notes'] = notes
		body['lines'] = lines

		response = self.client.post('/core.journal/add', body, options)

		return response

	# View a journal entry
	# '/core.journal/view/:journal_id' GET
	#
	def view(self, options = {}):
		body = options['query'] if 'query' in options else {}

		response = self.client.get('/core.journal/view/' + self.journal_id + '', body, options)

		return response

	# Add a new journal entry
	# '/core.journal/update/:journal_id' POST
	#
	# organisation_id - The UUID of the organisation this journal entry belongs to
	# journal_number - The journal number this journal entry belongs to
	# journal_type - The type of journal entry this is
	# datetime - The timestamp this journal entry was recorded
	# notes - Any notes this journal entry has
	# lines - An array of journal lines that make up this journal entry
	def update(self, organisation_id, journal_number, journal_type, datetime, notes, lines, options = {}):
		body = options['body'] if 'body' in options else {}
		body['organisation_id'] = organisation_id
		body['journal_number'] = journal_number
		body['journal_type'] = journal_type
		body['datetime'] = datetime
		body['notes'] = notes
		body['lines'] = lines

		response = self.client.post('/core.journal/update/' + self.journal_id + '', body, options)

		return response

