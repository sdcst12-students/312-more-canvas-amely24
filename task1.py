import tkinter as tk
"""
Task 1
Read the map1.txt file and convert to a map that you can navigate a
rectangle object through.
"""
w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')
fr=f.read()
frs=fr.split('\n')
print(frs)


maze=[]


for k in range(0,15):
    for (i,j) in itertools.zip_longest(frs[k],range(len(frs[k]))):
        if i=='*':
            maze.append(c.create_rectangle(0+j*31,0+k*31,31+j*31,31+k*31,fill='#000000'))
        else:
            pass
w.mainloop()
