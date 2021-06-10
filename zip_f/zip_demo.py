import os;
import zipfile;

def create_zip(path):
    """创建一个压缩文件"""
    # 创建一个zip文件对象
    print(os.path.basename(path))
    zip_file = zipfile.ZipFile(os.path.basename(path) + ".zip", "w")

    # 将文件写入zip文件中，即将文件压缩
    # os.walk 遍历目标文件夹，获取每一个文件和文件夹
    print('开始压缩文件……')
    for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            print("正在压缩文件夹：" + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
        for name in files:
            print("正在压缩文件：" + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
    # 关闭zip文件对象
    zip_file.close()


def uncommoner(path):
  '''解压缩'''
  zFile = zipfile.ZipFile(path, 'r');
  zFile.extractall();


# 程序主入口
if __name__ == "__main__":
    # 打包（解压缩）的文件路径（文件名）
    path_info = 'test'
    print(os.path.isdir(path_info))
    if os.path.isdir(path_info):
        # 打包
        create_zip(path_info)
        print('压缩完成！')
    elif os.path.isfile(path_info):
      uncommoner(path_info);
      print('解压缩');
    else:
      print('文件格式不正确！')
