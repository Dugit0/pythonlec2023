# Все приемы и функции для решения были честно найдены на StackOverflow
# https://stackoverflow.com/questions/34162017/unzip-buffer-with-python
# https://stackoverflow.com/questions/39952867/how-to-know-the-folder-size-in-a-zipfile
# https://stackoverflow.com/questions/31124670/how-to-programmatically-count-the-number-of-files-in-an-archive-using-python

import zipfile
import sys
import io
my_zip = zipfile.ZipFile(io.BytesIO(bytes.fromhex(sys.stdin.read())))
print(sum(1 for i in my_zip.infolist() if not i.is_dir()), sum(i.file_size for i in my_zip.filelist))
