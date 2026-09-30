"""Top and side views of the exported mount tests; requires NumPy and Matplotlib."""
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
fig,axes=plt.subplots(2,2,figsize=(12,6.5),layout='constrained')
view(axes[0,0],'pitch_strip','top','Pitch strip, top: posts 75.5 mm apart')
view(axes[1,0],'pitch_strip','side','Pitch strip, side: 17.5 mm split posts')
view(axes[0,1],'post_fit','top','Post fit, top: barbs 11.8 / 12.2 / 12.6 mm')
view(axes[1,1],'post_fit','side','Post fit, side')
fig.suptitle('Volvo VNL cup holder v0.2 — mount test pieces',fontsize=14)
fig.savefig(root/'preview.png',dpi=120)
