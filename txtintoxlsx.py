### xlsx导入数据库程序

import numpy as np
import xlrd
import MySQLdb
import pandas as pd
import os
firedir = r'D:\pythonProject3\spider_collection\zhihuAnswerSpider\result'
filename=os.listdir(firedir)
data = pd.read_csv( r'D:\pythonProject3\spider_collection\zhihuAnswerSpider\result\7月份手机坏了，买iphone11合适吗？.txt' , sep='\t')
col = list('文')
data = pd.DataFrame(columns=col)
i = 0
for file in filename:

    filepath = firedir + '\\' + file
    print(filepath)
    # 遍历单个文件，读取行数
    # datai = pd.read_csv(filepath, sep='\t', dtype=str)

    datai = pd.read_csv(filepath,sep='\t', converters={'item': str},header=None,names=['文'],error_bad_lines=False)

    data = pd.concat([data, datai],axis=0)

    '''
    for line in open(filepath, 'r', encoding='utf-8-sig', errors='ignore'):
        # print(str(line))
        f.writelines(line)
        # f.write('\n')
    '''
# 关闭文件
# f.close()

data.to_excel('result.xlsx', index=False)