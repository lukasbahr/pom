import re


def getCourseData(full_path_instance):
    """
    input:
    output:
    """

    isCourses = False
    isRooms  = False
    isCurricula = False
    isUnavailabilityConstraints = False

    l = {} # number of lectures for each course k e.g. {'c0008': 2}
    s = {} # number of students participating a course k e.g. {'c0006: 20'}
    b = {} # capacity of students of a room r e.g. {'DS1': 12}
    d = {} # number of different days a courses k have to take place e.g. {'c0004': 3}. Course c0004 has to take place on 3 different days i
    c = {} # course k taught by teacher e.g. {'c0005': 't004'}. Course c0005 taught by teacher t004
    q = {} # couses k of the curiccula p {'q00': ('c0023', 'c002')}. Curricula q00 consist of courses c0023 and c002
    t = {} # unavailability, courses k cannot be take place at (i,j) i being the day and j being the timeslot e.g. {'c0003':(2,3)}. Course c0003 cannot take place on day 2 with timeslot 3



    with open(full_path_instance, 'r') as df:
        for line in df:
            if line.strip():

                if line.find("COURSES") > -1:
                    isCourses = True
                    isRooms = False
                    isCurricula = False
                    isUnavailabilityConstraints = False
                    continue

                elif line.find("ROOMS") > -1:
                    isRooms = True
                    isCourses = False
                    isCurricula = False
                    isUnavailabilityConstraints = False
                    continue

                elif line.find("CURRICULA") > -1:
                    isCurricula = True
                    isCourses = False
                    isRooms = False
                    isUnavailabilityConstraints = False
                    continue

                elif line.find("UNAVAILABILITY_CONSTRAINTS") > -1:
                    isUnavailabilityConstraints = True
                    isCourses = False
                    isRooms = False
                    isCurricula = False
                    continue

                elif line.find("END.") > -1:
                    break

                content = re.split("  | |\t", line)

                if isCourses:
                    l[content[0]] = int(content[2])
                    s[content[0]] = int(content[4].replace("\n", ""))
                    d[content[0]] = int(content[3])
                    c[content[0]] = content[1]

                elif isRooms:
                    b[content[0]] = int(content[1].replace("\n", ""))

                elif isCurricula:
                    content.pop()
                    q[content[0]] = tuple(content[2:None])


                elif isUnavailabilityConstraints:
                    print(content)
                    if not content[0] in t:
                        t[content[0]] = [tuple((int(content[1]),
                            int(content[2].replace("\n", ""))))]
                    else:
                        t[content[0]].append(tuple((int(content[1]),
                            int(content[2].replace("\n", "")))))


    return l, s, b, d, c, q, t









