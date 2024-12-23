movies = {
    '파묘': [23.6, 5.5, 11914768],
    '범죄도시4': [20.6, 8.8, 11502779],
    '인사이드 아웃 2': [15.6, 8.8, 8799013],
    '베테랑2': [10.8, 5.3, 7525302]
}

print(movies)

# 파묘의 관객 수는?
print(movies['파묘'][2])

# 평점이 8.8인 영화 제목은?
result = []
for i in movies:
    if movies[i][1] == 8.8:
        result.append(i)

print(result)
