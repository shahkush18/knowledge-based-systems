import csv

input_file = csv.DictReader(open('movies_new.dat','rb'))

dict_list = []


def printMovies(theList):


    for line in input_file:
        dict_list.append(line)
        id = int(line["id"])
        for z in theList:
            if id == z:
                print(line["name"] +"---" + line["genre"])
