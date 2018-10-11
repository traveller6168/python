from multiprocessing import Pool 
import queue
import time
import sys

def test(p):
    print ("子进程" , p)
    time.sleep(p)
    if p == 30 :
       return str(p) + 'True'
    else:
       return str(p) + 'False'
if __name__=="__main__": 
  pool = Pool(processes=10)
  q=queue.Queue()
  for i in range(50):
    #print ("主进程:" , i)
    ''' 
     将子进程对象存入队列中。 
    '''
    q.put(pool.apply_async(test, args=(i,)))#维持执行的进程总数为10,当一个进程执行完后添加新进程.
    ''' 
     因为这里使用的为pool.apply_async异步方法,因此子进程执行的过程中,父进程会执行while,获取返回值并校验。 
    '''
  while 1:
    print('大小 ',q.qsize())
    flag = q.get().get()
    print('取出后大小 ',q.qsize())
    print ("子进程返回值：",flag)
    if 'True' in flag:
           pool.terminate() #结束进程池中的所有子进程。
           pool.join()
           sys.exit(1)
    if q.qsize() == 0:
       sys.exit(0)
