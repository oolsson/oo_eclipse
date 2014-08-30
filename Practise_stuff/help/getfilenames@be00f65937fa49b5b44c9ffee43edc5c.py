def dir_list(dir_name, sub_dir, *args):
    file_list = []
    for file in os.listdir(dir_name):
        dirfile = os.path.join(dir_name, file)
        if os.path.isfile(dirfile):
            if len(args) == 0:
                file_list.append(dirfile)
            else:
                if os.path.splitext(dirfile)[1][1:] in args:
                    file_list.append(dirfile)
        elif os.path.isdir(dirfile) and sub_dir:
            file_list += dir_list(dirfile, sub_dir, *args)
    return file_list

d=dir_list('C:\Users\oo\Documents',False)
print d