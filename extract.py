import os
import argparse
import shutil

def extract(in_dir,out_dir):
    if os.path.isdir(in_dir) == False:
        print('Please Input A Directory Name')
        return -1
    if os.path.exists(out_dir) == False:
        os.mkdir(out_dir)

    file_dict = []
    for dirpath,dirnames,filenames in os.walk(in_dir):
        for file in filenames:
            out_file = file
            while out_file in file_dict:
                file = file + '_'
            src = os.path.join(dirpath,file)
            dst = os.path.join(out_dir,out_file)
            try:
                shutil.copy(src,dst)
            except:
                pass
    return 1

parser = argparse.ArgumentParser()

parser.add_argument('--input','-i',type=str,default=os.getcwd())
parser.add_argument('--output','-o',required=True,type=str)

args = parser.parse_args()

if extract(args.input,args.output) == 0:
    print('Extract Directories Failed!')
else:
    print('Extract All Files Flat to {}'.format(args.output))
