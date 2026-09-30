"""Draw the snap-post measuring guide (docs/measure_posts.png); requires Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyArrowPatch

GREY='#8a8f96'; DARK='#3b3f45'; RED='#d1342f'; BLUE='#1f6fd1'
def dim(ax,p,q,label,color,off=(0,0),ha='center'):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='<|-|>',mutation_scale=14,color=color,lw=2))
    ax.text((p[0]+q[0])/2+off[0],(p[1]+q[1])/2+off[1],label,color=color,fontsize=13,fontweight='bold',ha=ha,va='center')

fig,(a1,a2)=plt.subplots(1,2,figsize=(13,6.5),gridspec_kw={'width_ratios':[1,1.15]})
# Side view of one snap post on the stock holder's top flange.
a1.set_title('Side view: one snap post on top of the GREY holder body\n(the two posts that push up into the ledge holes)',fontsize=12)
a1.add_patch(Rectangle((-30,-6),60,6,color=GREY))
a1.text(0,-3,'top flange of the holder',ha='center',va='center',color='white',fontsize=10)
post=[(-5,0),(-5,12),(-6.5,15),(-6.5,18),(-4,21),(4,21),(6.5,18),(6.5,15),(5,12),(5,0)]
a1.add_patch(Polygon(post,color=DARK))
a1.add_patch(Rectangle((-0.8,9),1.6,12.2,color='white'))
a1.text(9,6,'post',fontsize=10,color=DARK)
a1.text(9,19.5,'barb (catch)',fontsize=10,color=DARK)
a1.text(-1,22.5,'slot',fontsize=9,color=DARK,ha='center')
dim(a1,(-14,0),(-14,21),'A',RED,off=(-2.5,0))
a1.plot([-15,-5],[21,21],color=RED,lw=1,ls=':'); a1.plot([-15,-5],[0,0],color=RED,lw=1,ls=':')
dim(a1,(-5,4),(5,4),'B',BLUE,off=(0,-2.2))
dim(a1,(-6.5,16.5),(6.5,16.5),'C',RED,off=(9,0),ha='left')
a1.set_xlim(-32,32); a1.set_ylim(-22,27); a1.set_aspect('equal'); a1.axis('off')
a1.text(-31,-10,'A = height, flange face to the tip\nB = post diameter at the base (do not squeeze it)\nC = widest point at the barb',fontsize=11,va='top')
# Underside of the dash ledge, looking up at the hole row.
a2.set_title('Looking up at the underside of the dash ledge',fontsize=12)
a2.add_patch(Rectangle((-10,-12),150,24,color='#c9ccd1'))
for i,x in enumerate(range(0,151,38)[:3]):
    a2.add_patch(Circle((x+10,0),5.75,color='#222'))
dim(a2,(10,8),(48,8),'D = 75.5 mm (done)',GREY,off=(0,3.2))
a2.text(-9,-20,'D = neighbouring holes, center to center: 75.5 mm (measured)',fontsize=11,va='top')
a2.set_xlim(-12,142); a2.set_ylim(-32,20); a2.set_aspect('equal'); a2.axis('off')
fig.suptitle('Cup holder snap posts: what to measure (A, B, C)',fontsize=15,fontweight='bold')
fig.savefig(Path(__file__).with_name('measure_posts.png'),dpi=110,bbox_inches='tight')
