from ..error import ClientError
from .response_handler import ResponseHandler

# ErrorHanlder takes care of selecting the error message from response body
class ErrorHandler():

	@staticmethod
	def check_error(response, *args, **kwargs):
		code = response.status_code
		typ = response.headers.get('content-type')

		if code in range(500, 600):
			raise ClientError('Error ' + str(code), code)
		elif code in range(400, 500):
			body = ResponseHandler.get_body(response)
			message = ''

			# If HTML, whole body is taken
			if isinstance(body, str):
				message = body

			# If JSON, a particular field is taken and used
			if typ.find('json') != -1 and isinstance(body, dict):
				if 'status' in body:
					message = body['status']
				else:
					message = 'Unable to select error message from json returned by request responsible for error'

			if message == '':
				message = 'Unable to understand the content type of response returned by request responsible for error'

			raise ClientError(message, code)
