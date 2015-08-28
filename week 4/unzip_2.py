import zipfile
zFile=zipfile.ZipFile("files.zip")
try:
	zFile.extractall(pwd="oranges")
except Exception, e:
	print e
