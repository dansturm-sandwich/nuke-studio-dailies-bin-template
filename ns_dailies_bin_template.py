import hiero

def makeFolders():

    myProject = hiero.core.projects()[-1]
    
    bin1 = hiero.core.Bin("Comps")
    bin2 = hiero.core.Bin("Plates")
    bin3 = hiero.core.Bin("Sequences")
    bin4 = hiero.core.Bin("Cuts")
    bin5 = hiero.core.Bin("_backup")
    
    bin3.addItem(bin4)
    bin3.addItem(bin5)
    
    clipsBin = myProject.clipsBin()
    clipsBin.addItem(bin1)
    clipsBin.addItem(bin2)
    clipsBin.addItem(bin3)