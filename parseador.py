import sys
import os

input_files = os.listdir(sys.argv[1])
output_file = open(sys.argv[2],"w" )
flag = False
if(len(sys.argv) > 3):
  flag = True
time = []
cacheMissPer = []
stalls = []
idle = []
scoreboard = []

for input_file in input_files:
  opened_file = open(sys.argv[1] + input_file, "r")
  for line in opened_file:
    if line.startswith("gpu_sim_cycle"):
        time.append(float(line.split("=")[1].strip()))
    elif line.startswith("\tL1D_total_cache_miss_rate"):
      cacheMissPer.append(float(line.split("=")[1].strip()))
    elif line.startswith("Stall:"):
      palabras = line.split("\t")
      stalls.append(int(palabras[0].split(":")[1]))
      idle.append(int(palabras[1].split(":")[1]))
      scoreboard.append(int(palabras[2].split(":")[1]))

  avgMiss = 0.0
  totalTime = 0
  totalStalls = 0
  totalIdle = 0
  totalScoreboard = 0
  debeDar1 = 0
  for i in range(len(time)):
    # print("Este es el tiempo parcial :" + str(time[i]))
    totalTime += time[i]
    totalStalls += stalls[i]
    totalIdle += idle[i]
    totalScoreboard += scoreboard[i]

  print("total time is :" + str(totalTime))
  
  for i in range(len(time)):
    avgMiss += cacheMissPer[i] * time[i]/totalTime
    print(str(cacheMissPer[i]) + " * " + str(time[i]/totalTime))
    debeDar1 += time[i]/totalTime
  print(debeDar1)
  if(flag):
    output_file.write("resultados de : " + input_file + "\n")
    output_file.write("El porcentaje de fallos en cache L1 de datos es de :" + str(avgMiss) + "\n")
    output_file.write("El numero total de ciclos donde hay un warp en Stall es: " + str(totalStalls) + "\n")
    output_file.write("El numero total de ciclos donde hay un warp en Idle son: " + str(totalIdle) + "\n")
    output_file.write("El numero total de ciclos donde hay un warp en Scoreboard son: " + str(totalScoreboard) + "\n")
    output_file.write("El numero total de ciclos que ha tardado en ejecutarse son" + str(totalTime) + "\n")
  else:
    output_file.write("resultados de : " + input_file + "\n")
    output_file.write(str(avgMiss).replace(".", ",") + "\n")
    output_file.write(str(totalStalls) + "\n")
    output_file.write(str(totalIdle) + "\n")
    output_file.write(str(totalScoreboard) + "\n")
    output_file.write(str(totalTime) + "\n")
  del time[:]
  del cacheMissPer[:]
  del stalls[:]
  del idle[:]
  del scoreboard[:]