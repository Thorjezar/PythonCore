from multiprocessing import Pool
from multiprocessing import Manager
import os

def copyFiletask(queue, files, old_file_name, new_file_name):
    fr = open(old_file_name+'/'+files)
    fw = open(new_file_name+'/'+files)
    content = fr.read()
    fw.write(contene)
    fr.close()
    fw.close()
    queue.put(files)

def main():
    os.chdir('./')
    now_file = os.getcwd()
    print('当前操作目录是%s'%now_file)

    file_name = input('请输入要copy的文件名')
    file_name = str(file_name)
    if file_name not in os.listdir(now_file):
        print('输入的文件名%s有误，请检查！'%file_name)
        exit()
    else:
        old_file = os.listdir(file_name)
        new_file_name = file_name + '_副本'
        if new_file_name not in os.listdir(now_file):
            os.mkdir(new_file_name)
            print('创建文件夹%s'%new_file_name)
    
    q = Manager().Queue()
    pool = Pool(3)

    for files in old_file:
        pool.apply_async(copyFiletask, (q, files, file_name, new_file_name))

    num = 0
    allNum = len(old_file)
    while True:
        q.get()
        num += 1
        copyRate = num/allNum
        print('\r copy的进度是:%.2f%%'%(copyRate*100), end="")
        if num == allNum:
            break

    pool.close()
    pool.join()

    print('拷贝完成')

if __name__=='__main__':
    main()
