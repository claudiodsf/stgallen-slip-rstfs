#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# plot_slip.py
#
# Example script to plot the St. Gallen slip model
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

strike, dip, slip = np.loadtxt('StGallen_slip.txt', usecols=(0, 1, 7)).T
extent = min(strike), max(strike), min(dip), max(dip)
slip = slip.reshape(141, 141)

fig, ax = plt.subplots()
ax.set_xlabel('Along strike (m)')
ax.set_ylabel('Along dip (m)')
vmin = 0.01
vmax = 0.11
slip[slip <= vmin] = np.nan
im = ax.imshow(
    slip, extent=extent, origin='lower', cmap='inferno_r',
    vmin=vmin, vmax=vmax)
fig.colorbar(im, label='slip (m)')
plt.show()
