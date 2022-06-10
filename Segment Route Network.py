'''
Segment Road Network

Description: Program that takes a starting point value, a number of segments, a unique ID, and a Object ID. Based on the number of segments the program divides a route into quarter segments from the starting point.

Inputs: CSV/xlsx dataset

Field Inputs: starting point value, a number of segments, a unique ID, and a Object ID.

Output: An xlsx file that contains the new starts and stops for the new segments of the orginal route file.

Utilization: To run this script please have a CSV file that contains a Object ID, Route name, a start and end marker for each route, and a number of segments needed (Segments = End marker/Segmentation value).
After data is properly prepared please run the script (f5) or press run on the Idle ribbon. Enter in the correct information in the prompt and press enter each time. You should receive a None after the tool is complete
the output file will be found at the output location.

Time/Space Complexity: Program runs in o(n^2). The larger the input the dataset the time to process all the data will grow exponetiallty. 
'''

import pandas as pd

inputFile = input('Enter in file path for csv (File must be a CSV): ')

inputSegments = input('Enter field name for column containg the total number of segments ([Segments = Route End Point/Segmentation value] *Segment must be rounded up to the nearest whole number): ')

inputBegin = input('Enter field name for column containg Route Begin markers:')

inputOID = input('Enter field name for column containing Unique Object ID (must be integer value): ')

inputRoute = input('Enter field name for column containing Route names: ')

inputSegValue = input('Enter the value used to segment a road file (Example: .25 mile segment): ')

outputLocation = input('Enter output location path plus name followed by .xlsx (Folders\Desktop\FileExample.xlsx): ')

def segment(inputFile, inputSegments, inputBegin, inputOID, inputRoute, outputLocation):

    #input file location
    f = (r'%s' %inputFile)

    #empty dictionary
    d = {}

    #reads csv
    dl = pd.read_csv(f)

    #list of all number of segments (Segments = Route End Marker/Segmenation value)
    nList = dl[str(inputSegments)].tolist()

    #List of all Begin markers
    cList = dl[str(inputBegin)].tolist()

    #List of all Object IDs
    IDList = dl[str(inputOID)].tolist()
    
    #List of Route names
    rList = dl[str(inputRoute)].tolist()

    #for every value in range of the file
    for y in range(len(nList)):

        #n equals the int value of the element at index [y]
        n = int(nList[y])

        #ID equals the element of the OID list at element [y]
        ID = IDList[y]

        #C equals the Begin marker list at element [y]
        c = cList[y]

        #r equals the route name list at element [y]
        r = rList[y]

        #for the (i)th number in range of the current value of n 
        for i in range(n):

            #c equals itself + the segment value for each iteration of i in range of n
            c += float(inputSegValue)

            #UID makes a unique ID by attaching ID and i
            UID = (str(ID) + '.' + str(i))

            #Hashes values to the UID(key) 
            d[UID] = [(r),(c - float(inputSegValue)),(c)]

    #Pandas data frame of the dictionary object (d) organized by colums
    df = pd.DataFrame(d).T

    #Sets data frame columns names
    df.columns = ['Route', 'Start Segment', 'End Segment']

    #Converts and exports data frame to output location
    df.to_excel(r'%s'%outputLocation)

print(segment(inputFile, inputSegments, inputBegin, inputOID, inputRoute, outputLocation))

