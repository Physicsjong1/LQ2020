import ROOT
import sys
#import objects as obj
from LFNTool import SearchROOT

# ROOT.ROOT.EnableImplicitMT()


# List of Branch Objects
def objects():
    obj_Event = ['event']
    obj_Jet = ['nJet','nbJet','Jet_btagDeepB','Jet_btagDeepC','Jet_eta','Jet_mass','Jet_phi','Jet_pt']
    obj_Electron = ['nElectron','Electron_charge','Electron_eta','Electron_mass','Electron_phi','Electron_pt']
    obj_Muon = ['nMuon','Muon_charge','Muon_eta','Muon_mass','Muon_phi','Muon_pt']
    obj_MET = ['MET_phi','MET_pt','MET_sumEt']
    obj_Tau = ['nTau','Tau_charge','Tau_chargedIso','Tau_eta','Tau_idAntiMu','Tau_mass','Tau_neutralIso','Tau_phi','Tau_pt']
    obj = obj_Event + obj_Jet + obj_Electron + obj_Muon + obj_MET + obj_Tau
    return obj


# Ntuplemaker RDataFrame
def ntuplemaker(inputfile, obj):
    print("Searching input root file...")
    searcher= SearchROOT()
    searcher.verboseOn()
    infilePFN = searcher.fromLFN(inputfile).toPFN()
    print("Load ROOTFile : "+infilePFN)
    
    df = ROOT.ROOT.RDataFrame("Events", infilePFN)
    entries = df.Count()

#    df = ROOT.ROOT.RDataFrame("Events", inputfile)

    # Get Branch Lists such as Jet_pt, Muon_eta, ...
    v = ROOT.vector('string')()
    for name in obj:
        v.push_back(name)


    # Event Selections
#    sel_electron = df.Filter('All(Electron_pt > 30 && abs(Electron_eta) < 2.4)','Electron pt & eta Selection')
#    sel_muon = sel_electron.Filter('All(Muon_pt > 30 && abs(Muon_eta) < 2.4)','Muon pt & eta Selection')
#    #sel_tau = sel_lep_pt.Filter('All(Tau_pt > 30 && (Tau_eta) < 2.4)','Tau pt & eta selection')
    sel_jet = df.Filter('All(Jet_pt > 30 && abs(Jet_eta < 2.4))','Jet pt & eta Selection')
    sel_jet_entries = sel_jet.Count()
#    sel_MET = sel_jet.Filter('MET_pt > 30','MET pt Selection')


    # Add nbjet branch
    #br_nbJet = sel_jet.Define('nbJet','Sum(Jet_btagDeepB > 0.8953)')    # 2016 tight
    #br_nbJet = sel_jet.Define('nbJet','Sum(Jet_btagDeepB > 0.8001)')    # 2017 tight
    br_nbJet = sel_jet.Define('nbJet','Sum(Jet_btagDeepB > 0.7527)')    # 2018 tight
    br_nbJet.Snapshot('Tree','output.root',v)   # b-tagged events only

    report = sel_jet.Report()
    x = report.Print()
    
    with open("events.txt","a") as f:
        f.write("\nInputfile : " + inputfile + "\n")
        f.write("Entries : " + str(entries.GetValue()) + "\n") 
        f.write("Jet selection : " + str(sel_jet_entries.GetValue()) + "\n")
    return report

inputfile = sys.argv[1]
obj = objects()
ntuplemaker(inputfile, obj)

#files = rs.rootfiles(year, sample)  # year : 2016, ... sample : DoubleEG, ...
#print(len(files))
#for i,inputfile in enumerate(files):         # Each run contains upto 20 rootfiles
#    #inputfile = ROOT.vector('string')()
#    print(str(i) +"th Run of "+ year + sample)
#    #for name in files[i]:
#    #    inputfile.push_back(name)
#    outputfilename = "Data_Run" + year + "_" + sample + "_" + str(i) + ".root"
#    outputfile = "./ntuples/data_Run" + year + sample + "/" + outputfilename
#    ntuplemaker(inputfile, outputfile)





## Object Selections
#sel_obj_1l = sel_MET.Filter('nElectron + nMuon == 1','Number of Leptons = 1')
#
## Obj Selection 1
#sel_obj_3j = sel_obj_1l.Filter('nJet >= 3','Number of Jets >= 3')
#sel_obj_1tau = sel_obj_3j.Filter('nTau == 1','Number of Tau == 1')
#
## Obj Selection 2 and 3
#sel_obj_2j = sel_obj_1l.Filter('nJet >= 2','Number of Jets >= 2')
#sel_obj_1b = sel_obj_2j.Filter('nbJet == 1','One b-tagged jet')
#
## Save ntuples to outputfile
#sel_obj_1tau.Snapshot(treename, out_sel1, v)
#sel_obj_1b.Snapshot(treename, out_sel2, v)
#
#report1 = sel_obj_1tau.Report()
#report2 = sel_obj_1b.Report()
#
#print("\n1tau")
#report1.Print()
#print("\n1bjet")
#report2.Print()


#report = sel_jet_pt.Report()

#sel_MET_pt.Snapshot(treename, outputfile, v)

#report = sel_MET_pt.Report()
#report.Print()

#h_nJet = ''' "nJet", "nJet", 15, 0, 15 '''
#h_nMuon = ''' "nMuon", "nMuon", 5, 0, 5 '''
#h_nElectron = ''' "nElectron", "nElectron", 5, 0, 5 '''
#h_Jet_pt = ''' "Jet_pt", "Jet_pt", 25, 0, 500 '''
#h_Jet_eta = ''' "Jet_eta", "Jet_eta", 20, 0, 4.0 '''
#h_Jet_phi = ''' "Jet_phi", "Jet_phi", 20, -4.0, 4.0 '''

#hist = []
#for i, name in enumerate(objects):
#    hist[i] = df_sel.Histo1D((


