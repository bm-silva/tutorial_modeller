                                                               # Addition of restraints to the default ones
from modeller import *
from modeller.automodel import *                               # Load the automodel class

log.verbose()
env = Environ()
env.io.hetatm = False					       # Read in HETATM records from template PDBs

a = automodel(env,
              alnfile  = 'model-seq.ali',                          # alignment filename
              knowns   = ('model'),                           # codes of the templates
              sequence = 'seq',
              assess_methods = (assess.DOPE, assess.GA341))    # code of the target

a.starting_model= 1                                            # index of the first model
a.ending_model  = 3                                          # index of the last model
                                                               # (determines how many models to calculate)
# Very thorough VTFM optimization:
a.library_schedule = autosched.slow
a.max_var_iterations = 300

# Thorough MD optimization:
a.md_level = refine.slow

# Repeat the whole cycle 2 times and do not stop unless obj.func. > 1E6
a.repeat_optimization = 2
a.max_molpdf = 1e6


a.make()                                                       # do homology modeling


