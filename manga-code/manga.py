class Manga:
	def __init__(self, name, description, genre, num_capitulos, mangaka):
		self._name = name
		self._description = description
		self._genre = genre
		self._num_capitulos = num_capitulos
		self._mangaka = mangaka

	def get_name(self):
		return self._name

	def get_description(self):
		return self._description

	def get_genre(self):
		return self.genre

	def get_num_capitulos(self):
		return self._num_capitulos

	def get_mangaka(self):
		return self._mangaka