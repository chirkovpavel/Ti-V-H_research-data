#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:48:42 2026

@author: chirkovpv
"""

import numpy as np
import matplotlib.pyplot as plt

f_train = np.loadtxt('res_err_train.txt')
f_t1 = np.loadtxt('res_err_test.txt')


fsize = (8,4)
fs = 10
fs_label = fs+2
fs_leg = fs
fs_ticks = fs
fs_alpha = 0.2
fs_text = fs
fs_lett = fs+6
fs_title = fs + 4
fs_stitle = fs + 8

ms_e, ms_f = 4, 2
c1 = 'tab:green'
c2 = 'tab:red'
c3 = 'dodgerblue'
c_l = 'k'
al1 = 0.5
al2 = 0.2

xlim = 9., 29
e_lim = [1.3, 4.7]
f_lim = [0.07, 0.128]


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=fsize, dpi=100) 

ax1.plot(f_train[:,0], f_train[:,1], '--d', c=c2, label='train err')
ax2.plot(f_train[:,0], f_train[:,3], '--d', c=c2)

ax1.plot(f_t1[:,0], f_t1[:,1], '-s', c=c1, label='test error')
ax2.plot(f_t1[:,0], f_t1[:,3], '-s', c=c1)

ax1.set_xticks([int(s) for s in f_t1[:,0]])
ax2.set_xticks([int(s) for s in f_t1[:,0]])


ax1.grid(True)
ax2.grid(True)

ax1.legend(loc='lower left')

ax1.set_xlabel('MTP level')
ax2.set_xlabel('MTP level')

ax1.set_ylabel('Energy RMSE (meV/at.)')
ax2.set_ylabel(r'Force RMSE (eV/$\AA$)')

ax1.grid(True, linestyle=':')
ax1.tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax2.grid(True, linestyle=':')
ax2.tick_params(axis='both', direction='in', bottom=True, right=True, left=True, top=True, labelsize=fs_ticks)

ax1.set_xlim(xlim)
ax2.set_xlim(xlim)

ax1.set_ylim(e_lim)
ax2.set_ylim(f_lim)

loc_lett = (0.87, 0.9)
ax1.annotate('(a)', loc_lett, xycoords='axes fraction', backgroundcolor='white', fontsize=fs_lett)
ax2.annotate('(b)', loc_lett, xycoords='axes fraction', backgroundcolor='white', fontsize=fs_lett)


fig.tight_layout(pad=0.5)
fig.savefig('01_MTP_err.pdf', dpi=600)
plt.show()














