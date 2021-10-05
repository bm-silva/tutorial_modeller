from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='model', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='model', atom_files='model.pdb')
aln.append(file='seq.ali', align_codes='seq')
aln.align2d()
aln.write(file='model-seq.ali', alignment_format='PIR')
aln.write(file='model-seq.pap', alignment_format='PAP')