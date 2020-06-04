from gurobi import *
import extractdata


def solve(full_instance_path):

    hospitals, cities, coord, c, b, g, minSize2 = extractdata.getHospitalData(full_instance_path)


    #  return model

if __name__ == "__main__":

    import sys

    path = sys.argv[1]
    if isinstance(path, str):
        solve(path)
    else:
        print("Please enter valid string.")

