"""
Copyright (c) 2021-, rav4kumar, Haibin Wen, sunnypilot, and a number of other contributors.

This file is part of sunnypilot and is licensed under the MIT License.
See the LICENSE.md file in the root directory for more details.
"""

# Acceleration profile for maximum allowed acceleration
MAX_ACCEL_ECO     = [2.0, 2.0, 2.0, 1.38, 0.91, .53,  .42,  .31,  .085]
MAX_ACCEL_NORMAL  = [2.0, 2.0, 2.0, 1.68, 1.07, .72,  .53,  .42,  .13]
MAX_ACCEL_SPORT   = [2.0, 2.0, 2.0, 2.00, 1.34, .96,  .78,  .60,  .4]

# Acceleration profile for minimum (braking) acceleration
#MIN_ACCEL_ECO     = [-1.0, -1.0, -1.0, -1.0, -1.0]
MIN_ACCEL_ECO     = [-1.0, -1.0,  -0.74]
MIN_ACCEL_NORMAL  = [-1.0, -1.0,  -0.76]
MIN_ACCEL_SPORT   = [-1.0, -1.0,  -0.78]
MIN_ACCEL_STOCK   = [-1.2, -1.2, -1.2]

# Speed breakpoints for interpolation
MAX_ACCEL_BREAKPOINTS = [0.,  1.,  6.,  8.,   11.,  20.,  25.,  30.,  55.]
MIN_ACCEL_BREAKPOINTS = [0.,   11.1,  20.]
