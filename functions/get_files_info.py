import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))
        
    if os.path.commonpath([abs_working_directory, full_path]) != abs_working_directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
        
    # build the list
    dir_list_prep = [] # initialize an empty list to create the required format
    directory_list = os.listdir(full_path)
    
    for item in directory_list:
        item_path = os.path.join(full_path, item)  # full path for checks
        
        file_size = os.path.getsize(item_path) #if os.path.isfile(item_path) else 0
        is_dir = os.path.isdir(item_path)
        
        dir_list_prep.append(f"- {item}: {file_size} bytes, is_dir={is_dir}") # store the req format in a list to join later as a single string 
    
    # print(absolute_path) # debug prints
    # print("\n".join(directory_list)) # debug prints
    print("\n".join(dir_list_prep))
    # return ("\n".join(dir_list_prep))

