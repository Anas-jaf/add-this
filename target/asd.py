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
print(file_text2)
#try:
for x in file_text2:
    if x != "asd.py":
        # print(x)
        folder_files = os.listdir(x)
        # x=re.escape(x)
        
        print (f'files\' folders of `{x}`##########################')
        # print (x) 
        # kursor.execute(f" create  TABLE `{x}` (textID int NOT NULL AUTO_INCREMENT PRIMARY KEY, text text);" )
        kursor.execute(f" create  TABLE `{x}` ( textID int NOT NULL , text text);" )
        db_handle.commit()

        for y in folder_files:
            # y = re.escape(y)
            # print (f'`{y}`')
            
            print (f'{x}/{y}***********')
            file = open(f'{x}/{y}', 'r')

            for z in file.readlines():

                # text.append(z.rstrip('\n').replace('\xa0', '').replace('\'', '').replace('\"', ''))
                no_SC=z.replace('\'', "\\'").replace('\"', '\\"')
                noSC2=re.escape(z)
                noSC3=noSC2.replace('\\ ', ' ')

                table = str.maketrans({"-":  r"\-", "]":  r"\]", "\\": r"\\",
                                    "^":  r"\^", "$":  r"\$", "*":  r"\*", ".":  r"\." , "'": r"\'" , '"' : r"\""})
                # Replace string
                s_new = z.translate(table)
                y=y.replace("_video_or_play_page.txt", "").replace(".txt" , "")
                print(y)
                print(f'{s_new}__________________')
                kursor.execute(f"INSERT INTO `{x}` VALUE ({y},'{s_new}'); " ) 
                db_handle.commit()         
                # input("continue")   
            text = []
#except:
#    print('#####################################')
#    print (x)
#    print('not a folder')
# print (file_text2)
