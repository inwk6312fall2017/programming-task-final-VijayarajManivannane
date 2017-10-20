try:
    fin = open("running-config.cfg", 'r')
except:
    print("Something Went wrong while reading")

line = fin.read()
word = line.strip(' ')
replaced = word.replace('172.','192.')

try:
    fout = open('new-config.txt', 'w')
    fout.write(replaced)

except:
    print("Something Went wrong while writing")
