#!/usr/local/bin/python3
import sys
import os


def mycopy(path,path2):
    f1 = open(path)
    fcontent = f1.read()
    f1.close()
    f2 = open(path2,'w')
    f2.write(fcontent)
    f2.close()
    return path2
    """
    执行复制操作
    :param path: 文件路径
    :return: 成功 文件名 ;失败 False
    """
def main(path,path2=''):
    """
    打印处理结果
    :param path:要复制的文件路径
    :return:若文件存在，返回 True ;否则，返回 False
    """
    if os.path.exists(path):
        if path2:
            cpres = mycopy(path,path2)
        else:
            cpres = mycopy(path, 'copy_'+path)
        if cpres:
            print("success ,file'name: {}".format(cpres))
            return True
        else:
            print("excute error")
            return False
    else:
        print("args error")
        return False


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            main(sys.argv[1],sys.argv[2])
        else:
            main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)