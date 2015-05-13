#!/usr/bin/env python
import ROOT as r
from array import array
import sys as s
import os
import glob as g
import math
from HiggsAnalysis.HiggsToTauTau.utils import get_mass
### Creating 2-dim histogram in the (mA, tanb) plane
#masslist = array('d',(90, 100, 110, 120, 125, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050) )
masslist = array('d', (90+10*m for m in range(93)))
#fulltanblist = array('d', (0.50, 0.60, 0.70, 0.80, 0.90, 1.00, 2.00, 3.00, 4.00, 6.00, 8.00, 9.00, 10.00, 12.00, 13.00, 15.00, 16.00, 19.00, 20.00, 22.00, 25.00, 30.00, 35.00, 40.00, 45.00, 50.00, 55.00, 60.00, 65.00))
fulltanblist = array('d', (x for x in range(1,62)))
masspoints = len(masslist)-1
fulltanbpoints = len(fulltanblist)-1

# histograms with asymptotic calculation

CLsHist2D_as = r.TH2D('CLsHist2D_as', r'CL_{s} values for (m_{A}, tan#beta) plane (asymptotic); m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
CLsbHist2D_as = r.TH2D('CLsbHist2D_as', r'CL_{s+b} values for (m_{A}, tan#beta) plane (asymptotic); m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
CLbHist2D_as = r.TH2D('CLbHist2D_as', r'CL_{b} values for (m_{A}, tan#beta) plane (asymptotic); m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
qmuHist2D_as = r.TH2D('qmuHist2D_as', r'q_{#mu} values for (m_{A}, tan#beta) plane (asymptotic); m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
qAHist2D_as = r.TH2D('qAHist2D_as', r'q_{A} values for (m_{A}, tan#beta) plane (asymptotic); m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

# histograms with step by step calculation
CLsHist2D = r.TH2D('CLsHist2D', r'CL_{s} values for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
CLsbHist2D = r.TH2D('CLsbHist2D', r'CL_{s+b} values for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
CLbHist2D = r.TH2D('CLbHist2D', r'CL_{b} values for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
qmuHist2D = r.TH2D('qmuHist2D', r'q_{#mu} values for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
qAHist2D = r.TH2D('qAHist2D', r'q_{A} values for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

NLLmuFixedforqmu = r.TH2D('NLLmuFixedforqmu', r'full NLL values of q_{#mu} with #mu fixed for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
NLLmuGlobalforqmu = r.TH2D('NLLmuGlobalforqmu', r'global fit NLL values of q_{#mu} for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
NLLmuFixedforqA = r.TH2D('NLLmuFixedforqA', r'full NLL values of q_{A} with #mu fixed for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
NLLmuGlobalforqA = r.TH2D('NLLmuGlobalforqA', r'global fit NLL values of q_{A} for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

# histograms with Crossection x BR values for ggH & bbH production mode and the Higgses A, H, h

ggAXsBR = r.TH2D('ggAXsBR', r'#sigma(ggA)#upointBR(A#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
ggHXsBR = r.TH2D('ggHXsBR', r'#sigma(ggH)#upointBR(H#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
gghXsBR = r.TH2D('gghXsBR', r'#sigma(ggh)#upointBR(h#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

bbAXsBR = r.TH2D('bbAXsBR', r'#sigma(bbA)#upointBR(A#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
bbHXsBR = r.TH2D('bbHXsBR', r'#sigma(bbH)#upointBR(H#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
bbhXsBR = r.TH2D('bbhXsBR', r'#sigma(bbh)#upointBR(h#rightarrow#tau#tau) [pb] for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

# histograms for mass differences between the scalar Higgses h, H and the pseudoscalar Higgs A

massDiffh = r.TH2D('massDiffh', '|(m_{A}-m_{h})/m_{A}| for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)
massDiffH = r.TH2D('massDiffH', '|(m_{A}-m_{H})/m_{A}| for (m_{A}, tan#beta) plane; m_{A}; tan#beta', masspoints, masslist, fulltanbpoints, fulltanblist)

### Searching for relevant files: batch_*.root
filelist = g.glob('batch_*.root')
tanblist = []
rmaxlist = []
for filename in filelist:
	filename = (filename.replace('batch_', '')).replace('.root','')
	tanblist.append(filename)

#logfile = open('logfile.txt', 'w+')

### Determining mass from directory
directory = os.getcwd()
mass = get_mass(directory)
for i in range(len(tanblist)):
	tanb = tanblist[i]
	rMax = "{tanb}".format(tanb=(float(tanb)+10))
	### Asymptotic CLs calculation.

	os.system("combine -M Asymptotic --minimizerStrategy=0 --minimizerTolerance=0.01 --singlePoint {tanb} batch_{tanb}.root -n tanb_{tanb} -m {mass} --rMin=0 --rMax={rMax} > tmpNLL.txt".format(tanb=tanb, mass=mass, rMax=rMax))

	# Extracting values from asymptotic calculation
	File = open('tmpNLL.txt', 'r')
	as_data = File.readlines()
	quantities_line = ''
	for line in as_data:
		if (line.find('At r =') > -1): quantities_line = line
	
	#print "Current tanb value: ", tanb
	#print quantities_line
	if not (quantities_line.find('nan') > -1):
		qmu_as_string = quantities_line[quantities_line.find('q_mu'):quantities_line.find('q_A')]
		qA_as_string = quantities_line[quantities_line.find('q_A'):quantities_line.find('CLsb')]
		CLsb_as_string = quantities_line[quantities_line.find('CLsb'):quantities_line.find('CLb')]
		CLs_as_string = quantities_line.replace('CLsb', '')
		CLb_as_string = quantities_line[CLs_as_string.find('CLb'):CLs_as_string.find('CLs')]
		CLs_as_string = CLs_as_string[CLs_as_string.find('CLs'):]

		qmu_as = float(qmu_as_string.replace(' ', '').split('=')[1])
		qA_as = float(qA_as_string.replace(' ', '').split('=')[1])
		CLsb_as = float(CLsb_as_string.replace(' ', '').split('=')[1])
		CLb_as = float(CLb_as_string.replace(' ', '').split('=')[1])
		CLs_as = float(CLs_as_string.replace(' ', '').split('=')[1])

		#print qmu_as
		#print qA_as
		#print CLsb_as
		#print CLb_as
		#print CLs_as

		qmuHist2D_as.Fill(float(mass), float(tanb), qmu_as)
		qAHist2D_as.Fill(float(mass), float(tanb), qA_as)
		CLsbHist2D_as.Fill(float(mass), float(tanb), CLsb_as)
		CLbHist2D_as.Fill(float(mass), float(tanb), CLb_as)
		CLsHist2D_as.Fill(float(mass), float(tanb), CLs_as)
		#logfile.write("There are NaN values during asymptotic calculation at point ({mass},{tanb}). Skipping also the by hand calculation.#\n".format(mass=mass, tanb=tanb))
	#else: 
	#	continue
	### Calculation of CLs by hand.

	# First: CLsb calculation from data set
	os.system("combine -n FitToData.tanb_{tanb} -M MultiDimFit --rMin=0 --rMax={rMax} --minimizerStrategy=0 --minimizerTolerance=0.01 --cminFallbackAlgo 'Minuit2,0:0.1' --saveNLL --setPhysicsModelParameters r={tanb} --algo fixed batch_{tanb}.root -m {mass}".format(tanb=tanb, mass=mass, rMax=rMax))

	# Second: Toy production for post-fit of the asimov set
	os.system("combine -n PostFitToy.tanb_{tanb} -M MultiDimFit --rMin=0 --rMax={rMax} --minimizerStrategy=0 --minimizerTolerance=0.01 --cminFallbackAlgo 'Minuit2,0:0.1' -t -1 --toysFrequentist --expectSignal 0 --saveToys --saveWorkspace batch_{tanb}.root -m {mass}".format(tanb=tanb, mass=mass, rMax=rMax))

	# Third: CLb calculation from asimov set using produced toys
	os.system("combine -n FitToAsimov.tanb_{tanb} -M MultiDimFit --rMin=0 --rMax={rMax} --minimizerStrategy=0 --minimizerTolerance=0.01 --cminFallbackAlgo 'Minuit2,0:0.1' --saveNLL  --setPhysicsModelParameters r={tanb} --algo fixed  -d higgsCombinePostFitToy.tanb_{tanb}.MultiDimFit.mH{mass}.123456.root -w w --snapshotName 'MultiDimFit' --toysFile higgsCombinePostFitToy.tanb_{tanb}.MultiDimFit.mH{mass}.123456.root -t -1 --toysFrequentist --bypassFrequentistFit -m {mass}".format(tanb=tanb, mass=mass, rMax=rMax))

	ROOTFile1 = r.TFile("higgsCombineFitToData.tanb_{tanb}.MultiDimFit.mH{mass}.root".format(tanb=tanb, mass=mass))
	ROOTFile2 = r.TFile("higgsCombineFitToAsimov.tanb_{tanb}.MultiDimFit.mH{mass}.root".format(tanb=tanb, mass=mass))

	### Extracting L(mu^) and L(mu=1) values for data and asimov.

	# Data

	t1 = ROOTFile1.Get("limit")
	nll_list_data = []
	nll0_list_data = []
	r_list_data = []
	for event in t1:
		nll_list_data.append(event.nll)
		nll0_list_data.append(event.nll0)
		r_list_data.append(event.r)

	global_NLL_mu_data = nll0_list_data[1]
	if not math.isnan(global_NLL_mu_data): NLLmuGlobalforqmu.Fill(float(mass), float(tanb), global_NLL_mu_data)
	#print "global NLL(mu): ", global_NLL_mu_data


	NLL_mu1_data = nll_list_data[1]
	if not math.isnan(NLL_mu1_data): NLLmuFixedforqmu.Fill(float(mass), float(tanb), NLL_mu1_data)
	#print "NLL(mu) for mu: ", NLL_mu1_data

	# Asimov

	t2 = ROOTFile2.Get("limit")
	nll_list_asimov = []
	nll0_list_asimov = []
	r_list_asimov = []
	for event in t2:
		nll_list_asimov.append(event.nll)
		nll0_list_asimov.append(event.nll0)
		r_list_asimov.append(event.r)

	global_NLL_mu_asimov = nll0_list_asimov[1]
	if not math.isnan(global_NLL_mu_asimov): NLLmuGlobalforqA.Fill(float(mass), float(tanb), global_NLL_mu_asimov)
	#print "global NLL(mu) for asimov: ", global_NLL_mu_asimov


	NLL_mu1_asimov = nll_list_asimov[1]
	if not math.isnan(NLL_mu1_asimov): NLLmuFixedforqA.Fill(float(mass), float(tanb), NLL_mu1_asimov)
	#print "NLL(mu) for mu=1.0 for asimov: ", NLL_mu1_asimov

	### Calculation of values for CLs

	# q_mu for data
	q_mu = 2*(NLL_mu1_data - global_NLL_mu_data)
	if abs(q_mu) < 0.1 and q_mu < 0: q_mu = 0
	#if q_mu < 0: q_mu = 0
	#print "q_mu = ", q_mu
	if not math.isnan(q_mu): qmuHist2D.Fill(float(mass), float(tanb), q_mu)
	# CLsb for data using asymptotic formula
	CL_SplusB = 1 - r.Math.normal_cdf(r.TMath.Sqrt(q_mu))
	if not math.isnan(CL_SplusB): CLsbHist2D.Fill(float(mass), float(tanb), CL_SplusB)
	#print "CLsb = ", CL_SplusB

	#q_A for asimov
	q_A = 2*(NLL_mu1_asimov - global_NLL_mu_asimov)
	if abs(q_A) < 0.1 and q_A < 0: q_A = 0
	#if q_A < 0: q_A = 0
	#print "q_A = ", q_A
	if not math.isnan(q_A): qAHist2D.Fill(float(mass), float(tanb), q_A)
	# CLb for asimov using asymptotic formula
	CL_B = r.Math.normal_cdf(r.TMath.Sqrt(q_A)-r.TMath.Sqrt(q_mu))
	if not math.isnan(CL_B): CLbHist2D.Fill(float(mass), float(tanb), CL_B)
	#print "CLb = ", CL_B

	# CLs value
	if CL_B == 0:
		CL_S = 0
	else:
		CL_S = CL_SplusB/CL_B
	#print "CLs = ", CL_S
	if not math.isnan(CL_S): CLsHist2D.Fill(float(mass), float(tanb), CL_S)
	#if math.isnan(CL_S):
		#logfile.write("NaN value for CLs at the point ({mass},{tanb})\n".format(mass=mass, tanb=tanb))

	### Filling the Crossection x BR histograms
	os.system("root -l -b -q '$CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/macros/mssm_xs.C(\"$CMSSW_BASE/src/auxiliaries/models/out.mhmodp-8TeV-tanbHigh-nnlo.root\", {mass}, {tanb})' > XsBr.txt".format(mass=mass, tanb=tanb))
	File2 = open('XsBr.txt', 'r')
	xs_data = File2.readlines()

	ggA_string = ''
	ggH_string = ''
	ggh_string = ''

	bbA_string = ''
	bbH_string = ''
	bbh_string = ''
	
	massH_string = ''
	massh_string = ''
	
	for line in xs_data:
		if (line.find('-> xsec(ggA)(tautau): ') > -1): ggA_string = line
		elif (line.find('-> xsec(ggH)(tautau): ') > -1): ggH_string = line
		elif (line.find('-> xsec(ggh)(tautau): ') > -1): ggh_string = line
		elif (line.find('-> xsec(bbA)(tautau): ') > -1): bbA_string = line
		elif (line.find('-> xsec(bbH)(tautau): ') > -1): bbH_string = line
		elif (line.find('-> xsec(bbh)(tautau): ') > -1): bbh_string = line
		elif (line.find('Mass H: ') > -1): massH_string = line
		elif (line.find('Mass h: ') > -1): massh_string = line

	ggA = float(ggA_string.replace('-> xsec(ggA)(tautau): ', ''))
	ggH = float(ggH_string.replace('-> xsec(ggH)(tautau): ', ''))
	ggh = float(ggh_string.replace('-> xsec(ggh)(tautau): ', ''))

	bbA = float(bbA_string.replace('-> xsec(bbA)(tautau): ', ''))
	bbH = float(bbH_string.replace('-> xsec(bbH)(tautau): ', ''))
	bbh = float(bbh_string.replace('-> xsec(bbh)(tautau): ', ''))
	
	massH = float(massH_string.replace('Mass H: ',''))
	massh = float(massh_string.replace('Mass h: ',''))
	
	mdiffH = abs((float(mass)-massH)/float(mass))
	mdiffh = abs((float(mass)-massh)/float(mass))

	ggAXsBR.Fill(float(mass), float(tanb), ggA)
	ggHXsBR.Fill(float(mass), float(tanb), ggH)
	gghXsBR.Fill(float(mass), float(tanb), ggh)

	bbAXsBR.Fill(float(mass), float(tanb), bbA)
	bbHXsBR.Fill(float(mass), float(tanb), bbH)
	bbhXsBR.Fill(float(mass), float(tanb), bbh)
	
	massDiffH.Fill(float(mass), float(tanb), mdiffH)
	massDiffh.Fill(float(mass), float(tanb), mdiffh)
### Creating a file containing the 2-dim histograms
histFile = r.TFile("NLLHistogram.mA{mass}.root".format(mass=mass), "RECREATE")

CLsHist2D.Write()
CLsbHist2D.Write()
CLbHist2D.Write()
qmuHist2D.Write()
qAHist2D.Write()

NLLmuFixedforqmu.Write()
NLLmuGlobalforqmu.Write()
NLLmuFixedforqA.Write()
NLLmuGlobalforqA.Write()

CLsHist2D_as.Write()
CLsbHist2D_as.Write()
CLbHist2D_as.Write()
qmuHist2D_as.Write()
qAHist2D_as.Write()

ggAXsBR.Write()
ggHXsBR.Write()
gghXsBR.Write()

bbAXsBR.Write()
bbHXsBR.Write()
bbhXsBR.Write()

massDiffH.Write()
massDiffh.Write()

histFile.Close()
#logfile.close()