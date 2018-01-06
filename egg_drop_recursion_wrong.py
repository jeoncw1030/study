# 2017. 12. 05 (화)

def get_drop_count(range_, floor):
    if not floor:
        return
    
    drop_cnt = 0
    drop_points = []
    n_list = range_
    
    
    while True:
        half = int((len(n_list) - 1) / 2)
        drop_cnt += 1
        drop_points.append(n_list[half])

        if floor < n_list[half]:
            n_list = n_list[:half]

        elif floor > n_list[half]:
            n_list = n_list[half + 1:]
        else:
            break
        
    answer = "{} floor : total drop egg '{}' - drop points '{}'"
    answer = answer.format(floor, drop_cnt, drop_points)
    print(answer)

    floor -= 1
    get_drop_count(range_,floor)


if __name__ == '__main__':
    floor = 100
    min_ = 1
    max_ = 100
    range_ = [i for i in range(min_, max_ + 1)] #층수 비교하는 범위

    get_drop_count(range_,floor)