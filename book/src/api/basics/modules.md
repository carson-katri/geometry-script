# Modules

The first step when writing is script is importing the `geometry_script` module. There a are a few ways of doing this:

## Import All Names (Recommended)
This will import every type and function available into your script. It can make it easy to discover what's available with code completion, and makes the scripts more terse.
```python
from geometry_script import *

cube(...) # Available globally
my_geo: Geometry # All types available as well
```

## Import Specific Names
This will import only the specified names from the module:
```python
from geometry_script import cube, Geometry

cube(...) # Available from import
my_geo: Geometry
```

## Namespaced Import
This will import every type and function, and place them behind the namespace. You can use the module name, or provide your own.
```python
import geometry_script

geometry_script.cube(...) # Prefix with the namespace
my_geo: geometry_script.Geometry
```
```python
import geometry_script as gs

gs.cube(...) # Prefix with the custom name
my_geo: gs.Geometry
```

Now that you have Geometry Script imported in some way, let's create a tree.