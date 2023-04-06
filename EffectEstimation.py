import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from econml.dr import LinearDRLearner #econml=0.10.0
import shap
import warnings
warnings.filterwarnings("ignore")

dir='./'
shapdir='./'
est=LinearDRLearner()

def ecnoml_train(train_data_file):
    train_data = pd.read_csv(train_data_file) # feature matrix
    new_mutspace=train_data.columns.values[:-1] #list of mutations
    effect_list=[]
    for mutindex,mut in enumerate(new_mutspace):
        print(mut)
        #ATE via causal inference
        Y = train_data['R0']
        T = train_data[mut]
        X = train_data.drop(columns=[mut,'R0'])
        est.fit(Y=Y, T=T, W=X)
        mut_effect=est.ate(T0=0, T1=1)
        effect_list.append(mut_effect)

    header='Mutation,Effect Score'
    effect_array=np.array(effect_list,dtype='str')
    effect_merge_matrix=np.hstack((new_mutspace.reshape((-1,1)),effect_array.reshape((-1,1))))
    np.savetxt(dir+'ATEs.csv',effect_merge_matrix,fmt='%s',delimiter=',',newline='\n',header=header,comments='')
    print('ATE estimation complete.\n')


if __name__ == '__main__':
    ecnoml_train(train_data_file=dir+'input_example.csv')




