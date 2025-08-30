import os
from config import *


def get_file_content(working_directory, file_path):
    # resolve to absolute paths
    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(abs_working_directory, file_path)) # generate the target file absolute path

    try:
        # check if file is in working directory 
        if os.path.commonpath([abs_working_directory, target_path]) != abs_working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
    
    try:
        # check if file is actually a file
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"Error: {e}"
    
    try:
        # return the file contents truncated or not, or an error if exceptions happens
        file = open(target_path)
        file_data = file.read()    
        if len(file_data) > MAX_CHARS:
            return file_data[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
        return file_data
    except Exception as e:
        return f"Error: {e}"