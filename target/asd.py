from encodings import utf_8
import mysql.connector, time, os, re

db_handle = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

print (db_handle)

kursor = db_handle.cursor()

text = []

kursor.execute("use test ;")
db_handle.commit()
########################################
########### Old sample #################
########################################

# file = open('2/data.txt', 'r')

# for x in file.readlines():
#     text.append(x.rstrip('\n'))
    


# for y in text:
#     print (f'`{y}`')
#     # kursor.execute("create database `" + y +"`")
#     # db_handle.commit()
#     # time.sleep(1)
print("######################################")

# file_text = [os.system("powershell -c \"ls -n\"")]
file_text2=os.listdir()
# print(file_text2)
#try:
for x in file_text2:
    
    folder_files = os.listdir(x)
    # x=re.escape(x)
    print (f'files\' folders of `{x}`##########################')
    # print (x) 
    # kursor.execute(f" create  TABLE `{x}` (textID int NOT NULL AUTO_INCREMENT PRIMARY KEY, text varchar(255));" )
    # db_handle.commit()

    for y in folder_files:
        # y = re.escape(y)
        # print (f'`{y}`')
        
        print (f'{x}/{y}***********')
        file = open(f'{x}/{y}', 'r')

        for z in file.readlines():

            text.append(z.rstrip('\n').replace('\xa0', ''))
            print(text)
        text = []
        # kursor.execute(f"INSERT INTO `{x}` (text) VALUE (\'{y}\'); " ) 
        # db_handle.commit()            
#except:
#    print('#####################################')
#    print (x)
#    print('not a folder')
# print (file_text2)
