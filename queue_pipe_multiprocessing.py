import multiprocessing


def calc_square(numbers, result, value_obj):
    value_obj.value = 5.67
    for idx,n in enumerate(numbers):
        result[idx] = n*n
    
if __name__=='__main__':
    numbers= [2,3,5]
    result = multiprocessing.Array('i', 3)
    value_obj = multiprocessing.Value('d',0.0)
    
    p= multiprocessing.Process(target= calc_square, args= (numbers,result, value_obj))
    
    
    p.start()
    p.join()
    
    print('result:',result[:])
    
    print(value_obj.value)