import extractdata


def solve(full_path_instance):
    l, s, b, d, c, q, t  = extractdata.getCourseData(full_path_instance)
    print(l,s,b,q,d,c,t)





if __name__ == "__main__":

    import sys
    full_path_instance = sys.argv[1]
    solve(full_path_instance)



