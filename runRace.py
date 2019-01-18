import subprocess, re
exe = "/home/mmgeorg/eecs482/demos/lab_1_demo/a.out"
args = ""

results = {}

for i in range(0, 10000):
   output = subprocess.Popen([exe, args], stdout=subprocess.PIPE).communicate()[0]
   counter = int(re.search(r'\d+', output).group())
   if counter not in results.keys():
      results[counter] = 1
   else:
      results[counter] += 1

print("counter : occurences")
for k, v in results.items():
   print(k, " : ", v)
