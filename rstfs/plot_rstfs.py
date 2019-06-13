#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# plot_rstfs.py
#
# Example script to plot Relative Source Time Functions (rstfs)
#
# (c) 2019 Claudio Satriano <satriano@ipgp.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import numpy as np
import matplotlib.pyplot as plt


stations = ('SGT00', 'SGT02', 'SGT03', 'SGT04', 'SGT05', 'SGT06')
waves = ('P', 'SE', 'SN')
egfs = ('EGF1', 'EGF2')
colors = {
    'EGF1': '#1f77b4',
    'EGF2': '#ff7f0e',
}

fig, axes = plt.subplots(6, 3, figsize=(16, 9), sharex=True, sharey=True)
for n, wave in enumerate(waves):
    for m, station in enumerate(stations):
        ax = axes[m, n]
        ax.set_xlim(0, 0.4)
        cut_file = 'cut_times.txt'
        for line in open(cut_file):
            w = line.split()
            if w[0] == station:
                cut_time_P = float(w[1])
                cut_time_S = float(w[2])
        if wave == 'P':
            cut_time = cut_time_P
        else:
            cut_time = cut_time_S
        ax.axvline(cut_time, color='black')
        for egf in egfs:
            rstf_file = '{}.{}.{}.txt'.format(station, wave, egf)
            time, rstf = np.loadtxt(rstf_file).T
            label = '{}.{}.{}'.format(station, wave, egf)
            ax.plot(time, rstf, color=colors[egf], label=label)
            ax.legend()
    ax.set_xlabel('Time (s)')
axes[-1, 0].set_ylabel('Moment rate (Nm/s)')
plt.show()
