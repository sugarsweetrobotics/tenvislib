tenvislib
=========

Tenvis Low-cost Pan-Tilt Network Camera Library for Python

This library helps to control TENVIS low-cost network camera.

## This allows
 1. change resolution
 2. change brightness / contrast
 3. flip / mirror image
 4. get status
 5. pan/tilt control (just apply velocity. This camera can not acquire current joint positions)
 6. Acquire image

## This depends on
 Python Imaging Library (PIL)

## Install
```python
$ sudo python setup.py install
```

## Example

```python
import tenvis
import Image

t = tenvis.Tenvis('192,168.1.20:7777', 'admin', 'admin')
t.camera_control(resolution=t.VGA)
t.camera_control(brightness=127)

t.videostream()

image = t.update()
image.show()
```

