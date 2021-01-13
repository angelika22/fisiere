with open("numar.txt", "r") as f:
    a=f.readline()
with open("inmultire.txt", "w") as f:
    f.write("1*"+a+"="+str(int(a)*1)+"\n")
    f.write("2*"+a+"="+str(int(a)*2)+"\n")
    f.write("3*"+a+"="+str(int(a)*3)+"\n")
    f.write("4*"+a+"="+str(int(a)*4)+"\n")
    f.write("5*"+a+"="+str(int(a)*5)+"\n")
    f.write("6*"+a+"="+str(int(a)*6)+"\n")
    f.write("7*"+a+"="+str(int(a)*7)+"\n")
    f.write("8*"+a+"="+str(int(a)*8)+"\n")
    f.write("9*"+a+"="+str(int(a)*9)+"\n")
    f.write("10*"+a+"="+str(int(a)*10))
