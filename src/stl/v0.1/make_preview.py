"""Top and side views of the exported gauges; requires NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
root=Path(__file__).resolve().parent
dtype=np.dtype([('n','<f4',(3,)),('v','<f4',(3,3)),('a','<u2')])
def view(ax,name,plane,title):
    v=np.frombuffer((root/(name+'.stl')).read_bytes(),dtype=dtype,offset=84)['v'].astype(float)
    a,b,depth={'top':(0,1,2),'side':(0,2,1)}[plane]
    n=np.cross(v[:,1]-v[:,0],v[:,2]-v[:,0]); tri=v[np.abs(n[:,depth])>1e-8]
    d=tri[:,:,depth].mean(axis=1); order=np.argsort(d if plane=='top' else -d)
    shade=plt.get_cmap('Greys')(0.25+0.6*(d[order]-d.min())/max(np.ptp(d),1e-9))
    ax.add_collection(PolyCollection(tri[order][:,:,[a,b]],facecolors=shade,edgecolors='none',antialiased=False))
    ax.autoscale();ax.margins(.06);ax.set_aspect('equal');ax.set_title(title,fontsize=10)
    ax.set_xlabel('mm');ax.set_ylabel('mm');ax.set_facecolor('#f3f5f7')
fig,axes=plt.subplots(1,3,figsize=(13,4.6),layout='constrained')
view(axes[0],'bottle_ring_93.5','top','Bottle ring 93.5 mm ID (also 92.0, 95.0)')
view(axes[1],'cup_step_gauge','side','OEM cup step gauge, side (104 → 74 mm)')
view(axes[2],'cup_step_gauge','top','Step gauge, top view')
fig.suptitle('Volvo VNL cup holder v0.1 — measurement gauges',fontsize=14)
fig.savefig(root/'preview.png',dpi=120)
