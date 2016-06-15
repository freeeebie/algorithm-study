''' boggle solve 
import sys
def get_next(board, count, target, xcoord, ycoord):
	result = []

	if count == 0: 
		for x in range(5):
			for y in range(5):
				if (board[x][y] == target):
					result.append((x,y))
	else: 
		for x in range(xcoord -1, xcoord + 2):
			for y in range(ycoord -1, ycoord + 2 ):
				if x < 0 or x > 4:
					continue
				if y < 0 or y > 4: 
					continue
				if x == xcoord and y == ycoord:
					continue
				if board[x][y] == target:
					result.append((x,y))
	return result 	

def find_word(board, boardsize, targetword, xcoord, ycoord, count):
	if count == len(targetword): 
		return True

	nextcoords = get_next(board, count, targetword[count], xcoord, ycoord)

	if len(nextcoords) == 0:
		return False
	count += 1
	for nextcoord in nextcoords: 
		result = find_word(board, boardsize, targetword, nextcoord[0], nextcoord[1], count)
		if result == True:
			return True #, count # 왜 이문장이 들어가야 하나? 
	return False

inputcount = sys.stdin.readline()
testcase = int(inputcount) 
board = []
words = []
while(testcase > 0) :
	for _ in range(5): 
		inputraw = list(sys.stdin.readline())
		board.append(inputraw)
	inputcount = sys.stdin.readline()
	wordcount = int(inputcount) 

	for _ in range(wordcount): 
		inputraw = input()
		words.append(inputraw)

	for word in words: 
		count = 0; 
		ret = find_word(board, 5, word, 0, 0, count)

		if ret == False:
			print("%s NO" % word)
		else: 
			print("%s YES" % word)
	del board[:]
	del words[:]
	testcase -= 1
