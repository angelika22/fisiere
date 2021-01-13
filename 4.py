# Ion şi Vasile joacă următorul joc:
with open("input.txt", "r") as f:
    a=f.readline()
with open("output.txt", "w") as f:
    f.write(str(int(a)-2))
    f.write("  ")
    f.write(str(int(a)-1))
    f.write("  ")
    f.write(str(a))
    f.write("  ")
    f.write(str(int(a)+1))
    f.write("  ")
    f.write(str(int(a)+2))

