
import mysql.connector, time, os

db_handle = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

print (db_handle)

kursor = db_handle.cursor()

names = []

kursor.execute("use test ;")
db_handle.commit()
########################################
########### Old sample #################
########################################

# file = open('2/data.txt', 'r')

# for x in file.readlines():
#     names.append(x.rstrip('\n'))
    


# for y in names:
#     print (f'`{y}`')
#     # kursor.execute("create database `" + y +"`")
#     # db_handle.commit()
#     # time.sleep(1)
print("######################################")

# file_names = [os.system("powershell -c \"ls -n\"")]
file_names2=os.listdir()
try:
    for x in file_names2:
        folder_files = os.listdir(x)
        
        print (f'files\' folders of `{x}`')
        kursor.execute(f" create  TABLE `{x}` (textID int NOT NULL AUTO_INCREMENT PRIMARY KEY, text varchar(255));" )
        db_handle.commit()
        
        for y in folder_files:
            print (f'`{y}`')
            kursor.execute(f"INSERT INTO {x} (text) VALUES ('`{y}`'); " ) 
            db_handle.commit()            
except:
    print('#####################################')
    print (x)
    print('not a folder')
# print (file_names2)
