import random

class GeneratorAlgorithm:
	def generate_CPF(self):
		self.build_CPF = []
		for i in range(9):
			self.build_CPF.append(random.randint(0, 9))

		for i in range(2):
			self.build_CPF.append(self._digit())

		return self._build_string()
		
	def _digit(self):
		sum = 0
		index = len(self.build_CPF) + 1
		for i in range(len(self.build_CPF)):
			sum += self.build_CPF[i] * index
			index -= 1
		return self._verify_sum(sum)

	def _verify_sum(self, sum):
		if (sum % 11) < 2:
			return 0
		else:
			return 11 - (sum % 11)

	def _build_string(self):
		self.CPF = ""
		self.build_CPF.insert(3, ".")
		self.build_CPF.insert(7, ".")
		self.build_CPF.insert(11, "-")

		for i in range(len(self.build_CPF)):
			self.CPF += str(self.build_CPF[i])

		return self.CPF