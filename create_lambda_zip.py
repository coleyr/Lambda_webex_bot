import subprocess, os, sys, glob
import shutil


def remove_zip(zipname):
    if os.path.exists(zipname): 
        os.remove(zipname)
    if os.path.exists(f"{zipname}.zip"):
        os.remove(f"{zipname}.zip")
        
def copy_python_files(directory, package_location_path):
    for file in os.listdir(directory):
        filepath = os.path.abspath(os.path.join(directory, file))
        if filepath[-3:] == ".py" and filepath != __file__:
            shutil.copy(filepath, package_location_path) 
            
def make_zip(package_location='./packages', zip_name="lambda_function"):
    #Get Directory path of current python file
    directory = os.path.dirname(__file__)
    #Remove file.zip if already exists
    remove_zip(zipname=zip_name)
    #Get absolute path of target directory
    package_location_path =  os.path.abspath(os.path.join(directory, package_location))
    #Remove all items in the package location directory
    shutil.rmtree(package_location_path, ignore_errors=True)
    #Make directory to store dependencies and python files
    os.makedirs(package_location, exist_ok=True)
    #Update Pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", '--upgrade', 'pip'])
    #install dependencies into above folder
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r', 'requirements.txt', '--target', package_location])
    #Copy python files if they end in ".py" and is not this file
    copy_python_files(directory, package_location_path)
    #Create zip file from package folder
    shutil.make_archive(zip_name, 'zip', package_location)

make_zip()