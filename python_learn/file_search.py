from def_local import files_cwd as files_cwd
from def_local import list_cwd as list_cwd
import os
print(os.getcwd())
print(list_cwd.list_cwd())
print('测试步骤1:')
print(files_cwd.files_cwd())
print('测试步骤2:')
print(files_cwd.folders_cwd())