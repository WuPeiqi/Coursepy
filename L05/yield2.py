#grep -rl 'python' /root


import os

def init(func):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def search(target):
    while True:
        search_path=yield
        g=os.walk(search_path)
        for par_dir,_,files in g:
            for file in files:
                file_abs_path=r'%s\%s' %(par_dir,file)
                # print(file_abs_path)
                target.send(file_abs_path)

@init
def opener(target):
    while True:
        file_abs_path=yield
        # print('opener func==>',file_abs_path)
        with open(file_abs_path,encoding='utf-8') as f:
            target.send((file_abs_path,f))

@init
def cat(target):
    while True:
        file_abs_path,f=yield  #(file_abs_path,f)
        for line in f:
            tag=target.send((file_abs_path,line))
            if tag:
                break
@init
def grep(target,pattern):
    tag=False
    while True:
        file_abs_path,line=yield tag
        tag=False
        if pattern in line:
            tag=True
            target.send(file_abs_path)

@init
def printer():
    while True:
        file_abs_path=yield
        print(file_abs_path)



x=r'D:\code\py\py3\Coursepy\L05\a'



g=search(opener(cat(grep(printer(),'python'))))
print(g)

g.send(x)

'''
面向过程的程序设计：是一种流水线式的编程思路，是机械式
优点：
    程序的结构清晰，可以把复杂的问题简单

缺点：
    1 扩展性差


应用场景：
    1 linux内核，git，httpd

'''




