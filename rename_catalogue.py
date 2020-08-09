import os

'''
修改图片目录名
'''

def getNumber(mystr: str):   # 获取目录的位置 形式为 001 023这类的， 便于排序
    length = len(mystr)
    zeros = '0' * (3 - length)
    mystr = zeros + mystr
    return mystr


url = '/Users/jiangchengyin/Downloads/imgs'


catalogue = os.listdir(url)
catalogue.sort()
length_catalogue = len(catalogue)
for i in range(length_catalogue):
    dir_name = catalogue[i]
    dir_url = os.path.join(url, dir_name)
    if os.path.exists(dir_url) and dir_url != '/Users/jiangchengyin/Downloads/imgs/.DS_Store':

        new = getNumber(str(i)) + '_' + dir_name.split('_')[-1]
        # new = dir_name.split('_')[-1]
        newurl = os.path.join(url, new)
        os.rename(dir_url, newurl)

