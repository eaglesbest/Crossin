#!/usr/bin/env python2.7

import os
import os.path


def find_file(directory,pattern):
    result_list = []
    if os.path.isdir(directory):
        for dirs,sub_dirs,files in os.walk(directory):
            for file_name in files:
                if file_name.endswith(pattern):
                    result_list.append(os.path.join(dirs,file_name))
    else:
        print "Error directory!"
        return None
    return result_list

if __name__ == '__main__':
    pattern = '.txt'
    test_dir = '/home/fany'
    result_list = find_file(test_dir,pattern)
    if result_list:
        for file_name in result_list:
            print file_name

