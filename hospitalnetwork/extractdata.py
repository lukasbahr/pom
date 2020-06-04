import csv
import pandas as pd


def getHospitalData(full_instance_path):
    """
    input: path to csv file containing hospital network data
    output: hospitals - name of hospitals
            cities - name of cities
            h_coord - hospital coordinates
            c_coord - city coordinates
            coord - coordinates [[x_y_h_coordinates], [x_y_c_coordinates]]
            c - cost [[costk1], [costk2], [costk3]]
            b - capacity [[capk1], [capk2], [capk3]]
            closingIncome - closing income {'existing_hospital': closing_income}
            min_size_2 - cities with minimum hospital size 2 [cities]
    """

    hospitals = []
    cities = []
    h_coord, c_coord = []
    c = [[],[],[]]
    b = [[],[],[]]
    closingIncome = []
    minSize2 = []

    skipString = {'# hospitals: loc_id', '# existing hospitals: loc_id', '# cities: loc_id', '# cities with minimum hospital size 2: loc_id'}
    hospitalData = []
    existingHospitalData = []
    cityData = []
    cityMinData = []
    with open(full_instance_path, 'r') as read_obj:
        csv_dict_reader = csv.reader(read_obj, delimiter=',')
        for row in csv_dict_reader:
            row = list(filter(None, row))
            if row[0] in skipString:
                continue
            elif (len(row) == 9):
                hospitalData.append(row)
            elif (len(row) == 2):
                existingHospitalData.append(row)
            elif (len(row) == 3):
                cityData.append(row)
            elif (len(row) == 1):
                cityMinData.append(row)

    for entry in hospitalData:
        hospitals.append(entry[0])
        h_coord.append((int(entry[1]), int(entry[2])))
        c[0].append(int(entry[3]))
        c[1].append(int(entry[4]))
        c[2].append(int(entry[5]))
        b[0].append(int(entry[6]))
        b[1].append(int(entry[7]))
        b[2].append(int(entry[8]))

    for idx in range(len(hospitals)):
        for entry in existingHospitalData:
            if int(entry[0].strip('c')) == idx:
                closingIncome.append(entry(1))
            else:
                closingIncome.append(0)

    for entry in cityData:
        cities.append(entry[0])
        c_coord.append((int(entry[1]), int(entry[2])))

    for entry in cityMinData:
        idx = int(entry[0].strip('c'))
        minSize2.append(idx)


    return hospitals, cities, h_coord, c_coord, c, b, g, minSize2


