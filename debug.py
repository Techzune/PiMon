import time

file = open ("_std.log");
file.seek(0,2)

i = 0

while (True):
    i += 1
    output = str(i)+"\t"
    output += file.readline()
    print(output)
    time.sleep(0.2)