
# import mymodule
import mymodule as mm
mm.func_in_module() # I AM INSIDE THE MYMODULE.PY FILE!

# from mymodule import func_in_module
# func_in_module()

## frowned upon b/c wastes memory by importing everything
# from mymodule import *
# func_in_module