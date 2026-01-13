f1=5.6
f2=4.3
f3=3.6
f4=2.8
f5=4.1

total_force=f1+f2+f3+f4+f5

print('The total force is' +str(total_force)+'KN')

d1 = 0
d2 = 0.75
d3 = 1.5
d4 = 2.25
d5 = 3.0

f = [f1, f2, f3, f4, f5]
d = [d1, d2, d3, d4, d5]

f_tot = f[0] + f[1] + f[2] + f[3] + f[4]
print(str(f_tot) + ' KN')

mid = (d[-1] - d[0]) / 2

mid = f[0] * (d[0] + mid) + f[1] * (d[1] + mid) + f[2] * (d[2] + mid) + f[3] * (d[3] + mid) + f[4] * (d[4] + mid)
print('The moment about the mid point is ' + str(mid) + ' KNm')
# Another way to calculate the moment about the mid point using a loop

indexes = [0, 1, 2, 3, 4]
f_tot = 0
for i in indexes:
    f_tot += f[i] # sum of forces
    print("total at" + str(i) + "=" + str(f_tot) + ' KN')

m_total = 0
mid = (d[-1] - d[0]) / 2

for i in range(5):
    m_total += f[i] * (mid - d[i])
    print("total moment at " + str(i) + "=" + str(m_total) + ' KNm')

n = len(f)

f_tot = 0
m_total = 0
for i in range(n):
    f_tot += f[i]
    m_total += f[i] * (mid - d[i])

print('The total force is ' + str(f_tot) + ' KN')
print('The moment about the mid point is ' + str(m_total) + ' KNm')
 
 # Does the structure meet structural requirements?
f_cap = 100
f_tot = 99

if f_tot > f_cap:
   print("Force exceeds capacity")
elif f_tot == f_cap:
   print("Force is exactly equal to capacity")
else:
   print("Force is less than capacity")
# A better way to compare floating point numbers
if f_tot > f_cap:
   print("Force exceeds capacity")
elif abs(f_tot - f_cap) < 1e-9:
   print("Force is equal to capacity")
else:
   print("Force is less than capacity")
   
  #Momwnet capacity check
m_tot = 100
m_cap = 90 

if m_tot > m_cap:
   print("Moment exceeds capacity")
elif abs(m_tot - m_cap) < 1e-9:
   print("Moment is equal to capacity")
else:
   print("Moment is less than capacity")

def check_against_capacity(tot, cap):
   if tot > cap:
       return "exceeds capacity"
   elif abs(tot - cap) < 1e-9:
       return "is equal to capacity"
   else:
       return "is less than capacity"
   
   output = "moment" + check_against_capacity(f_tot, f_cap)
   print(output)

class Force:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
    
    def to_string(self):
        return str(self.X) + ',' + str(self.Y) + ',' + str(self.Z)
    
 #objects   
    
f1 = Force(-0.3, 0.8, 5.6)

print('Force in X = ' + str(f1.X) + ' KN')
print('Force in Y = ' + str(f1.Y) + ' KN')
print('Force in Z = ' + str(f1.Z) + ' KN')

print('Force = ' + f1.to_string() + ' KN')

f1.X = 0.1
f1.Y = 0.9
f1.Z = 0.0

print('Force in X = ' + str(f1.X) + ' KN')
print('Force in Y = ' + str(f1.Y) + ' KN')
print('Force in Z = ' + str(f1.Z) + ' KN')

fs = [Force(0.0, 0.0, 5.6),
      Force(0.0, 0.0, 4.3),
      Force(0.0, 0.0, 3.6),
      Force(0.0, 0.0, 2.8),
      Force(0.0, 0.0, 4.1)]
f_tot = 0.0
for i in range(len(fs)):
    f_tot += fs[i].Z
print('Total force = ' + str(f_tot) + ' KN')

f_tot = Force(0.0, 0.0, 0.0)
for f in fs:
    f_tot.X += f.X
    f_tot.Y += f.Y
    f_tot.Z += f.Z
print('Total force = ' + f_tot.to_string() + ' KN')
