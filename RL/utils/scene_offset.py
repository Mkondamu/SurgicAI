"""Shift between the authors' old SRC scene and the current SRC scene.

The phantom sits in a different place in the current SRC, so the fixed world positions
SurgicAI uses (needle reset origin, camera pose) point at empty space unless they are moved
by the same amount. The shift is measured from the Entry1 marker at start-up.

Approach and values from Akshaya Jeyaprakash's ROS 2 port (team midterm report, Oct 2026).

SURGICAI_SCENE_OFFSET:
  auto (default)  measure: Entry1 now minus Entry1 in the old scene
  0               no shift (use this for the authors' old scene)
  x,y,z           a fixed shift in metres
"""
import os
from PyKDL import Vector

# Entry1 in the authors' old SRC scene, in metres
OLD_ENTRY1 = Vector(-0.00374025404, 0.04418904781, 0.07500418425)


def scene_offset(scene):
    mode = os.environ.get('SURGICAI_SCENE_OFFSET', 'auto').strip()
    if mode == '0':
        offset = Vector(0.0, 0.0, 0.0)
    elif mode == 'auto':
        offset = scene.entry1_measured_cp().p - OLD_ENTRY1
    else:
        x, y, z = (float(v) for v in mode.split(','))
        offset = Vector(x, y, z)
    print(f'scene offset vs old SRC ({mode}): {offset}')
    return offset
