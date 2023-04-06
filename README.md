# Spikemut
Average Treatment Effect Estimation of Spike Mutations of SARS-CoV-2 Based on Causal Inference, as presented in the paper "_Evaluating the Effect of SARS-CoV-2 Spike Mutations by Causal Inference Models_".
 

**Setting**

Recommended: Python=3.8.0, EconML=0.10.0

**Input**

1. CSV file as "input_example.csv".
2. Each row represents a viral mutation combination.
3. Each column represents the value of R0 (the last column) or the bool of a mutation (otherwise).

**Guidance**

1. Prepare the input feature matrix ("input_example.csv").
2. Run the code ("EffectEstimation.py").
3. Obtain the output ATE.csv as the effect score.


**Note**

1. Replicant rows have no impact on the estimation.
2. For sound estimations, all mutations must have presence and non-presence acorss all rows/samples, otherwise error.
3. Unlike other muations that both have presence and non-presence, the D614G mutation occurs in almost all sequences. In case of errors like "AttributeError: Provided crossfit folds contain training splits that don't contain all treatments" due to D614G, the row for wildtypes is recommended to have two occurences.


**Supplementary Files**

1. Effect scores and validations of all 107 estimated mutations: Supplementary_EffectScore.csv.
2. Detailed information of genome sequences from GISAID Website: (csv file compressed as 7z file) Supplementary_FastaID.7z.001 - Supplementary_FastaID.7z.004
