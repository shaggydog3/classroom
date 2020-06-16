courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                        'title': 'Object-Oriented Python',
                        'prereqs': [{'count': 1,
                                     'title': 'Python Collections',
                                     'prereqs': [{'count':0,
                                                  'title': 'Python Basics',
                                                  'prereqs': []}]},
                                    {'count': 0,
                                     'title': 'Python Basics',
                                     'prereqs': []},
                                    {'count': 0,
                                     'title': 'Setting Up a Local Python Environment',
                                     'prereqs': []}]},
                       {'count': 0,
                        'title': 'Flask Basics',
                        'prereqs': []}]}


def prereqs(data, pres=None):
    pres = pres or set()
    #print("entering loop")
    for pre in data['prereqs']:
        #print("processing data for prereq: {}.  Pres is of type {}".format(pre['title'], type(pres)))
        pres.add(pre['title'])
        pres = prereqs(pre)
    return pres

def prereqs_with_mapping(data, pres=None):
    pres = pres or set()


print(prereqs(courses))