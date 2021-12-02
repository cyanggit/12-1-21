def list_counter(start, count):

    list1 = [0] * count
    counter = 0

    if start % 2 != 0:
        start += 1

    for i in range(len(list1)):

        list1[i] = start + counter

        counter += 2

    print(list1)

list_counter(5, 7)