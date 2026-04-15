
### Draw a circle in FreeCAD python console

import FreeCAD, Part, Sketcher, FreeCADGui

# 1. Create a new document
doc = FreeCAD.newDocument("CircleTest")

# 2. Add a Sketcher object to the document
sketch = doc.addObject("Sketcher::SketchObject", "MyCircleSketch")

# 3. Add a circle geometry 
# Syntax: Part.Circle(Center, Normal_Axis, Radius)
center = FreeCAD.Vector(0, 0, 0)
axis = FreeCAD.Vector(0, 0, 1) # Points straight up (Z-axis)
radius = 25.0
sketch.addGeometry(Part.Circle(center, axis, radius), False)

# 4. Recompute the document to generate the shape
doc.recompute()

# 5. Bring the view to the object so you can see it
FreeCADGui.activeView().viewFront()
FreeCADGui.SendMsgToActiveView("ViewSelection")
