# Class to store data for each node
# Elements in the class:
#   - numberOfChildren: Number of children to be read
#   - metadataEntries: Metadata entries - to be added to the total sum
#   - childrenList[]: list of children of the node (Node type objects)
#   - metadataValues[]: list of metadataValues
class Node:

    # Constructor with paramters
    #   numberOfChildren - Number of children to be read
    #   metadataEntries - Metada entries - to be added to the total sum
    def __init__(self, numberOfChildren: int = 0, metadataEntries: int = 0):

        self.numberOfChildren = numberOfChildren
        self.metadataEntries = metadataEntries
        self.childrenList = []
        self.metadataValues = []
