#首先要把文件名编码为当前电脑的编码，再用原始编码对应的unicode字库来进行解码，得到正确的文件名
import os
base_path = input("paste your folder addr \n")
if(not os.path.isdir(base_path)):
    print("invalid path")
    exit(0)

charset = ["blank","SHIFT-JIS","GBK","UTF-8"]
origin_lang = 0
dest_lang = 0
while(not (type(origin_lang)==int and 0<origin_lang<4)):
    origin_lang = eval(input("enter number for file name's origin character set \n1.SHIFT-JIS    2.GBK   3.UTF-8\n"))

while(not (type(dest_lang)==int and 0<dest_lang<4)):
    dest_lang = eval(input("enter number for your computer's character set \n1.SHIFT-JIS    2.GBK   3.UTF-8\n"))
if(origin_lang == dest_lang):
    print("same lang between origin and destination lang!")
    exit(0)


origin_lang = charset[origin_lang]
dest_lang = charset[dest_lang]


for root, dirs, files in os.walk(base_path,topdown=False):
    #print(root,dirs,files)
    for file in  files:
        trans_file = file.encode(dest_lang).decode(origin_lang)
        os.rename(os.path.join(root,file),os.path.join(root,trans_file))
        print(file+"-->"+trans_file)
    for dir in  dirs:
        trans_dir = dir.encode(dest_lang).decode(origin_lang)
        os.rename(os.path.join(root,dir),os.path.join(root,trans_dir))
        print(dir+"-->"+trans_dir)
print('done')