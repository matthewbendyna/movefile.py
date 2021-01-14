This Python module, movefile.py, presently has four functions, three being methods
to be called from an outside program.

In your Python IDE:

import os
import movefile

Three original functions created by Matthew Bendyna:

movefile.move(path, file, returntobasedir)
	This method takes a specified path and a file in the cwd(current working directory)
	and deletes it from the cwd, copying it to the new directory.
	Under the condition that the file does not exist, returnFile is
	called from this method

returnFile(r, file, ordir)
	This function is called by movefile.move() and is responsibale for
	returning the file data that was deleted from the orginal directory
	in movefile.move() and returning it to the original directory, ordir.
	r is the string containing the file data, file is the file name to
	be restored to the original directory, and ordir is the string path
	of the owd.