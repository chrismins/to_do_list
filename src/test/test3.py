def getCommonElementList(firstList, secondList):
    result = [item for item in firstList if item in secondList]
    return result


def getUnionList(nlist):
    while len(nlist) > 1:
        list_one = nlist.pop()
        list_two = nlist.pop()
        result = getCommonElementList(list_one, list_two)
        if len(result) > 0:
            nlist.append(result)
    print(nlist[0])


if __name__ == '__main__':
    nlist = [[1, 2, 3, 4], [2, 3, 4], [5, 4, 7, 8, 3]]
    getUnionList(nlist)
