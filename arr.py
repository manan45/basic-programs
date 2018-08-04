class ArrayRotation(object):
	"""docstring for ArrayRotation"""
	def rotation(self, array, size_of_array, no_of_rotations):
			for i in range(no_of_rotations):
				new_array = self.rotation_by_one(array, size_of_array)
			return new_array

	def rotation_by_one(self, array, size_of_array):
		temp = array[0]
		for i in range(1,size_of_array):
			array[i-1] = array[i]
		array[size_of_array-1]=temp
		return array

	def printArray(self, arr, size_of_array):
		for i in range(size_of_array):
			print(array[i],end=" ")
		return None

array = [1,2,3,4,5,6]

rotated_array = ArrayRotation().rotation(array,6,2)
print(rotated_array)