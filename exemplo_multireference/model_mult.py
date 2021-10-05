from modeller import *
from modeller.automodel import *

env = environ()
a = automodel(env, alnfile='seq-multi.ali',
              knowns=('model1A','model2A'), sequence='seq',
			  assess_methods=(assess.DOPE))
a.starting_model = 1
a.ending_model = 5
a.make()
