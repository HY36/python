import os,time
def fun(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            f,ext = os.path.splitext(fn)
            if ext==".py":
                size=os.path.getsize(os.path.join(root, fn))
                cTime = os.path.getctime(os.path.join(root, fn))
                c_time = time.localtime(cTime)
                print(fn,time.strftime('%Y-%m-%d %H:%M:%S',c_time),size)
fun('c:\\')