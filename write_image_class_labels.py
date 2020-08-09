import os
'''
记录图片的类别
'''


url = '/Users/jiangchengyin/Downloads/imgs'
text_file_name = 'image_class_labels.txt'  # 保存的路径


catalogue = os.listdir(url)
catalogue.sort()
length_catalogue = len(catalogue)
index = 1
for i in range(length_catalogue):
    dir_name = catalogue[i]
    dir_url = os.path.join(url, dir_name)
    if os.path.exists(dir_url) and dir_url != '/Users/jiangchengyin/Downloads/imgs/.DS_Store':
        dir_file = os.listdir(dir_url)
        length_dir = len(dir_file)

        for j in range(length_dir):
            old = dir_file[j]
            new_url = os.path.join(dir_name, old)
            res = str(index) + " " + str(i) + '\n'
            index += 1
            with open(text_file_name, 'a+') as f:
                f.writelines(res)