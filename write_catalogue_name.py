import os
'''
记录目录的路径
'''

url = '/Users/jiangchengyin/Downloads/imgs'
text_file_name = 'classes.txt'  # 保存的路径


catalogue = os.listdir(url)
catalogue.sort()
length_catalogue = len(catalogue)
index = 1
for i in range(length_catalogue):
    dir_name = catalogue[i]
    dir_url = os.path.join(url, dir_name)
    if os.path.exists(dir_url) and dir_url != '/Users/jiangchengyin/Downloads/imgs/.DS_Store':

        myclass = str(i)
        res = myclass + ' ' + dir_name + '\n'
        with open(text_file_name, 'a+') as f:
            f.writelines(res)

