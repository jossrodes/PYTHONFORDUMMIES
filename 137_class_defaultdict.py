class defaultdict(dict):
	def __init__(self, default=None):
		dict.__init__(self)
		self.default = default
	def __getitem__(self, key):
		try:
			return dict.__getitem__(self, key)
		except KeyError:
			return self.default