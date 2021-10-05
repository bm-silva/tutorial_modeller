# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = './:../atom_files'

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        return selection(self.residue_range('35:A', '39:A'),
                         self.residue_range('49:A', '57:A'),
                         self.residue_range('102:A', '108:A'))

m = MyLoop(env,
           inimodel='model.pdb', # initial model of the target
           sequence='seq',
           loop_assess_methods = (assess.DOPE))

m.loop.starting_model= 1           # index of the first loop model 
m.loop.ending_model  = 5       # index of the last loop model
m.loop.md_level = refine.slow      # loop refinement method; this yields
                                   # models quickly but of low quality;
                                   # use refine.slow for better models

m.make()

