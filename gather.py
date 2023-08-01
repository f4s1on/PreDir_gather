import re
import sys

file = open('url.txt')
formatfile = open('dir.txt','w+')
domainregex = r'(^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/))'
regex = r'\/([^\/]*)\/'
dirs = []

def add(basedir,dir):
    data = re.search(regex,str(dir))
    if(data != None):
        data = data.group(1)
        data = basedir+data+'/'
        dirs.append(data)
        d = re.sub(regex,'/',str(dir),1)
        add(data,d)
    else:
        return

for line in file.readlines():
    line = re.sub(domainregex,'',str(line),1)
    line = '/' + line 
    add('/',line)


with open('url.txt', 'r') as file:
    first_line = file.readline()
host = re.search(domainregex,first_line)
if(host != None):
    host = host.group(1)
dirs.append('/')
host = host[:-1]


dirs = set(dirs)

for i in dirs:
    formatfile.writelines(host+i+'\n')
