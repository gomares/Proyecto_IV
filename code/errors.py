class GenreNotFound(Exception):
	"""
	Excepción lanzada para errores si el género introducido no se encuentra
	en el enumerado Genre

	Attributes
	----------
	message: str
		Texto explicativo del error.
	"""
	def __init__(self, mesasge="El género no es correcto porque no se encuentra entre los géneros admitidos."):
		self.message = message

