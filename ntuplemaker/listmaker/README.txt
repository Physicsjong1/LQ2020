Run with "python classification.py"

Importfiles for classification.py

    1. path_search.py
        
        Functions
        search_data(data_dir)   data_dir = /xrootd/store/data
        search_mc(mc_dir)       mc_dir = /xrootd/store/mc
            
        * Search all of the NanoAOD rootfiles under the given directory.
        * Return full paths in form of python list

    2. class_objects.py

        Functions
        class_mc()
        class_data()

        * Return list of the selected triggers (data) or processes (mc)


Classfication with classification.py
    
    Select the version of NanoAOD : "Nano25Oct2019"
    
    For Data:   Select year (eg."Run2016B") and trigger (eg."DoubleMuon")
                years : Run2016, Run2017, Run2018
                triggers : DoubleMuon, DoubleEG, EGamma, DoubleEG

    For MC:     Select year (eg. "RunIIAutumn18") and process (eg. TT, DY, ...)
                years : RunIIAutumn18, RunIIFall17, RunIISummer16
                processes : TT or tt, DY
                * Further ST, W(1,2,3,4)Jets or WJets, WW, WZ, ZZ (not WWW, WWZ, WZZ, ZZZ) 


