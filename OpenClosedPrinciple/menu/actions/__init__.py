import os
import pkgutil
import importlib
from .action import BaseAction

# Get the directory name of the current package
pkg_dir = os.path.dirname(__file__)

# Import each module
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    importlib.import_module('.' + name, __package__)

# Since each menu action class is a subclass of BaseAction, I can
# build a dictionary of all classes, in all modules, in this package
all_actions = {cls.__name__: cls for cls in BaseAction.__subclasses__()}

# Now anywhere I want to use all classes, I can use the following code
#
# import menu.actions
#
# for k,v in menu.actions.all_actions.items():
#   ...do something awesome with each one
