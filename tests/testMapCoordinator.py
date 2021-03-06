from os import path, access, R_OK
import importlib

def getMap(level):
	# Local directory filename and import name
	mapFilename = "Map" + str(level)
	mapImportName = "maps." + mapFilename
	# Local directory filename with extension
	mapFullFilename =  "../src/org/maps/" + mapFilename + ".py"

	if (path.exists(mapFullFilename) and path.isfile(mapFullFilename) and access(mapFullFilename, R_OK)):
		# File exists and is readable, import it
		return importlib.import_module(mapImportName)
	else:
		# Either file is missing or is not readable, return None
		return None