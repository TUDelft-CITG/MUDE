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

# FN curve

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(axes_class=AxesZero)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>") # add arrows
    ax.axis[direction].set_visible(True) # x and y from origin
    
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False) # hide borders
    
N_fatalities = ['0', '10', '100','100']
N_fatalities_loc = [0.03,0.33, 0.95, 0.95]

pdf = ['0','$1.1 * 10^{-2}$', '$10^{-3}$','0']
pdf_loc = [0.03,0.99, 0.66, 0.03]

ax.step(N_fatalities_loc, pdf_loc, color= 'darkblue',linewidth=4)

ax.set_xticks(N_fatalities_loc)
ax.set_xticklabels(N_fatalities)

ax.set_yticks(pdf_loc)
ax.set_yticklabels(pdf)

ax.set_title('FN curve, $f_{N}(x) = P(N \leq n)$', x=0.75, y=1.1)
ax.set_xlabel('Fatalities')
ax.set_ylabel('Probability')

plt.savefig('ex_FN_curve_step_03.svg')