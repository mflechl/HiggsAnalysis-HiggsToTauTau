#!/usr/bin/env python
from optparse import OptionParser, OptionGroup
parser = OptionParser(usage="usage: %prog [options] ARG1 ARG2 ARG3 ...", description="")
agroup = OptionGroup(parser,"MAIN OPTIONS", "")
agroup.add_option("--xs-path",dest="xsPath", default="$CMSSW_BASE/src/higgsContributions/", type="string", help="")
agroup.add_option("--nll-path",dest="nllPath", default="$CMSSW_BASE/src/LIMITS150428-mssm/bbb-asimov-mhmodp-NLL/mt/", type="string", help="")
agroup.add_option("--ggH-bbH-path",dest="ggHbbHPath", default="$CMSSW_BASE/src/LIMITS150428-mssm/bbb-asimov-ggH-bbH/", type="string", help="")
agroup.add_option("--bg-path",dest="BGPath", default="", type="string", help="")
agroup.add_option("--model", dest="model", default="mhmodp",type="string", help="")
agroup.add_option("--model-masspoint", dest="modelMasspoint", default="500_30", type="string", help="")
agroup.add_option("--mass-tolerance", dest="massTolerance", default=0.15, type="float", help="")
agroup.add_option("--tolerance-denumerator-max", dest="toleranceDenumeratorMax", default=False, action="store_true", help="")
agroup.add_option("--reference-mass", dest="referenceMass", default="A", type="string", help="")
agroup.add_option("--higgs-contribution", dest="higgsContribution", default="hHA", type="string", help="")
agroup.add_option("--forbidden-region-level", dest="forbiddenRegionLevel", default=100, type="float", help="")
agroup.add_option("--analysis", dest="analysis", default="plain", type="string", help="")
agroup.add_option("--expected", dest="expected", default=False, action="store_true", help="")
agroup.add_option("--light-vs-heavy", dest="lightVsHeavy", default=False, action="store_true", help="")
agroup.add_option("--higgs-bounds", dest="higgsBounds", default=False, action="store_true", help="")
agroup.add_option("--weighted-hb", dest="weightedHB", default=False, action="store_true", help="")
agroup.add_option("--full-nll-subtracted", dest="fullNLLSubtracted", default=False, action="store_true", help="")
agroup.add_option("--SMHscale", dest="SMHscale", default=False, action="store_true", help="Use the option to chose for each mA tanb point the re-interpreted signal for which scale*xs*BR of the 125GeV peak best agrees with the xs*BR of the little h of the considered MSSM model")
parser.add_option_group(agroup)

(options, args) = parser.parse_args()

import ROOT as r
import os
import sys


	# constructing the cross-section file, that determines the contributions of the Higgs bosons to (mA,tanb) points
for higgs in ["h", "A", "H"]:
	os.system("rm {xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.reference{reference}.contr{contr}.root".format(xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, reference=higgs, contr=options.higgsContribution, Max=".MaxDenumerator" if options.toleranceDenumeratorMax else ""))
	os.system("hadd {xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.reference{reference}.contr{contr}.root {xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.reference{reference}.contr{contr}.mass*.root".format(xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, reference=higgs, contr=options.higgsContribution, Max=".MaxDenumerator" if options.toleranceDenumeratorMax else ""))


if options.higgsBounds:
	print "HiggsBounds method"
	os.system("rm {nllpath}/NLLHistogram.Full.root".format(nllpath=options.nllPath))
	os.system("hadd {nllpath}/NLLHistogram.Full.root {nllpath}/*/NLL*.root".format(nllpath=options.nllPath))
	
	# creating model independent histograms from 2d fits
	os.system('python HiggsAnalysis/HiggsToTauTau/scripts/multidimNLL_HiggsBounds.py --nll-path="{nllpath}/NLLHistogram.Full.root" --ggH-bbH-path="{gghbbhpath}/" --xs-path={xspath} --model={model} --mass-tolerance={tolerance} {Max} --higgs-contribution={contr} --forbidden-region-level={frlevel} --analysis={analysis} {lightVsHeavy} {expected} {weightedHB} {fullNLLSubtracted} --bg-path={BGPath}/NLLHistogram.Full.root'.format(nllpath=options.nllPath, gghbbhpath=options.ggHbbHPath, xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, contr=options.higgsContribution, Max = "--tolerance-denumerator-max" if options.toleranceDenumeratorMax else "", frlevel=options.forbiddenRegionLevel, analysis=options.analysis, lightVsHeavy="--light-vs-heavy" if options.lightVsHeavy else "", expected="--expected" if options.expected else "", weightedHB="--weighted-hb" if options.weightedHB else "", fullNLLSubtracted="--full-nll-subtracted" if options.fullNLLSubtracted else "", BGPath=options.BGPath))


elif options.SMHscale:
	print "Naive approach with SMHscale - NOT YET FULLY TESTED"
	# constructing the file with CLs histograms
	os.system("rm {nllpath}/NLLHistogram.Full.root".format(nllpath=options.nllPath))
	os.system("hadd {nllpath}/NLLHistogram.Full.root {nllpath}/*/NLL*.root".format(nllpath=options.nllPath))

	# creating model independent histograms from 2d fits
	os.system('python HiggsAnalysis/HiggsToTauTau/scripts/multidimNLL_SMHscale.py --nll-path="{nllpath}/NLLHistogram.Full.root" --ggH-bbH-path="{gghbbhpath}/" --xs-path={xspath} --model={model} --mass-tolerance={tolerance} {Max} --reference-mass={reference} --higgs-contribution={contr} --forbidden-region-level={frlevel} --analysis={analysis} {lightVsHeavy}'.format(nllpath=options.nllPath, gghbbhpath=options.ggHbbHPath, xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max = "--tolerance-denumerator-max" if options.toleranceDenumeratorMax else "", frlevel=options.forbiddenRegionLevel, analysis=options.analysis, lightVsHeavy="--light-vs-heavy" if options.lightVsHeavy else ""))
	
	
else:
	print "naive approach"
	# constructing the file with CLs histograms
	os.system("rm {nllpath}/NLLHistogram.Full.root".format(nllpath=options.nllPath))
	os.system("hadd {nllpath}/NLLHistogram.Full.root {nllpath}/*/NLL*.root".format(nllpath=options.nllPath))

	# creating model independent histograms from 2d fits
	os.system('python HiggsAnalysis/HiggsToTauTau/scripts/multidimNLL.py --nll-path="{nllpath}/NLLHistogram.Full.root" --ggH-bbH-path="{gghbbhpath}/" --xs-path={xspath} --model={model} --mass-tolerance={tolerance} {Max} --reference-mass={reference} --higgs-contribution={contr} --forbidden-region-level={frlevel} --analysis={analysis} {lightVsHeavy}'.format(nllpath=options.nllPath, gghbbhpath=options.ggHbbHPath, xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max = "--tolerance-denumerator-max" if options.toleranceDenumeratorMax else "", frlevel=options.forbiddenRegionLevel, analysis=options.analysis, lightVsHeavy="--light-vs-heavy" if options.lightVsHeavy else ""))




# starting analysis of CLs file
os.system("""root -l -b -q '$CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/macros/NLLPlot.C("{nllpath}/NLLHistogram.Full.root", "{xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.reference{reference}.contr{contr}.root", {frlevel},{higgsBounds})'""".format(nllpath=options.nllPath, xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max=".MaxDenumerator" if options.toleranceDenumeratorMax else "", frlevel=options.forbiddenRegionLevel, higgsBounds=1 if options.higgsBounds else 0))
print "---------------- first plotting script finished -----------------------"
os.system("""root -l -b -q '$CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/macros/higgsContributionsPlot.C("{xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.referenceA.contr{contr}.root", "{xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.referenceH.contr{contr}.root", "{xspath}/higgsContribution.model{model}.tolerance{tolerance}{Max}.referenceh.contr{contr}.root")'""".format(xspath=options.xsPath, model=options.model, tolerance=options.massTolerance, contr=options.higgsContribution, Max=".MaxDenumerator" if options.toleranceDenumeratorMax else ""))
print "---------------- second ploptting script finished -----------------------"

# copying produced plotfiles into the right folder
os.system("rm PLOTS-model{model}{SMHscale}-masspoint{masspoint}-tolerance{tolerance}{Max}-reference{reference}-contr{contr} -r".format(model=options.model, SMHscale="-SMHscale" if options.SMHscale else "", masspoint=options.modelMasspoint, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max="-MaxDenumerator" if options.toleranceDenumeratorMax else ""))
os.system("mkdir PLOTS-model{model}{SMHscale}-masspoint{masspoint}-tolerance{tolerance}{Max}-reference{reference}-contr{contr}".format(model=options.model, SMHscale="-SMHscale" if options.SMHscale else "", masspoint=options.modelMasspoint, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max="-MaxDenumerator" if options.toleranceDenumeratorMax else ""))
os.system("mv *.png *.pdf PLOTS-model{model}{SMHscale}-masspoint{masspoint}-tolerance{tolerance}{Max}-reference{reference}-contr{contr}".format(model=options.model, SMHscale="-SMHscale" if options.SMHscale else "", masspoint=options.modelMasspoint, tolerance=options.massTolerance, reference=options.referenceMass, contr=options.higgsContribution, Max="-MaxDenumerator" if options.toleranceDenumeratorMax else ""))


