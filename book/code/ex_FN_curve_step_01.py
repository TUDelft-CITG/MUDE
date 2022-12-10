import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero

# TUD Color Palette

def set_TUDstyle():
    TUcolor = {"cyan": "#00A6D6", "darkgreen": "#009B77", "purple": "#6F1D77",
               "darkred": "#A50034", "darkblue": "#0C2340",
               "orange": "#EC6842", "green": "#6CC24A",
               "lightcyan": "#00B8C8", "red": "#E03C31", "pink": "#EF60A3",
               "yellow": "#FFB81C", "blue": "#0076C2"}
    plt.rcParams.update({'axes.prop_cycle': plt.cycler(color=TUcolor.values()),
                         'font.size': 16, "lines.linewidth": 4})
    return TUcolor

# Probability density/mass function

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>") # add arrows
    ax.axis[direction].set_visible(True) # x and y from origin
    
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False) # hide borders

N_fatalities = ['0', '10', '100']
N_fatalities_loc = [0.05, 0.30, 0.66]

pdf = ['0.989', '$10^{-2}$', '$10^{-3}$']
pdf_loc = [0.99, 0.66, 0.33]

set_TUDstyle()
ax.bar(N_fatalities_loc, pdf_loc, width=0.05, color= 'lightcyan', edgecolor='k')

ax.set_xticks(N_fatalities_loc)
ax.set_xticklabels(N_fatalities)

ax.set_yticks(pdf_loc)
ax.set_yticklabels(pdf)

ax.set_title('Probability density/mass function, $f_{N}(n)$', x=0.6, y=1.0)
ax.set_xlabel('Fatalities')
ax.set_ylabel('Probability')

ax.axhline(y=0.66, xmin= 0.01, xmax= 0.40, linewidth=1, linestyle='dashed', color='k') # add dashed horizontal lines
ax.axhline(y=0.33, xmin= 0.01, xmax= 0.90, linewidth=1, linestyle='dashed', color='k')

plt.savefig('ex_FN_curve_step_01.svg')