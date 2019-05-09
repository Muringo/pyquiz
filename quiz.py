def divisible_by_three():
    list = [100,110,120,130,140,150]
    c = [i%3 for i in list]
    print(c)

def sorted():
  a = ['apple','banana','mango']
  b = ['avocado','peach','orange']
  c = ['pineapple','lemon']
  d = list(set(a + b + c))
  print(d)


def divisible_by_three(n):
  for i in range (1,n):
      if (i%3==0):
          print(i)


def smallest():
  t = [1,3,6,8,2,4,5.7]
  print(min(t))


def nested():
m = [[1, 2], [3, 4], [5, 6]]
f = []
for s in m:
    for v in s:
        f.append(v)
        print(f) 

def remove(mystring):
    new = ""
    for c in string:
        if c not in new:
            new = new + c
            return new


def squares():
    d=dict()
    for x in range(149,159):
        d[x]=x**2
        print(d)  





    

    


        