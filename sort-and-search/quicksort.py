def swap(list, x, y): 
	list[x], list[y] = list[y], list[x]
def partition(list,left,right,pivot_idx):
	tail_idx = left 
	for i in range(left, right, 1):
		if list[i] < list[pivot_idx]: 
			swap(list, i, tail_idx)	
			tail_idx += 1
	swap(list, tail_idx, pivot_idx)
	return tail_idx	
def quicksort(list, left, right):

	if left < right:
		pivot_idx = right
		pivot_idx = partition(list, left, right, pivot_idx)
		quicksort(list, left, pivot_idx - 1)
		quicksort(list, pivot_idx + 1, right)

list = [10, 3, 1, 50, 2, 4, 29]
quicksort(list, 0, len(list) - 1)
print(list)
