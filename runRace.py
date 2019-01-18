import subprocess, re
exe = "yourPathToTheExecutableHere" # YOUR PATH HERE
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
