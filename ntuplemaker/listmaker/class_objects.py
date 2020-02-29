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


def data_trigger(path):
    tmp = ''
    trigger = ['DoubleMuon','DoubleEG','MuonEG','EGamma','SingleElectron','SingleMuon','Tau']
    for i in trigger:
        if i in path:
            tmp = i
    return tmp

def mc_process(path):
    tmp = ''
    process = ['DY','TTTo2L2Nu','TTToSemiLeptonic','TTToHadronic','WW','WZ','ZZ','ST']
    for i in process:
        if i in path:
            tmp = i
    return tmp
    

