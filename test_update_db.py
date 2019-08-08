import json
import os
import sqlite3
import re
import sys
import win32com.client as win32





#########  db  ##############

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# cursor.execute("select * from fenix_maindb, SET vm_name=replace(vm_name, '.vmx', '')")
cursor.execute("update fenix_maindb SET vm_name = replace(vm_name, '.vmx', '')")
conn.commit()
# print(cursor)
# for i in cursor:
#     print(i)

cursor.execute("Select vm_name from fenix_maindb")

results = cursor.fetchall()
# print(results)
for i in results:
    print(i)

# Не забываем закрыть соединение с базой данных
conn.close()
##########

