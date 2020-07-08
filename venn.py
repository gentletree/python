from matplotlib import pyplot as plt 
import numpy as  np
from matplotlib_venn import venn3, venn3_circles
import pandas as pd 
import seaborn as sns
import os
os.chdir(r'F:\树先生文件夹\课题\斑马鱼课题\斑马鱼测序整理\cleandata\veen')

sns.set(style='darkgrid')


set1=pd.read_csv('ABup.csv',header=0)
set2=pd.read_csv('ABdown.csv',header=0)
set3=pd.read_csv('ACup.csv',header=0)
set4=pd.read_csv('ACdown.csv',header=0)
set5=pd.read_csv('ADup.csv',header=0)
set6=pd.read_csv('ADdown.csv',header=0)

plt.figure(figsize=(13,5)) 
ax1=plt.subplot(121)
set1=set1.ID
set3=set3.ID
set5=set5.ID

set1=set(set1)
set3=set(set3)
set5=set(set5)

set13=set1.intersection(set3)
set15=set1.intersection(set5)
set35=set3.intersection(set5)


v=venn3([set1,set3,set5],('10ug/L vs control','50ug/L vs control','100ug/L vs control'))
c=venn3_circles([set1,set3,set5],linestyle='dashed',linewidth=1,color='dimgray')
v.get_patch_by_id('001').set_color('steelblue')
v.get_patch_by_id('011').set_color('lightskyblue')
plt.title('upregulation',y=-0.1,fontsize='15')



ax3=plt.subplot(122)
set2=set2.ID
set4=set4.ID
set6=set6.ID

set2=set(set2)
set4=set(set4)
set6=set(set6)

set24=set2.intersection(set4)
set26=set2.intersection(set6)
set46=set4.intersection(set6)

v=venn3([set2,set4,set6],('10ug/L vs control','50ug/L vs control','100ug/L vs control'))
c=venn3_circles([set2,set4,set6],linestyle='dashed',linewidth=1,color='dimgray')
v.get_patch_by_id('001').set_color('steelblue')
v.get_patch_by_id('011').set_color('lightskyblue')
plt.title('downregulation',y=-0.1,fontsize='15')



plt.savefig(r'H:\python\gene\figure\venn.pdf',dpi=400)
plt.savefig(r'H:\python\gene\figure\venn.tif',dpi=400)



plt.show()