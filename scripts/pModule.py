class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    pass


Adam1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 

def find_triple (seq, base):
    count = 0
    for i in range(len(seq)):

        if seq[i] ==  str(base):
            count = count + 1
            if count == 3:
                return(seq[:i-2] + "-" + seq[i:])
        else:
            count = 0

def dalga(d):
    ydots = []
    xdots = np.arange(-d, d+ 1)
    #x^ 3 – 3x 
    for x in np.arange(-d,d+1):
        ydots.append(x ** 3 - 3*x)
      
    plt.plot(xdots, ydots)



def sinus(a):
    xdots = np.arange(-a, a+ 1)
    ydots = np.array(np.sin(xdots))
    
    plt.plot(xdots, ydots)

