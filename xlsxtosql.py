import traceback
import pymysql
import xlrd
import time
from time import  sleep
def mysql_link(de_name):
    try:
        db =pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="123456",
                            db=de_name,
                            charset='utf8'
                            )
        return  db
    except:
        print("could not connect to sql")
def open_excel(excel_file):
    try:
        book =xlrd.open_workbook(excel_file)
        return book
    except:
        print(traceback.print_exc())
        print("could not open xlsx")
def store_to_num(db_name, table_name, excel_file):

       store_to(db_name,table_name,excel_file)
def store_to(db_name, table_name, excel_file):
    db = mysql_link(db_name)
    cursor = db.cursor()

    book =open_excel(excel_file)
    sheets =book.sheet_names()
    for sheet in sheets:
        sh= book.sheet_by_name(sheet)
        row_num = sh.nrows
        print(row_num)
        print(sh.row_values(14999))
        for i in range(4301, 14801, 200):
           for j in range(i,i+200):
              print(j)
              row_data =sh.row_values(j)
              value=(row_data[0],row_data[1])
              sql = "INSERT INTO " + table_name + "(id,answer)VALUES(%s,%s)"
              try:
               cursor.execute(sql, value)
              except:
                continue
        db.commit()

        print( sheet +" has been inserted")
    cursor.close()
    db.close()
if __name__ == '__main__':
    store_to_num('lucene','answerzhi','result.xlsx')