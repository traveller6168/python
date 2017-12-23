import sys


from pyhive import hive
from TCLIService.ttypes import TOperationState

def pyhiveexesql(sql):
    print (sql)
    cursor = None
    try:
       cursor = hive.connect(host='45.77.110.33', port=10000, username='hadoop').cursor()
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
       for var in conn_result:
           #print(var)
           var1 = var[0]
           var2 = var[1]
           print("|  接口编号: %s,接口名称: %s,接口属性: %s,接口主题: %s,上传方式: %s,上传时限: %s,接口状态: %s   |" % \
                 (var[0],var[1],var[2],var[3],var[4],var[5],var[6]))

    except Exception:
        print ('%s' % (message))
    finally:
        cursor.close()

if __name__ == '__main__':
    pyhiveexesql("SELECT * FROM new_test where intunit_code <> 'P直通车固定用户' LIMIT 20")

