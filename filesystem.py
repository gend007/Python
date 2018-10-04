import os
import shutil

def show_dir(path):
    print('=====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))

tmpdir = 'C:/Users/amemiya/Documents/bk/testdir'

os.mkdir(tmpdir)
os.makedirs('C:/Users/amemiya/Documents/bk/testdir/test')
show_dir(tmpdir)


os.rmdir('C:/Users/amemiya/Documents/bk/testdir/test')
show_dir(tmpdir)

os.removedirs(tmpdir)
