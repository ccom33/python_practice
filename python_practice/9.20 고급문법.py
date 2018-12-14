num = [11, 22, 33]
it = iter(num)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)
print('#', '-'*55)
#-------------------------------------------------------------------------

class Seq:
    def __init__(self,data):
        self.data = data
        self.index = -2
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index:self.index +2]

solarterm = Seq ("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ",")

#-------------------------------------------------------------------------
print("\n")
    
def sigong(data):
    for index in range(0, len(data), 2):
        yield data [index:index+2]

solarterm = sigong("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ',')
#--------------------------------------------------------------------------
print('\n')
print('#', '-'*55)
#--------------------------------------------------------------------------
data = "입춘우수경칩춘분청명곡우입하소만망종하지소서대서"
for k in (data[index:index+2] for index in range(0, len(data), 2)):
    print(k, end = ',')

print('\n')

def add(a,b):
    print(a+b)


plus = add
plus(1,2)
