print("搶曽僺傾僲Easy儌乕僪".encode('GBK').decode('shift_jis'))

exit(0)
import os

#base_path = input("paste your folder addr \n")
base_path = "D:\syn_fold\文档\e-lib\钢琴谱\月まで届け不死の煙tuki_easy"
if(not os.path.isdir(base_path)):
    print("invalid path")
    exit(0)
file_list = []
for root, dirs, files in os.walk(base_path,topdown=False):
    print(root,dirs,files)
os.rename(r"D:\Code\Y700\Python\shift-jis_i18n\1",r"D:\Code\Y700\Python\shift-jis_i18n\11")