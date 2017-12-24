import sys


from pyhive import hive
from TCLIService.ttypes import TOperationState

def pyhiveexesql(sql):
    print (sql)
    cursor = None
    try:
       cursor = hive.connect(host='', port=10000, username='').cursor()
       cursor.execute(sql, async=True)
       status = cursor.poll().operationState
       while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
          logs = cursor.fetch_logs()
          for message in logs:
             print (message)
             # If needed, an asynchronous query can be cancelled at any time with:
             # cursor.cancel()
             status = cursor.poll().operationState
       #print (cursor.fetchall())
       print("测试连接HIVE库，并输出结果！")
       conn_result = cursor.fetchall()
       var_len = len(conn_result)
       #print(var_len,conn_result)
       var = 0
       while var < var_len:
           print(conn_result[var])
           var += 1

    except Exception:
        print ('%s' % (message))
    finally:
        cursor.close()

if __name__ == '__main__':
    pyhiveexesql("SELECT * FROM new_test LIMIT 2")
    pyhiveexesql("set hive.exec.dynamic.partition.mode=nonstrict")

