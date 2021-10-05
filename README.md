# Tutorial para Modelagem Comparativa utilizando Modeller v10.1

## Introdução

É preciso que todos os arquivos estejam na mesma pasta e nomeados de acordo com as suas referências nos scripts. Observação: os nomes podem ser definidos de qualquer maneira, contanto que haja semelhança entre os nomes referenciados nos scripts e os arquivos dentro da pasta. Desta forma, é preferível padronizar todos os nomes para evitar cometer algum erro.
Neste tutorial, utilizaremos `model.pdb` para o arquivo de referencia e o arquivo `seq.ali` como o arquivo contendo a sequencia a ser modelada.

Dentro de cada pasta de exemplo ja se encontram os scripts que serão utilizados e seus respectivos arquivos de entrada e saida.

##  Modelagem Utilizando Somente uma Estrutura como Referencia

Para esta etapa, é preciso conter os seguintes arquivos: **model.pdb**, **seq.ali**, **align2d.py** e **genmodel.py** ou **genmodel_opt.py**.

Dentro do script **align2d.py**, podemos observar as seguintes linhas:
```
  mdl = model(env, file='model', model_segment=('FIRST:A','LAST:A'))
  aln.append_model(mdl, align_codes='model', atom_files='model.pdb')
```

Estes códigos definirão qual será o pdb de referência para a modelagem. Observar os campos no qual aparece `model`. Neles é contido as informações necessárias para referenciar o arquivo .pdb a ser utilizado como referencia. Em `mode_segment` está definindo quais cadeias do arquivo serão utilizados na modelagem (FIRST:`A`','LAST:`A`'). Para uma estrutura contendo somente um monómero, os valores de FIRST e LAST deverão ser iguais. Caso necessite de mais de uma cadeia, ou a sua estrutura for um dímero, colocar quais as cadeias a serem utilizadas em ordem alfabética. Por exemplo, para um trímero: ('FIRST:A','LAST:C').

```
aln.append(file='seq.ali', align_codes='seq')
```
Este código define qual a sequência primária que será utilizada para gerar o modelo. Em `file` está definido qual será o arquivo contendo a sequência fasta a ser utilizado na modelagem em `align_codes` o seu index, tal como no código anterior a este mostrado mostrado.

```
aln.align2d()
```

Esta linha representa qual alinhador será utilizado pelo modeller. Sequências muito grandes necessitarão de argumentos especiais para poder agilizar o processo. Olhe no manual (https://salilab.org/modeller/manual/) do Modeller para poder saber quais parâmetros precisarão ser ajustados.

```
aln.write(file='model-seq.ali', alignment_format='PIR')
aln.write(file='model-seq.pap', alignment_format='PAP')
```

Estas linhas definem o arquivo de saída do alinhamento que será utilizado na modelagem. Em `file` o nome pelo qual os arquivos serão salvos. Também precisam estar referenciados no script que gera o modelo, caso modifique este arquivo para utilizear um nome diferente.

Analisando o arquivo de alinhamento gerado **model-seq.ali** podemos observar as seguintes informações:

```
>P1;model
structureX:model.pdb:1:A:+558:A:MOL_ID  1; MOLECULE  RNA-DIRECTED RNA POLYMERASE; CHAIN  A, B; SYNONYM  NS5B; ENGINEERED  YES:MOL_ID  1; ORGANISM_SCIENTIFIC  HEPATITIS C VIRUS ISOLATE HC-J8; ORGANISM_COMMON  HCV; ORGANISM_TAXID  11115; EXPRESSION_SYSTEM  ESCHERICHIA COLI; EXPRESSION_SYSTEM_TAXID  562: 1.90: 0.17
SMSYTWTGALITPCGPEEEKLPINPLSNSLMRFHNKVYSTTSRSASLRAKKVTFDRVQVLDAHYDSVLQDVKRAA
SKVSARLLTVEEACALTPPHSAKSRYGFGAKEVRSLSRRAVNHIRSVWEDLLEDQHTPIDTTIMAKNEVFCI---
DKKPARLIVYPDLGVRVCEKMALYDIAQKLPKAIMGPSYGFQYSPAERVDFLLKAWGSKKDPMGFSYDTRCFDST
VTERDIRTEESIYQACSLPQEARTVIHSLTERLYVGGPMTNSKGQSCGYRRCRASGVFTTSMGNTMTCYIKALAA
CKAAGIVDPVMLVCGDDLVVISESQGNEEDERNLRAFTEAMTRYSAPPGDLPRPEYDLELITSCSSNVSVALDSR
GRRRYFLTRDPTTPITRAAWETVRHSPVNSWLGNIIQYAPTIWVRMVIMTHFFSILLAQDTLNQNLNFEMYGAVY
SVNPLDLPAIIERLHGLEAFSLHTYSPHELSRVAATLRKLGAPPLRAWKSRARAVRASLIAQGARAAICGRYLFN
WAVKTKLKLTPLPEASRLDLSGWFTVGAGG-GDIYHS*

>P1;seq
sequence:seq:: :: ::: 0.00: 0.00
SLSYSWTGALVTATRREERRHPIGPLSNTLITKHNLVYQTTTASASARMTKVTIDREQILDKHYFDTVTAVKKKA
SEVTADLLTWDEVARLTPKNTARSKSGLSGSDVRQLTRAARRELNSMWQDLLSDSEELIPTTVMAKNEVFVSSPT
ARKPARLIVYPDLPVRACEKRAMYDLFQKLPYAVMGKAYGFQYTPRQRVNRLLDMWRHFKNPMGFSYDTKCFDST
VTPHDIDTERDIFLSATLPDEAKTVIKNLTSRLYRGSPMYNSRGDLVGKRECRASGVFPTSMGNTLTNFIKATAA
AKAAGLSDPQFLICGDDLVCITSSKGVEEDEQALREFTSAMTKYSAIPGDLPKPYYDLEQITSCSSNVTVAQDRN
GRPYYFLTRDPTTPLARASWETISHSPVNSWLGNIIAFAPTVWVRLVFLTHFFGLLLQQDAVDRNYEFEMYGSTY
SVNPLDLPAIIYKLHGPEAFDLTNYSPYEVQRVAAALQKLGSPPLRAWKRRAKLDRSKLKVRGGRYAVVADYLFG
FASAYRPKRPAPPGVNSIDVSGWFSIGDDSIGDIYRQ*
```

Nos campos contendo `model` e `seq` é possível observar os nomes que foram definidos no script de alinhamento. Observar que os gaps são preenchidos por `-`. É possível adicionar, remover e mover resíduos caso necessário. Para tal, observar que o número de caracteres nas duas sequências deverão ser iguais e terminar com *.

No arquivo **seq.ali**, temos as seguintes informações:

```
>P1;seq
sequence:seq:::::::0.00: 0.00
SLSYSWTGALVTATRREERRHPIGPLSNTLITKHNLVYQTTTASASARMTKVTIDREQILDKHYFDTVTAVKKKASEVTA
DLLTWDEVARLTPKNTARSKSGLSGSDVRQLTRAARRELNSMWQDLLSDSEELIPTTVMAKNEVFVSSPTARKPARLIVY
PDLPVRACEKRAMYDLFQKLPYAVMGKAYGFQYTPRQRVNRLLDMWRHFKNPMGFSYDTKCFDSTVTPHDIDTERDIFLS
ATLPDEAKTVIKNLTSRLYRGSPMYNSRGDLVGKRECRASGVFPTSMGNTLTNFIKATAAAKAAGLSDPQFLICGDDLVC
ITSSKGVEEDEQALREFTSAMTKYSAIPGDLPKPYYDLEQITSCSSNVTVAQDRNGRPYYFLTRDPTTPLARASWETISH
SPVNSWLGNIIAFAPTVWVRLVFLTHFFGLLLQQDAVDRNYEFEMYGSTYSVNPLDLPAIIYKLHGPEAFDLTNYSPYEV
QRVAAALQKLGSPPLRAWKRRAKLDRSKLKVRGGRYAVVADYLFGFASAYRPKRPAPPGVNSIDVSGWFSIGDDSIGDIY
RQ*
```

Este arquivo contém a sequência primária a ser modelada. Nos campos contendo `seq`, nomes presentes nos scripts. Lembrar que a sequência deve conter o caracter * no final. Caso o seu modelo seja um dímero ou um trímero, a separação deverá ocorrer por meio de `/`  por exemplo: 

```
>P1;seq
sequence:seq:::::::0.00: 0.00
SLSYSWTGALVTATRREERRHPIGPLSNTLITKHNLVYRMTK/VTIDREQILDKHYFDTVTAVKKKASEVTADLLTWDEVARLTPKNTARSKS/GLSGSDVRQLTRAARRELNSMWQDLLSDSEELIPTTVMAKNEVFVSSPT*
```

Para a modelagem, estão disponíveis 2 tipos de scripts: o **genmodel.py** e o **genmodel_opt.py**. A diferença é que no segundo o Modeller irá fazer um refinamento da estrutura após a modelagem, gastando mais tempo e necessitando de menos modelos a ser modelado.
Dentro destes arquivos observamos as seguintes linhas:

```
a = automodel(env,
              alnfile  = 'model-seq.ali',                     
              knowns   = ('model'),                             
              sequence = seq,
              assess_methods = (assess.DOPE, assess.GA341))
```

Em `alnfile`, `knowns` e `sequence`, observamos os arquivos e os nomes de referência que serão utilizados nesta etapa. Em `assess_methods`, o argumento necessário para gerar o valor de DOPE (https://en.wikipedia.org/wiki/Discrete_optimized_protein_energy) score dentro do arquivo PDB para poder selecionar as estruturas de menor energia.

```
a.starting_model= 1                                            
a.ending_model  = 10
```

Estas duas linhas definem o número de estruturas que serão calculadas. Caso deseje 1000 estruturas, alterar o valor do `a.ending_model` para 1000.

Dentro do arquivo do **genmodel_opt.py**, estas linhas são responsáveis pelo refinamento das estruturas após a modelagem:

```
a.library_schedule = autosched.slow
a.max_var_iterations = 300

a.md_level = refine.slow

a.repeat_optimization = 2
a.max_molpdf = 1e6
```

Portanto, para rodar a modelagem, siga os seguintes passos:

1. **$ python align2d.py**
2. **$ python genmodel.py ou genmodel_opt.py**
3. **$ mkdir menor_energia** - Para criar uma pasta que irá conter as estruturas de menor energia
4. **$ grep DOPE \*.pdb | sort -nk5 > dope.txt** - Para poder criar um arquivo texto contendo todas as energias dos modelos de ordem decrescente. Dentro deste arquivo, selecione o nome da estrutura de menor energia.
5. Copie a estrutura de menor energia para a pasta `menor_energia`

O valor de DOPE está escrito dentro dos arquivos no formato **.pdb** que foram gerados pelo Modeller. Com isso, utilizamos o **grep** e o **sort** para buscar e ordernar estes valores. Todos estes valores são escritos no arquivo **dope.txt**.

Pronto, agora você pode seguir para a avaliação do modelo que acabou de ser gerado!

## Avaliação de um modelo gerado pelo Modeller utilizando o DOPE Score

Para esta etapa você irá precisar dos arquivos: **evaluate_model.py**, **evaluate_reference.py**, **plot_profile.py**, arquivo de alinhamento da sua sequência com o modelo de referência, no formato **.ali** e os arquivos de estrutura, tanto da referencia quanto a que você acabou de modelar. 
Para realizar esta etapa, utilizando os scripts aqui encontrados, nomeie a sua estrutura de referencia como **reference.pdb** e a estrutura que você modelou como **model.pdb**.

Dentro dos arquivos **evaluate_model.py** e **evaluate_reference.py** encontramos as seguintes linhas:

```
mdl = complete_pdb(env, 'model.pdb')

s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='model.profile',
              normalize_profile=True, smoothing_window=15)
```

```
mdl = complete_pdb(env, 'reference.pdb')

s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='reference.profile',
              normalize_profile=True, smoothing_window=15)
```

Perceba os campos contendo as palavras `model` e `reference`, são eles que contém as informações do arquivo de entrada, no formato **.pdb** e de saída, com extensão **.profiles**.

O arquivo mais que irá gerar um gráfico de DOPE Score é o **plot_profile.py**. Nele encontramos as seguintes linhas:

```
a = modeller.Alignment(e, file='model-seq.ali')
```
Para referenciar o arquivo de alinhamento.

```
template = get_profile('reference.profile', a['model'])
model = get_profile('model.profile', a['seq'])
```

Para referenciarmos os arquivos de profile gerados pelo **evaluate_model.py** e **evaluate_reference.py** e os respectivos index escritos nos scripts de alinhamento e modelagem.

Com isso, para fazer a avaliação do seu modelo, siga os passos:

1. **$ python evaluate_model.py**
2. **$ python evalutate_reference.py**
3. **$ python plot_profile.py**

##  Modelagem Utilizando mais de uma Estrutura como Referencia

Para este tipo de modelagem, também haverá a padronização dos nomes dos arquivos **.pdb** e de sequência. Foi nomeado os arquivos **.pdb** de referência de forma crescente e mantendo padrão: **model1.pdb**, **model2.pdb** e assim por diante. O arquivo de alinhamento continuará com o nome **seq.ali**;
Para realizar a modelagem múltipla, vamos utilizar os aquivos: **salign.py**, **align2d_multi.py** e **model_multi.py**.

A primeira etapa é alinhar os modelos de referência, neste caso, com o script **salign.py**, que contém as seguintes linhas:

```
aln = alignment(env)
for (code, chain) in (('model1', 'A'), ('model2', 'A')):
    mdl = model(env, file=code, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(mdl, atom_files=code, align_codes=code+chain)
```
Em `model1`, `model2`, `A`, `A`,podemos observar os nomes dos arquivos de referencia no formato **.pdb** e as cadeias que serão utilizadas neste alinhamento. Caso seja mais de um modelo, adicionar os nomes seguindo o mesmo modelo, por exemplo:

```
for (code, chain) in (('model1', 'B'), ('model2', 'A'), (‘model3’, ‘A’)):
```

As linhas a seguir irão gerar o arquivo de alinhamento. Este nome é referenciado em outros scripts e precisa ser igual em todos.

```
aln.write(file='model_align.ali', alignment_format='PIR')
aln.write(file=’model_align.pap', alignment_format='PAP')
```
Próxima etapa é o alinhamento da sequência primária com o alinhamentos resultante das estruturas utilizando o **align2d_multi.py**:

```
aln.append(file='model_align.ali', align_codes='all')
```

Esta linha contém qual o arquivo de alinhamento de modelos será utilizado, em `file`.

```
aln.append(file='seq.ali', align_codes='seq')
```

Está linha contém qual o arquivo contendo a sequência fasta que será modelada, em `file`, e o seu index, em `align_codes`.

As linhas a seguir estão os nomes dos arquivos de alinhamento que serão utilizados na etapa de modelagem:

```
aln.write(file='seq-multi.ali', alignment_format='PIR')
aln.write(file='seq-multi.pap', alignment_format='PAP')
```
	
Último passo é a modelagem utilizando o **model_multi.py**:

```
env = environ()
a = automodel(env, alnfile=seq-multi.ali',
              knowns=('model1A','model2A'), sequence='seq',
			  assess_methods=(assess.DOPE))
```

Estas linhas contem quais os arquivos serão utilizados para a modelagem. Em `alnfile` o arquivo de alinhamento gerado, em `knonws` o nome dos arquivos pdb e em vermelho a cadeia escolhida. Destacado em `asses_methods` o argumento para escrever o DOPE score nos arquivos de saída.

Similar ao **genmodel.py**, as próximas linhas definem o número de estruturas a serem geradas:

```
a.starting_model = 1
a.ending_model = 10
```

Protanto, para rodar a sua modelagem com múltiplas estruturas de referência, siga os passos:

1. **$ python salign.py**

2. **$ python align2d_multi.py**

3. **$ python model_multi.py**

## Modelagem das regiões de *loop*

Após a realização da modelagem comparativa, selecione o modelo de menor energia que será submetido a otimização da modelagem dos loops.
Para esta etapa é necessário que o arquivo **.pdb** a ser modificado e nomeado de model.pdb, juntamente com o arquivo **loop_refine.py** e o arquivo **.ali** contendo a sequência.

Será utilizado o script loop_refine.py:

```
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        return selection(self.residue_range('35:A', '39:A'),
                         self.residue_range('49', '57:A'))
```

Estas linhas irão definir quais as regiões que serão modeladas. Destacado em `selection` os resíduos iniciais e finais que definem a região, seguidos pela cadeia (**:A**). Para adicionar mais regiões, manter o mesmo padrão de escrita, por exemplo:

```
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        return selection(self.residue_range('35:A', '39:A'),
                         self.residue_range('49:A', '57:A'),
                         self.residue_range('102:A', '108:A'))
```

A região a seguir define qual o arquivo **.pdb** será utilizado e qual a sequência a ser utilizada. Destacado em `loop_assess_methods` a função para escrita do DOPE score no arquivo PDB. Em `alnmodel`, o nome do arquivo **.pdb** que será modelado e em ver o nome da sequência.
Em `sequence` o prefixo que será adicionado no nome de cada arquivo de saída.


```
m = MyLoop(env,
           inimodel='model.pdb', # initial model of the target
           sequence=seq,
           loop_assess_methods = (assess.DOPE, assess.GA341))
```

Similar aos outros scripts, a região a seguir define o número de estruturas as serem geradas.

```
a.starting_model= 1                                            
a.ending_model  = 10  
```
	

Para rodar a modelagem, digite no terminal: **python loop_refine.py**;
A seleção das estruturas de menor energia são feitas de forma similar as etapas anteriores.

