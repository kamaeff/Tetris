from main import H, W

buff = 1


if (H == 20):
    file = open("test.txt", "w")
    file.write(buff + " test height" + " sucsess")
    file.close()
    buff+=1
else:
    file = open("test.txt", "w")
    file.write(buff + " test height" + " unsucsess")
    file.close()
    
    
if (W == 10):
    file = open("test.txt", "w")
    file.write(buff + " test weight" + " sucsess")
    file.close()
    buff+=1
else:
    file = open("test.txt", "w")
    file.write(buff + " test weight" + " unsucsess")
    file.close()


