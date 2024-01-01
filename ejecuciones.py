import sys
import os

input_path = os.listdir(sys.argv[1])
for path in input_path:
    totalPath = sys.argv[1] + "/" + path + "/"+ os.listdir(sys.argv[1] + "/" + path)[0] + "/traces/kernelslist.g"
    os.system("../gpu-simulator/bin/release/accel-sim.out -trace " + totalPath + " -config ../gpu-simulator/configs/tested-cfgs/NVIDIA_GeForce_RTX_3060_Ti/gpgpusim.config -config ../gpu-simulator/configs/tested-cfgs/NVIDIA_GeForce_RTX_3060_Ti/trace.config > "+ path + ".txt")
    print("Ejecucion terminada de " + path)
    