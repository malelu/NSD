
def main():
	file = open('graph1.txt', 'r')
	totalNodes = 0
	listNodes = []

	rptNodes = file.read().split()

	for node in rptNodes:
		totalNodes = countNumberNodes(node, listNodes, totalNodes)
	print (totalNodes)
	file.close()


def countNumberNodes (node, listNodes, totalNodes):
	"""Calculates the number of nodes in a graph"""
	if node not in listNodes:
		listNodes.append(node)
		totalNodes = totalNodes + 1
	return totalNodes;

if __name__ == "__main__":
	main()
