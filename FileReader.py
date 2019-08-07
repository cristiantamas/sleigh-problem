# Method for reading the input license file
# At first, it reads all the elements of the file
# and stores them into an array, then returns the array to be
# used later
# It has an input paramter:
#   - fileName: the file to be read from (by default is set to licenseFile.txt)
def readFromFile(fileName):

    # Main array of data
    licenseData = []

    try:
        with open(fileName) as reader:
            line = reader.readline()

            # Split the string into elements
            results = line.split()

            # Convert the array of strings to array of ints and add it to the main array
            licenseData.extend(list(map(int, results)))
    except:
        print("Error at opening/reading file")
    finally:
        return licenseData