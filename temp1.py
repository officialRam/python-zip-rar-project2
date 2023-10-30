import zipfile
import patoolib
import pathlib
import os
import os.path

def count_files(directory):
  """Counts the number of files in a directory."""
  count = 0
  for file in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, file)):
      count += 1
  return count


def extract_file_path(directory, i):
  """Extracts the file path from a directory.

  Args:
    directory: The directory to extract the file path from.

  Returns:
    The file path.
  """

  if not os.path.isdir(directory):
    raise ValueError("Directory does not exist.")
  files = os.listdir(directory)
  if not files:
    return None
  file = files[i]
  return os.path.join(directory, file)


  
val=input("Enter 'compress' or 'decompress': ")
if val=="compress":
    val2=input("Enter the folder to compress: ")
    val3=input("Enter the output filename (with extension .zip, .rar, .tar, .tar.gz, .tar.bz2): ")
    if ".zip"==val3[-4:]:
        folder=pathlib.Path(val2)
        with zipfile.ZipFile(val3, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for file in folder.iterdir():
                z.write(file)


    elif ".rar"==val3[-4:]:
        files=[]        
        directory = val2
        
        for i in range(count_files(directory)):
           file_path = extract_file_path(directory, i)          
           files.append(file_path)       
        
        patoolib.create_archive(val3, files);
        

if val=="decompress":
    val2=input("Enter the folder to decompress: ")
    val3=input("Enter the output filename to save decompressed file: ")
    if(val2[-4:]==".zip"):
       with zipfile.ZipFile(val2, 'r') as z:
          z.extractall(val3)
    else:
       files=[]        
       directory = val2            
       patoolib.extract_archive(directory, outdir=val3);
       
       
    

    



