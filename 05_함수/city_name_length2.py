def char_len_search(l):
    # input: list(citys)
    # output: int(8), int(5)
    # functions:
    # * list(l)를 받아서 글자수가 큰 값, 글자수가 작은 값 출력
    # print(l)
    nlist = [len(i) for i in l]
    return max(nlist), min(nlist)


def char_list(l, max, min):
    # input: list(l), int(max), int(min)
    # output: list(longlist), list(shortlist)
    # functions:
    # * list(l), max, min 값을 받아서 가장 긴 이름의 list와 가장 작은 이름의 list를 반환한다.
    # print(l, max, min)
    llist = []
    slist = []
    for i in l:
        if max == len(i):
            llist.append(i)
        if min == len(i):
            slist.append(i)
    return llist, slist


def outform(llist, slist):
    # input: list(llist), list(slist)
    # output: None
    # (출력폼)
    # Long Name City: suncheon
    # Short Name City: seoul, kimpo, pusan
    print("Long Name City :", ', '.join(llist))
    print("Short Name City:", ', '.join(slist))


def main():
    citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan', 'gwangju', 'ulsan', 'daegu']

    # 1) 글자수가 큰 값, 글자수가 작은 값 찾기
    maxlen, minlen = char_len_search(citys)

    # 2) 큰 글자수 list, 작은 글자수 list 출력하기
    longlist, shortlist = char_list(citys, maxlen, minlen)

    # 3) 출력 폼 맞추기
    outform(longlist, shortlist)


if __name__ == '__main__':
    main()
