def selection_sort(data):
    ch_len = len(data)

    for i in range(ch_len):
        min_index = i #index
        for j in range(i+1, ch_len) :
            if data[min_index] > data[j] :
                min_index = j
        data[min_index], data[i] = data[i], data[min_index]


        
if __name__ == '__main__':
    data = [9, 8, 3, 6, 7]

    print(data) # [9, 8, 3, 6, 7]

    selection_sort(data)

    print(data) # [3, 6, 7, 8, 9]
    
