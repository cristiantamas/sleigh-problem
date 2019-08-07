# Main program

from Node import Node
from FileReader import readFromFile

def main():
    # Main node of the tree
    root = Node()

    # Data to be parsed from the file
    licenseData = readFromFile("licenseFile.txt")

    # Build the tree
    buildNode(licenseData, root)

    # We parse the tree and calculate the full metadata entries sum
    metadataSum = parseTree(root)

    # Calculate the value for the root node - part two of the problem
    rootValue = parseTreeWithIndexes(root)

    print("Metadata sum: " + str(metadataSum))
    print("Root value: " + str(rootValue))



# Function that parses the given list
# It extracts the number of children and metadata entries
# and it calls itself recursively for every child of the current node.
# After that, it parses the remaining metadata entries (if any) and retains
# them to be used later
# Input parameters:
#   - dataList: list of remaining children and metadata entries
#   - node: the current node
def buildNode(dataList, node):
    node.numberOfChildren = dataList[0]
    node.metadataEntries = dataList[1]

    # Cut first two elements - we don't need them anymore
    dataList = dataList[2:]

    # Continue creating the tree
    for i in range(0, node.numberOfChildren):
        # Create a new child
        child = Node()

        # Call the function recursively for the new child
        dataList = buildNode(dataList, child)

        # Add the child to the list
        node.childrenList.append(child)

    # Parse the metadata entries for the current node and retain them
    for i in range(0, node.metadataEntries):
        node.metadataValues.append(dataList[0])
        dataList = dataList[1:]

    # List of remaining data to be used further
    return dataList


# Function used for parsing the tree in a recursive manner.
# For each child of the current node, add the sum to a variable
# auxSum that will be returned together with the metadata sum of the
# current node
def parseTree(node):

    auxSum = 0
    if node.numberOfChildren == 0:
        return sum(node.metadataValues)

    for child in node.childrenList:
        auxSum = auxSum + parseTree(child)

    return sum(node.metadataValues) + auxSum


# Function used for parsing the tree in a recursive manner.
# For each child of the current node, if it has no children
# return the metadata sum of that node
# If the node has children, parse the metadata entries and
# call the function recursively for each child with an index
# in the metadata entries list
def parseTreeWithIndexes(node):

    auxSum = 0
    if node.numberOfChildren == 0:
        return sum(node.metadataValues)

    for index in node.metadataValues:
        if index > len(node.childrenList):
            continue
        auxSum = auxSum + parseTreeWithIndexes(node.childrenList[index-1])

    return auxSum


if __name__ == '__main__':
    main()