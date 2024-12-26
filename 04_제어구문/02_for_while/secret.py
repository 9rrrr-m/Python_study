while True:
    passwd = int(input("비밀번호 입력: "))
    if passwd == 3415:
        print("맞았습니다. 현관문이 열렸습니다.")
        break
    else:
        print("틀렸습니다. 다시 입력하세요.\n")
