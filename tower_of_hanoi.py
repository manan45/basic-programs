def tower_of_hanoi(no_of_disk, beg, aux, end):
	if no_of_disk == 1 :
		print(beg + "->" + end)
	else:
		tower_of_hanoi(no_of_disk-1,beg,end,aux)
		print(beg + "->" + end)
		tower_of_hanoi(no_of_disk-1,aux,beg,end)
	return None


tower_of_hanoi(3,"a", "b", "c")
