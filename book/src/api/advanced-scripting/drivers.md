# Drivers

Drivers can be used with geometry nodes. To create a scripted expression driver, use the `scripted_expression` convenience function.

This can be used to get information like the current frame number in a Geometry Script.

```python
frame_number = scripted_expression("frame")
frame_number_doubled = scripted_expression("frame * 2")
```