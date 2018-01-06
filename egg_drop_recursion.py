# 2017. 12. 16 (토)

def get_drop_count(range_, floor, flag):
    if not floor:
        return

    if not flag:
        drop_cnt = 0
        drop_points = []
        n_list = range_


    half = int((len(n_list) - 1) / 2)
    drop_cnt += 1
    print(drop_cnt)
    drop_points.append(n_list[half])
    print(drop_points)
    if floor < n_list[half]:
        n_list = n_list[:half]
        print(half)
        get_drop_count(range_,floor, flag+1)


    elif floor > n_list[half]:
        n_list = n_list[half + 1:]
        print(half)
        get_drop_count(range_,floor,flag+1)
    
    else:
        answer = "{} floor : total drop egg '{}' - drop points '{}'"
        answer = answer.format(floor, drop_cnt, drop_points)
        print(answer)
        flag += 1
        floor -= 1
        return
        

if __name__ == '__main__':
    floor = 100
    flag = 0
    min_ = 1
    max_ = 100
    range_ = [i for i in range(min_, max_ + 1)] #층수 비교하는 범위

    get_drop_count(range_,floor,flag)