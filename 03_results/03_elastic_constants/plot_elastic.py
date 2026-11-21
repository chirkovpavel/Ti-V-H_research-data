#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:32:58 2026

@author: chirkovpv
"""
import numpy as np
import matplotlib.pyplot as plt


def calc_vrh(dd):
    B_vrh = (dd[:,1] + 2*dd[:,2]) / 3
    G_v = (dd[:,1] - dd[:,2] + 3*dd[:,3]) / 5
    G_r =  5*(dd[:,1]-dd[:,2])*dd[:,3]/(4*dd[:,3]+3*(dd[:,1] - dd[:,2]))
    G_vrh = (G_v + G_r) / 2
    mu = 0.5 * (3*B_vrh - 2 * G_vrh) / (3*B_vrh + G_vrh)
    return {'B' : B_vrh, 'G_v' : G_v, 'G_r' : G_r, 'G_vrh' : (G_v+G_r)/2, 'mu' : mu}

res_200 = np.loadtxt('elastic_const_H_2_00.txt')
res_175 = np.loadtxt('elastic_const_H_1_75.txt')
res_150 = np.loadtxt('elastic_const_H_1_50.txt')
res_125 = np.loadtxt('elastic_const_H_1_25.txt')
res_100 = np.loadtxt('elastic_const_H_1_00.txt')

fsize = (9,8)
fs = 11
fs_text = fs+4
fs_ticks = fs
fs_leg = fs-4
fs_label = fs+2
fs_lett = fs+6

c1, c2, c3, c4, c5 = 'tab:red', 'tab:green', 'dodgerblue', 'purple', 'cyan'
m1, m2, m3, m4, m5 = 'o', 'v', '^', 'd', 'x'

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=fsize, dpi=200)

ax[0,0].plot(res_200[:,0], res_200[:,1], marker=m1, c=c1)
ax[0,1].plot(res_200[:,0], res_200[:,2], marker=m1, c=c1, label='H=2.0')
ax[0,2].plot(res_200[:,0], res_200[:,3], marker=m1, c=c1)

ax[0,0].plot(res_175[:,0], res_175[:,1], marker=m2, c=c2)
ax[0,1].plot(res_175[:,0], res_175[:,2], marker=m2, c=c2, label='H=1.75')
ax[0,2].plot(res_175[:,0], res_175[:,3], marker=m2, c=c2)

ax[0,0].plot(res_150[:,0], res_150[:,1], marker=m3, c=c3)
ax[0,1].plot(res_150[:,0], res_150[:,2], marker=m3, c=c3, label='H=1.50')
ax[0,2].plot(res_150[:,0], res_150[:,3], marker=m3, c=c3)

ax[0,0].plot(res_125[:,0], res_125[:,1], marker=m4, c=c4)
ax[0,1].plot(res_125[:,0], res_125[:,2], marker=m4, c=c4, label='H=1.25')
ax[0,2].plot(res_125[:,0], res_125[:,3], marker=m4, c=c4)

# ax1.plot(res_100[:,0], res_100[:,1], marker=m5, c=c5)
# ax2.plot(res_100[:,0], res_100[:,2], marker=m5, c=c5, label='H=1.0')
# ax3.plot(res_100[:,0], res_100[:,3], marker=m5, c=c5)

ax[0,0].grid(True, linestyle=':')
ax[0,0].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax[0,1].grid(True, linestyle=':')
ax[0,1].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax[0,2].grid(True, linestyle=':')
ax[0,2].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax[0,1].legend(loc=(0.025, 0.5))

# ax2.set_xlabel('$x_V$', fontsize=fs_label)
ax[0,0].set_ylabel('elastic constants, GPa', fontsize=fs_label)

lett_coord = [0.07,0.91]
ax[0,0].annotate('(a)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
ax[0,1].annotate('(b)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
ax[0,2].annotate('(c)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
ax[1,0].annotate('(d)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
ax[1,1].annotate('(e)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
ax[1,2].annotate('(f)', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')

# ax[0,1].annotate('$C_{12}$', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
# ax[0,2].annotate('$C_{44}$', lett_coord, xycoords='axes fraction', fontsize=fs_lett, backgroundcolor='w')
# fig.tight_layout()
# fig.savefig('04_TiVH_elastic_const.png', dpi=1000)
# plt.show()


vrh_200 = calc_vrh(res_200)
vrh_175 = calc_vrh(res_175)
vrh_150 = calc_vrh(res_150)
vrh_125 = calc_vrh(res_125)
vrh_100 = calc_vrh(res_100)

# fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=fsize, dpi=200)

ax[1,0].plot(res_200[:,0], res_200[:,1]/res_200[:,2], marker=m1, c=c1)
ax[1,1].plot(res_200[:,0], vrh_200['B'], marker=m1, c=c1, label='H=2.0')
ax[1,2].plot(res_200[:,0], vrh_200['G_vrh'], marker=m1, c=c1)

ax[1,0].plot(res_175[:,0], res_175[:,1]/res_175[:,2], marker=m2, c=c2)
ax[1,1].plot(res_175[:,0], vrh_175['B'], marker=m2, c=c2, label='H=1.75')
ax[1,2].plot(res_175[:,0], vrh_175['G_vrh'], marker=m2, c=c2)

ax[1,0].plot(res_150[:,0], res_150[:,1]/res_150[:,2], marker=m3, c=c3)
ax[1,1].plot(res_150[:,0], vrh_150['B'], marker=m3, c=c3, label='H=1.50')
ax[1,2].plot(res_150[:,0], vrh_150['G_vrh'], marker=m3, c=c3)

ax[1,0].plot(res_125[:,0], res_125[:,1]/res_125[:,2], marker=m4, c=c4)
ax[1,1].plot(res_125[:,0], vrh_125['B'], marker=m4, c=c4, label='H=1.25')
ax[1,2].plot(res_125[:,0], vrh_125['G_vrh'], marker=m4, c=c4)

# ax1.plot(res_100[:,0], res_100[:,1]/res_100[:,2], marker=m5, c=c5)
# ax2.plot(res_100[:,0], vrh_100['B'], marker=m5, c=c5, label='H=1.00')
# ax3.plot(res_100[:,0], vrh_100['G_vrh'], marker=m5, c=c5)

ax[1,0].grid(True, linestyle=':')
ax[1,0].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax[1,1].grid(True, linestyle=':')
ax[1,1].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax[1,2].grid(True, linestyle=':')
ax[1,2].tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

# ax[1,1].legend(loc='upper left')

ax[1,1].set_xlabel('$x_V$', fontsize=fs_label+4)

ax[0,0].set_ylabel('$C_{11}$ (GPa)', fontsize=fs_label)
ax[0,1].set_ylabel('$C_{12}$ (GPa)', fontsize=fs_label)
ax[0,2].set_ylabel('$C_{44}$ (GPa)', fontsize=fs_label)

ax[1,0].set_ylabel('$C_{11}/C_{12}$', fontsize=fs_label)
ax[1,1].set_ylabel('$B_{VRH}$ (GPa)', fontsize=fs_label)
ax[1,2].set_ylabel('$G_{VRH}$ (GPa)', fontsize=fs_label)


fig.tight_layout(pad=0.1)
fig.savefig('04_TiVH_elastic.pdf', dpi=500)
plt.show()






# y_lim = [4.22, 4.46]
# x_lim = [-0.05, 1.05]

# B_vrh = (res[:,1] + 2*res[:,2]) / 3
# G_v = (res[:,1] - res[:,2] + 3*res[:,3]) / 5
# G_r =  5*(res[:,1]-res[:,2])*res[:,3]/(4*res[:,3]+3*(res[:,1] - res[:,2]))
# G_vrh = (G_v + G_r) / 2

#Poisson coeff
# mu = 0.5 * (3*B_vrh - 2 * G_vrh) / (3*B_vrh + G_vrh)
