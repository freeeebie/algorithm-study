# https://www.careercup.com/question?id=22809662
# use dynamic programming method for counting height

def find_height_node(nodelist, index, heights):
    if heights[index] != -1:
        return heights[index]
    node = nodelist[index]
    if node[0] == -1:    # root node
        return 1
    else:
        height = 1+ find_height_node(nodelist, node[0], heights)
        return height

def find_height(nodelist, N):
    heights = [-1] * N
    maxheights = -1
    for i in range(N):
        heights[i] = find_height_node(nodelist, i, heights)
        if heights[i] > maxheights:
            maxheights = heights[i]

    print("The height of tree is ", maxheights)

find_height([(3,0), (3,1), (3,2), (-1,3), (2,4)], 5)
find_height([(3,0), (0,1), (3,2), (-1,3), (2,4), (4,5), (1,6), (6,7)], 8)
