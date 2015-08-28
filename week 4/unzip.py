import zipfile
zFile=zipfile.ZipFile("files.zip")
zFile.extractall(pwd="secret")
