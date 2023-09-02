from  multiprocessing import Pool
import time 

def  f(n):
    return n*n


if __name__ == "__main__":
    
    t1 = time.time()
    
    p = Pool(processes = 3)
    
    result = p.map(f, [1,2,3,4,5])
    t1 = time.time()
    for n in  result:
        print(n)
        
    print(f"timed is {time.time()-t1})")