#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# plot_slip_3d.py
#
# Example script to plot the St. Gallen slip model in 3D
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
from mpl_toolkits.mplot3d import Axes3D  # noqa
import matplotlib.cm as cm
import matplotlib.colors as colors

x, y, z, slip = np.loadtxt('StGallen_slip.txt', usecols=(4, 5, 6, 7)).T
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

norm = colors.Normalize(vmin=0.01, vmax=0.11)
cmap = cm.inferno_r
colors = cmap(norm(slip))

# decimation factor for plotting
decimate = 5
ax.scatter(
    x[::decimate], y[::decimate], z[::decimate], color=colors[::decimate])
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

plt.show()
