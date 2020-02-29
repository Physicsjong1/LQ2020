import path_search as ps
import class_objects as co
import os, sys
import time

def save_data_list(run, trigger, filepath):
    class_txt = "./List/data_" + run + "_" + trigger + ".txt"
    with open(class_txt,'a') as f:
        if run in filepath:
            if trigger in filepath:
                if "25Oct2019" in filepath:
                    f.write(filepath + '\n')

def save_mc_list(run, process, filepath):
    class_txt = "./List/mc_" + run + "_" + process + ".txt"
    with open(class_txt,'a') as f:
        if run in filepath:
            if process in filepath:
                if "25Oct2019" in filepath:
                    f.write(filepath + '\n')

def round_time(start):
    str_itv = str(round((time.time()-start),1))
    return str_itv

data_dir = '/xrootd/store/data'
mc_dir = '/xrootd/store/mc'
start_time = time.time()

print("(1/6) Searching for the NanoAOD DATA in KISTI T3")
list_data = ps.search_data(data_dir)
print(round_time(start_time) + " seconds passed\n")

print("(2/6) Searching for the NanoAOD MC in KISTI T3")
list_mc = ps.search_mc(mc_dir)
print(round_time(start_time) + " seconds passed\n")

os.rmdir('List')
os.mkdir('List')

print("(3/6) Classifying the data ...")
for i in list_data:
    run = co.data_run(i)
    trigger = co.data_trigger(i)
    if run == 0 or trigger == 0:
        continue
    save_data_list(run, trigger, i)
print(round_time(start_time) + " seconds passed\n")

print("(4/6) Classifying the MC lists ...")
for i in list_mc:
    run = co.mc_run(i)
    process = co.mc_process(i)
    save_mc_list(run, process, i)
print(round_time(start_time) + " seconds passed\n")

print("(5/6) DAS formmating for DATA ...")
with open("./List/DAS_data.txt","w") as f:
    das_data_list = ps.das_format(list_data)
    for i in das_data_list:
        f.write(i+"\n")
print(round_time(start_time) + " seconds passed\n")

print("(6/6) DAS formmating for MC ...")
with open("./List/DAS_mc.txt","w") as f:
    das_mc_list = ps.das_format(list_mc)
    for i in das_mc_list:
        f.write(i+"\n")
print(round_time(start_time) + " seconds passed\n")

print("Done")
print(round_time(start_time) + " seconds passed\n")

