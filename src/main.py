import sys

from main_helper_functions import copy_contents_to_folder, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_contents_to_folder(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
