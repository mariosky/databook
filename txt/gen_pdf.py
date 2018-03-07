
from os import listdir
from os.path import isfile, join
import subprocess


path = r"/Users/mariosky/databook/txt"

files = [f for f in listdir(path) if isfile(join(path, f)) and f[-2:] == 'md' ]





for f in files:
    args = ['/usr/local/bin/pandoc', "%s/%s" % (path,f), r'--latex-engine=/Library/TeX/texbin/xelatex', '-o', f +".pdf"]
    print args
    subprocess.check_call(args)

    #call(command)

