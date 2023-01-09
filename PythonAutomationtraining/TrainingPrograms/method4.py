import subprocess   # core library
p = subprocess.Popen("python prog.py", stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              shell=True)
#low level communication or OS level communication
#will be in byte strings
out, error = p.communicate(b"10\n10\n")
print("OUTPUT =")
print(out.decode("utf-8"),"---")
print("ERROR =")
print(error.decode("utf-8"))
