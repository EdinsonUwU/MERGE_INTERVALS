def merge_intervals(intervals):
    first_number = None
    second_number = None
    interval = None
    for i in intervals:
        if (first_number == None) and (second_number == None):
            first_number = i[0]
            second_number = i[1]
            interval = i
            continue
        else:
            if (second_number+1) >= i[0]:
              intervals.remove(interval)
              intervals.remove(i)
              intervals.insert(0,(first_number,max(i[1],second_number)))
              interval = (first_number,max(i[1],second_number))
              second_number = max(i[1],second_number)
              intervals.insert(0,(None,None))
              continue
            else:
              first_number = i[0]
              second_number = i[1]
              interval = i
    return list(filter(((None,None)).__ne__, intervals))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(merge_intervals([(1, 4), (2, 6), (8, 10), (8, 11), (12, 19)]))
    #assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)], "First"
    #assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    #assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)], "Third"
