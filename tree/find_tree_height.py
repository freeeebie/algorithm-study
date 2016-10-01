# https://www.careercup.com/question?id=22809662
# use bfs method for counting height

def find_height(nodelist, N):
    rootnode = None
    for node in nodelist:
        if node[0] == -1:
            rootnode = node
            nodelist.remove(node)
            break
    queue = []
    queue.append(rootnode)
    height = 0
    while(queue):
        queuelen = len(queue)
        for _ in range(queuelen):
            parendnode = queue.pop(0)
            for node in nodelist:
                if parendnode[1] == node[0]:
                    queue.append(node)
                    nodelist.remove(node)
        height += 1

    print("The height of tree is ", height)

find_height([(3,0), (3,1), (3,2), (-1,3), (2,4)], 5)
find_height([(3,0), (0,1), (3,2), (-1,3), (2,4), (4,5), (1,6), (6,7)], 8)
