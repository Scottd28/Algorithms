'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

[YOUR NAMES GO HERE]
Jack Brinkman
Scott R
'''

import sys
import csv
from http.cookiejar import unmatched


class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]

            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)

            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 

        # print(self.hospitalsMappings)
        # print(self.residentsMappings)
    # print out the stable match
    def reportMatches(self):
        return self.matches
            
    # follow the chart described in the lab to find the stable match
    def runMatch(self):
        '''
        It is suggested you use the debugger or similar output statements
        to determine what the contents of the data structures are
        '''
        while self.unmatchedHospitals:
            hospital = self.unmatchedHospitals.pop(0)
            # CA
            residentAccepts = False
            residents = self.hospitalsMappings[hospital][:]
            while not residentAccepts:

                # Doris, Charlie, Alex, Barbara
                resident = residents.pop(0)
                # Doris
                if resident in self.unmatchedResidents:
                    self.matches[resident] = hospital
                    self.unmatchedResidents.remove(resident)

                    residentAccepts = True
                else:
                    rPriority = self.residentsMappings[resident].index(hospital)
                    hPriority = self.hospitalsMappings[hospital].index(resident)
                    if hPriority > rPriority:
                        prevHospital = self.matches[resident]
                        self.unmatchedHospitals.append(prevHospital)
                        self.matches[resident] = hospital
                        self.unmatchedHospitals.remove(hospital)
                        residentAccepts = True

                    else:
                        self.residentsMappings[resident].remove(hospital)














if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    # report the matches
    match.reportMatches()
    print(match.reportMatches())



