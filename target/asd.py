from encodings import utf_8
import mysql.connector, time, os, re

db_handle = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

print (db_handle)

kursor = db_handle.cursor()
kursor.execute('CREATE DATABASE IF NOT EXISTS translated_files')
kursor.execute("use translated_files ;")
db_handle.commit()
file_text2=os.listdir()
print(file_text2)
for x in file_text2:
    if x != "asd.py":
        folder_files = os.listdir(x)
        print (f'files\' folders of `{x}`##########################')
        # print (x) 
        # kursor.execute(f" create  TABLE `{x}` (textID int NOT NULL AUTO_INCREMENT PRIMARY KEY, text text);" )
        kursor.execute(f" create  TABLE `{x}` ( textID int NOT NULL , text text);" )
        db_handle.commit()

        for y in folder_files:         
            print (f'{x}/{y}***********')
            file = open(f'{x}/{y}', 'r')
            for z in file.readlines():
                no_SC=z.replace('\'', "\\'").replace('\"', '\\"')
                noSC2=re.escape(z)
                noSC3=noSC2.replace('\\ ', ' ')

                table = str.maketrans({"-":  r"\-", "]":  r"\]", "\\": r"\\",
                                    "^":  r"\^", "$":  r"\$", "*":  r"\*", ".":  r"\." , "'": r"\'" , '"' : r"\""})
                s_new = z.translate(table)
                y=y.replace("_video_or_play_page.txt", "").replace(".txt" , "")
                print(f'{s_new}__________________')
                kursor.execute(f"INSERT INTO `{x}` VALUE ({y},'{s_new}'); " ) 
                db_handle.commit()         

