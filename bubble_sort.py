#import copy

def bubble_sort(data):
    #change_data = copy.deepcopy(data)
    ch_len = len(data)-1
    
    for i in range(ch_len):
        for j in range(ch_len-i) :
            if data[j] > data[j+1] :
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

if __name__ == '__main__':
    data = [9, 8, 3, 6, 7]

    print(data) # [9, 8, 3, 6, 7]

    bubble_sort(data)

    print(data) # [3, 6, 7, 8, 9]
    
