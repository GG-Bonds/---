import os
import random
'''
记录图片的类别
'''

def getSplitRes(threahold: float):
    if random.uniform(0, 1) < threahold:
        return 1
    return 0


url = '/Users/jiangchengyin/Downloads/imgs'
text_file_name = 'train_test_split.txt'  # 保存的路径
threahold = 0.6   # 训练和测试样本的比例

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

            res = str(index) + ' ' + str(getSplitRes(threahold)) + '\n'
            index += 1
            with open(text_file_name, 'a+') as f:
                f.writelines(res)