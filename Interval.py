import sys
input  = float(sys.stdin.readline().strip())

if 0<= input <= 25:
 print ("Interval [0,25]")
elif 25< input <= 50:
  print ("Interval (25,50]")
elif 50< input <= 75:
  print ("Interval (50,75]")
elif 75< input <= 100:
  print ("Interval (75,100]")
else:
  print("Out of Intervals")
