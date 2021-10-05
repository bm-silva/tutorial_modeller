from modeller import *
from modeller.automodel import *                               # Load the automodel class

log.verbose()
env = Environ()
env.io.hetatm = False					       				   # Read in HETATM records from template PDBs

a = automodel(env,
              alnfile  = 'model-seq.ali',                     # alignment filename
              knowns   = ('model'),                             # codes of the templates
              sequence = 'seq',
              assess_methods = (assess.DOPE, assess.GA341))    # code of the target

a.starting_model= 1                                            # index of the first model
a.ending_model  = 5                                           # index of the last model
                                                               # (determines how many models to calculate)

a.make()                                                       # do homology modeling