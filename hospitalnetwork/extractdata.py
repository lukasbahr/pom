import csv

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
            g - closing income
            citiesSpecial - cities with minimum hospital size 2 [cities]
    """

    hospitals = []
    cities = []
    h_coord = []
    c_coord = []
    c = [[],[],[]]
    b = [[],[],[]]
    g = []
    citiesSpecial = []

    skipString = {'# hospitals: loc_id', '# existing hospitals: loc_id', '# cities: loc_id', '# cities with minimum hospital size 2: loc_id'}

    with open(full_instance_path, 'r') as read_obj:
        csv_dict_reader = csv.reader(read_obj, delimiter=',')
        for row in csv_dict_reader:
            row = list(filter(None, row))
            if row[0] in skipString:
                continue
            elif (len(row) == 9):
                hospitals.append(row[0])

                g.append(0)

                h_coord.append((int(row[1]), int(row[2])))

                c[0].append(int(row[3]))
                c[1].append(int(row[4]))
                c[2].append(int(row[5]))

                b[0].append(int(row[6]))
                b[1].append(int(row[7]))
                b[2].append(int(row[8]))

            elif (len(row) == 2):
                g[int(row[0].strip('h'))-1] = int(row[1])

            elif (len(row) == 3):
                cities.append(row[0])
                c_coord.append((int(row[1]), int(row[2])))

            elif (len(row) == 1):
                idx = int(row[0].strip('c'))
                citiesSpecial.append(idx-1)

    return hospitals, cities, h_coord, c_coord, c, b, g, citiesSpecial


