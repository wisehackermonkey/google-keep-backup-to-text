# pulls out the text from a google keep backup 
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200510
import json
import datetime
import os
import pathlib
p = pathlib.Path('./takeout/Keep').glob('**/*')
json_files =[str(x) for x in p if x.is_file() and str(x).endswith(".json")]
# print(json_files[0:3])
# json_files = json_files[0:3]
# print(open(json_files[0],"r").read())
with open("output_v1.txt","w") as output:
    for json_file in json_files:
        try:
            with open(json_file,"r",encoding="utf-8") as file:
                note_raw_text = file.read()

                note_json = json.loads(note_raw_text)
                title = note_json["title"]
                text = note_json["textContent"]
                date = note_json["userEditedTimestampUsec"]

                note_text = f"{title}\n{text}\n{date}\n-----------------------------------------"
                # print(note_text)
                output.write(note_text)
        except UnicodeEncodeError:
            pass
        except KeyError:
            pass