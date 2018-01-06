def get_drop_count(range_, floor, drop_points):
    drop_cnt = 0
    n_list = range_
    
    while True:
        half = int((len(n_list) - 1) / 2)
        print(half)
        drop_cnt += 1
        drop_points.append(n_list[half])

        if floor < n_list[half]:
            n_list = n_list[:half]
            
        elif floor > n_list[half]:
            n_list = n_list[half + 1:]
        else:
            break
        
    return drop_cnt


if __name__ == '__main__':
    min_ = 1 #1층
    max_ = 100 #100층
    range_ = [i for i in range(min_, max_ + 1)] #층수 비교하는 범위

    for floor in range(max_, 0, -1):
        drop_points = [] #실패할 때마다 해당 층수 기록하는 리스트
        #floor : N층 (계속해서 순서 변함)
        total_drop_count = get_drop_count(range_, floor, drop_points)

        answer = "{} floor : total drop egg '{}' - drop points '{}'"
        answer = answer.format(floor, total_drop_count, drop_points)
        print(answer)