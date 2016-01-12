#!/bin/zsh
python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-bg-only-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-bg-only-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-300fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-300fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-3000fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-3000fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-25-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-25-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-20-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-20-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-10-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-10-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-130-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-130-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-200-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-200-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-300-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-300-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-400-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-400-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-600-15-30fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-600-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-30fb-A+H/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-30fb-A+H/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-30fb-A+H/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-30fb-A+H/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-30fb-h/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-30fb-h/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-30fb-h/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-30fb-h/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-30fb/plain-SMHbkg-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-30fb/plain-SMHbkg-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-300fb/plain-SMHbkg-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-300fb/plain-SMHbkg-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-300fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-300fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-3000fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-3000fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150428-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS150512-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150512-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS150527-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150527-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --forbidden-region-level=95 --nll-path="$CMSSW_BASE/src/LIMITS150526-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150526-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS150525-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150525-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS150524-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150524-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS150608-mssm/bbb-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS150608-mssm/bbb-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-30fb/plain-asimov-mhmodp-NLL/mt/" --mass-tolerance=0.2 --tolerance-denumerator-max && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-30-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"

#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-05-30fb/plain-asimov-mhmodp-NLL/mt/" --mass-tolerance=0.2 --tolerance-denumerator-max && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-500-05-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-130-15-30fb/plain-asimov-mhmodp-NLL/mt/" --mass-tolerance=0.2 --tolerance-denumerator-max && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-130-15-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"
#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-BG-Only-30fb/plain-asimov-mhmodp-NLL/mt/" --mass-tolerance=0.2 --tolerance-denumerator-max && submit.py --multidim-fit --stable --physics-model='ggH-bbH' LIMITS-150707-mssm-BG-Only-30fb/plain-asimov-ggH-bbH/* --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null"


#python $CMSSW_BASE/src/HiggsAnalysis/HiggsToTauTau/scripts/adjust_mssm_boundaries.py --nll-path="$CMSSW_BASE/src/LIMITS-150707-mssm-500-30-300fb/plain-asimov-mhmodp-NLL/mt/" && submit.py --multidim-fit --stable --physics-model='ggH-bbH-SMH' --SMHscale="1" LIMITS-150707-mssm-500-30-300fb/plain-MSSMvsSM-asimov-ggH-bbH/500 --lxq --queue="-l h_vmem=2000M -l h_rt=12:00:00 -j y -o /dev/null" 
