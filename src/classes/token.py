class Token:
	def __init__(self, token_type, value):
		self.type = token_type
		self.value = value
		self.status = None
		self.is_negative = False

	def __str__(self):
		return "type: {}; value: {}; status: {}; is_negative: {}".format(self.type, self.value, self.status, self.is_negative)

