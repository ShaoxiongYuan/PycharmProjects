f=open("hello.txt","wb+")
f.write("春天来了".encode())
f.flush()
f.seek(-6,2)
print(f.read().decode())