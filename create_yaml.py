import os
from subprocess import Popen, PIPE, STDOUT
import argparse
import glob
from os.path import join
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description='prepare data')
    parser.add_argument('--input', '-i', type=str, nargs='+', help='path to the folder')
    parser.add_argument('--target', '-t', type=str, default='', help='target folder to save the pictures')
    args = parser.parse_args()
    return args

def check_picture_format(name):
    if name.endswith(('.jpg')):
        return True
    return False

def prepare_data(args):
    root_dir = args.input[0]
    rename(root_dir)
    file_list = sorted(glob.glob(join(root_dir, '*.jpg')))

    additional = 'http://localhost:8001/'
    yaml_items = []
    for img in file_list:
        name = os.path.basename(img)
        path = additional + name
        yaml_items.append({'url' : path})
    output = join(args.target, 'image_list.yml')
    with open(output, 'w') as f:
        yaml.dump(yaml_items, f)
    return output

def rename(dirname):
    file_list = sorted(glob.glob(join(dirname, '*.jpg')))

    for img in file_list:
        name = os.path.basename(img)
        if len(name)!=24:
            newname = name[:15] + '0'*(24 - len(name)) + name[15:]
            os.rename(dirname+'/'+name,dirname+'/'+newname)


def main():
    args = parse_arguments()
    print(args.input)
    print(args.target)
    if args.target:
        os.makedirs(args.target, exist_ok=True)

    output = prepare_data(args)
    if output:
        print("SUCCESS")

if __name__ == '__main__':
    main()
