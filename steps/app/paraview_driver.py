import os, shutil
import io
import subprocess
import app.messages as msg

def get_base_path(full_path):
    """
    This function takes a full file path and returns the base path (directory) containing the file.

    Parameters:
    full_path (str): The full file path.

    Returns:
    str: The base path (directory) containing the file.
    """
    base_path = os.path.dirname(full_path)
    return base_path

def get_basename(full_path):
    """
    This function takes a full file path and returns the basename (filename with extension).

    Parameters:
    full_path (str): The full file path.

    Returns:
    str: The basename (filename with extension).
    """
    basename = os.path.basename(full_path)
    filename, ext = os.path.splitext(basename)
    return filename, ext

def setup_temp_directory(script_file, data_path, files, temp_dir='./temp'):
    # Create a temporary directory to copy mesh files and scripts to run
    # If the directory does not exist, create it
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Define the directory where Paraview scripts are stored
    paraview_script_dir = "paraview_scripts"

    # Create the full path to the script
    script_path = os.path.join(paraview_script_dir, script_file)

    shutil.copy2(script_path, temp_dir)

    for f in files:
        src = os.path.join(data_path,f)
        dst = os.path.join(temp_dir,f)
        shutil.copy2(src, dst)

    return temp_dir

def delete_temp_directory(temp_dir='./temp'):

    return

def save_script_data(script_file, temp_dir, output_path):

    script_name, _ext = get_basename(script_file)
    # save data
    script_saves = 'convert_to_stl', 'generate_curvature'
    if script_name =='convert_to_stl':
        # Copy the output mesh back to the mesh directory
        temp_mesh = os.path.join(temp_dir,'out.stl')
        temp_png = os.path.join(temp_dir, 'screenshot.png')
        out_png = os.path.join(output_path, script_name+'.png')
        out_mesh = os.path.join(output_path, script_name+'.stl')

        shutil.copy2(temp_png, out_png)
        shutil.copy2(temp_mesh, out_mesh)

    elif script_name =='generate_curvature' or script_name == 'create_outlets':
        # Copy the output mesh back to the mesh directory
        temp_state = os.path.join(temp_dir,'paraview_state.pvsm')
        temp_png = os.path.join(temp_dir, 'screenshot.png')
        out_png = os.path.join(output_path, script_name+'.png')
        out_state = os.path.join(output_path, script_name+'.pvsm')
        shutil.copy2(temp_png, out_png)
        shutil.copy2(temp_state, out_state)

    return


def run_script(paraview_python_batch, script_file, data_path, files, output_path, debug=False):
    # Notify the user that the script is about to run
    msg.notification('running paraview script: {}'.format(script_file))

    # Save the current working directory
    cwd = os.getcwd()

    # Set up a temporary directory and copy the required files into it
    temp_dir = setup_temp_directory(script_file, data_path, files)

    # Change the working directory to the temporary directory
    os.chdir(temp_dir)

    # Define filenames for capturing standard output and error
    outfile = "out.txt"
    errfile = "err.txt"

    # Open the output and error files in write mode
    with open(outfile, 'w+') as fout:
        with open(errfile, 'w+') as ferr:
            # Start the Paraview script as a subprocess
            proc = subprocess.Popen([paraview_python_batch, script_file], 
                                    stdout=fout, stderr=ferr)

    # Wait for the subprocess to complete
    proc.wait()

    # Change back to the original working directory
    os.chdir(cwd)
    
    save_script_data(script_file, temp_dir, output_path)

    # Remove the temporary directory and its contents
    if debug==False:
        shutil.rmtree(temp_dir)

    # Return the subprocess object
    return proc