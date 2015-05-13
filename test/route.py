def route(regx):
	def _fun(func):
		def _(*args, **kwargs):
			res = func(*args, **kwargs)
			return res
		return _
	return _fun


