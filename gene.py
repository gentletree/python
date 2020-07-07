import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import pandas as pd
wb = pd.read_excel(r'C:\Users\Administrator\Desktop\AAA.xlsx',1,name=['foldchange','qvalue'])
data = pd.DataFrame(wb)
fold=data['foldchange']
qv=data['qvalue']
# print (fold)
# print (qv)
# fold['a']= range(len(fold))
# fold = fold.set_index('a')

result = pd.concat([fold, qv],axis=1,ignore_index=True)

result.columns = ['foldchange','qvalue']

result['log(qvalue)'] = -np.log30(result['qvalue'])
##########
result['sig'] = 'normal'

result['size']  =np.abs(result['foldchange'])/100
 
result.loc[(result.foldchange> 1 )&(result.qvalue < 0.05),'sig'] = 'up'
result.loc[(result.foldchange< -1 )&(result.qvalue < 0.05),'sig'] = 'down'

######
ax = sns.scatterplot(x="foldchange", y="log(qvalue)",
    hue='sig',
    hue_order = ('down','normal','up'),
    palette=("#377EB8","grey","#E41A1C"),
    data=result)
ax.set_ylabel('-log(qvalue)',fontweight='bold')
ax.set_xlabel('FoldChange',fontweight='bold')
plt.show()