orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]


def hello_world(orbits):
    new_list = []
    for i in orbits:
        new_list.append(sum(list(i)))
    #print(max(new_list))
    for i in orbits:
        if sum(list(i)) == max(new_list):
            print(list(i))


hello_world(orbits)