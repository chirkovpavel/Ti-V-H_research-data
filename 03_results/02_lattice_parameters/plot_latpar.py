#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 10:35:03 2025

@author: chirkovpv
"""

import numpy as np
# import scipy.constants as spc
import matplotlib.pyplot as plt


#Cuevas data
c_V_1 = np.array([0.00249, 0.25085, 0.50112, 0.69852, 0.80044, 0.89878])
a_1 = np.array([4.45142, 4.41644, 4.37343, 4.32423, 4.29562, 4.29732])

# Nowak and Miner data:
c_V_2 = np.array([0.0413, 0.08202, 0.12107, 0.16084, 0.35181, 0.64756, 0.99879])
a_2 = np.array([4.45051, 4.43794, 4.42567, 4.41832, 4.38831, 4.32757, 4.27035])

c_V_exp = np.append(c_V_1, c_V_2)
a_exp = np.append(a_1, a_2)

res_200 = np.loadtxt('res_TiVH2_24lvl.txt')

fsize = (6, 4)
fs = 12
fs_text = fs+4
fs_ticks = fs
fs_leg = fs-4
fs_label = fs+2

c1, c2, c3, c4, c5 = 'tab:red', 'tab:green', 'dodgerblue', 'purple', 'cyan'
m1, m2, m3, m4, m5 = 'o', 'v', '^', 'd', 'x'


y_lim = [4.22, 4.46]
x_lim = [-0.05, 1.05]

# fig, ax1 = plt.subplots(nrows=1, ncols=1, dpi=200)

# ax1.plot(c_V_1, a_1, 'd', c='k', label='Exp., Cuevas 2023')
# ax1.plot(c_V_2, a_2, 's', c='k', label='Exp., Nowak 1984')
# ax1.plot(res_200[:,0], res_200[:,7], marker=m1, c=c1, lw=0., label='MD, MTP')


c_V_fit = np.linspace(0, 1.0, 100)
fit = np.polyfit(c_V_exp, a_exp, 1)
fit_200 = np.polyfit(res_200[:,0], res_200[:,7], 1)


# ax1.plot(c_V_fit, np.polyval(fit, c_V_fit), '--', c='k')
# ax1.plot(c_V_fit, np.polyval(fit_200, c_V_fit), ':', c=c1)


# ax1.grid(True, linestyle=':')
# ax1.tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

# ax1.set_xlabel('$c_V$', fontsize=fs_label)
# ax1.set_ylabel('$Ti_{1-x}V_xH_2$ lattice parameter, $\AA$', fontsize=fs_label-1)
# ax1.set_title(r'$a_0 = %6.4g - %6.4g \cdot x_V$ ' % (fit[1], abs(fit[0])))
# ax1.legend()

# ax1.set_xlim(x_lim)
# ax1.set_ylim(y_lim)

# fig.tight_layout()
# fig.savefig('01_lat_par_TiVH2.png', dpi=500)
# plt.show()


res_175 = np.loadtxt('res_TiVH1p75.txt')
res_150 = np.loadtxt('res_TiVH1p50.txt')
res_125 = np.loadtxt('res_TiVH1p25.txt')
res_100 = np.loadtxt('res_TiVH1p00.txt')

fit_175 = np.polyfit(res_175[:,0], res_175[:,7], 1)
fit_150 = np.polyfit(res_150[:,0], res_150[:,7], 1)
fit_125 = np.polyfit(res_125[:,0], res_125[:,7], 1)
fit_100 = np.polyfit(res_100[:,0], res_100[:,7], 1)


y_lim2 = [4.05, 4.475]

fig, ax1 = plt.subplots(nrows=1, ncols=1, dpi=200)

ax1.plot(c_V_1, a_1, 'd', c='k', label='Experiment, Cuevas 2023')
ax1.plot(c_V_2, a_2, 's', c='k', label='Experiment, Nowak 1984')
ax1.plot(c_V_fit, np.polyval(fit, c_V_fit), '--', c='k')

ax1.plot(res_200[:,0], res_200[:,7], marker=m1, c=c1, lw=0., label='$Ti_{1-y}V_yH_2$')
ax1.plot(res_175[:,0], res_175[:,7], marker=m2, c=c2, lw=0., label='$Ti_{1-y}V_yH_{1.75}$')
ax1.plot(res_150[:,0], res_150[:,7], marker=m3, c=c3, lw=0., label='$Ti_{1-y}V_yH_{1.50}$')
ax1.plot(res_125[:,0], res_125[:,7], marker=m4, c=c4, lw=0., label='$Ti_{1-y}V_yH_{1.25}$')
# ax1.plot(res_100[:,0], res_100[:,7], marker=m5, c=c5, lw=0., label='$Ti_{1-y}V_yH_{1.25}$')

ax1.plot(c_V_fit, np.polyval(fit_200, c_V_fit), ':', c=c1)
ax1.plot(c_V_fit, np.polyval(fit_175, c_V_fit), ':', c=c2)
ax1.plot(c_V_fit, np.polyval(fit_150, c_V_fit), ':', c=c3)
ax1.plot(c_V_fit, np.polyval(fit_125, c_V_fit), ':', c=c4)
# ax1.plot(c_V_fit, np.polyval(fit_100, c_V_fit), ':', c=c5)

ax1.set_yticks([4.1, 4.2, 4.3, 4.4])

ax1.grid(True, linestyle=':')
ax1.tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax1.set_xlabel('$c_V$', fontsize=fs_label)
ax1.set_ylabel('lattice parameter ($\AA$)', fontsize=fs_label-1)

#$Ti_{1-y}V_yH_x$

ax1.legend(fontsize=fs-4)

ax1.set_xlim(x_lim)
ax1.set_ylim(y_lim2)


fig.tight_layout()
fig.savefig('03_TiVH_lat_par.pdf', dpi=500)
plt.show()






