def reverse(input_list ,end =0 ,start=0):
	if end==0:
		end = len(input_list)
	if start < end:
		input_list[start],input_list[end-1] = input_list[end-1],input_list[start]
		reverse(input_list,end-1,start+1)
	return input_list


s =[1,2,3,4,2,3,4,3]

x= reverse(s)

print(x)