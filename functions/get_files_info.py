import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(full_path)
    directory_list = os.listdir(full_path)
    

    if "AIAgent/" not in absolute_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if os.path.isdir(directory) != True:
        return f'Error: "{directory}" is not a directory'
    
    dir_list_prep = [] # initialize an empty list to create the required format
    for item in directory_list:
        item_path = os.path.join(full_path, item)  # full path for checks
        
        file_size = os.path.getsize(item_path) #if os.path.isfile(item_path) else 0
        is_dir = os.path.isdir(item_path)
        
        dir_list_prep.append(f"- {item}: {file_size} bytes, is_dir={is_dir}") # store the req format in a list to join later as a single string 
    
    # print(absolute_path) # debug prints
    # print("\n".join(directory_list)) # debug prints
    print("\n".join(dir_list_prep))
    # return "\n".join(dir_list_prep)
    # return "\n".join(dir_list_prep)
