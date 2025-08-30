from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_content


# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))
# print(get_files_info("calculator", "calculator"))

# print(get_file_content("calculator", "lorem.txt"))

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat")) #(this should return an error string)
print(get_file_content("calculator", "pkg/does_not_exist.py"))