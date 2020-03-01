import path_search as ps
import os, sys
import time

def data_run(path):
    tmp = ''
    run = ['Run2016','Run2017','Run2018']
    for i in run:
        if i in path:
            tmp = i
    return tmp
            
def mc_run(path):
    tmp = ''
    run = ['RunIISummer16','RunIIFall17','RunIIAutumn18']
    for i in run:
        if i in path:
            tmp = i
    return tmp
#def save_data_list(run, trigger, filepath):
#    class_txt = "./List/data_" + run + "_" + trigger + ".txt"
#    with open(class_txt,'a') as f:
#        if run in filepath:
#            if trigger in filepath:
#                if "25Oct2019" in filepath:
#                    f.write(filepath + '\n')
#
#def save_mc_list(run, process, filepath):
#    class_txt = "./List/mc_" + run + "_" + process + ".txt"
#    with open(class_txt,'a') as f:
#        if run in filepath:
#            if process in filepath:
#                if "25Oct2019" in filepath:
#                    f.write(filepath + '\n')

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

print("(3/6) Classifying and Saving the DATA NanoAOD ...")
data_classification = {}
for i in list_data:
    trigger = i.split('/')[4]
    year = data_run(i)
    mode = year + "_" + trigger
    if mode not in data_classification:
        data_classification[mode] = []
    data_classification[mode].append(i)
print(data_classification)
for key, paths in data_classification.items():
    with open("./List/data_" + key + ".txt","w") as f:
        for path in paths:
            f.write(path + "\n")
print(round_time(start_time) + " seconds passed\n")

print("(4/6) Classifying and Saving the MC NanoAOD ...")
mc_classification = {}
for i in list_mc:
    process = i.split('/')[4]
    year = mc_run(i)
    mode = year + "_" + process
    if mode not in mc_classification:
        mc_classification[mode] = []
    mc_classification[mode].append(i)
print(mc_classification)
for key, paths in mc_classification.items():
    with open("./List/mc_" + key + ".txt","w") as f:
        for path in paths:
            f.write(path + "\n")
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

