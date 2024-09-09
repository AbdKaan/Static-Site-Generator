import os
import shutil
from helper_functions import markdown_to_html_node


def copy_contents_to_folder(src: str, dst: str):
    # Delete contents in the destination folder
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    # Copy all the files recursively
    for dir in os.listdir(src):
        if os.path.isfile(f"{src}/{dir}"):
            shutil.copy(f"{src}/{dir}", dst)
        else:
            copy_contents_to_folder(f"{src}/{dir}", f"{dst}/{dir}")

def extract_title(markdown):
    if markdown[0:2] == "# ":
        return markdown.split("\n", 1)[0][2:]
    else:
        raise Exception("There is no h1 header.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    template = ""
    with open(from_path) as file1, open(template_path) as file2:
        markdown = file1.read()
        template = file2.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    
    with open(f"{dest_path}/index.html", 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for dir in os.listdir(dir_path_content):
        if dir[-3:] == ".md":
            generate_page(os.path.join(dir_path_content, dir), template_path, dest_dir_path)
        elif os.path.isdir(os.path.join(dir_path_content, dir)):
            generate_pages_recursive(os.path.join(dir_path_content, dir), template_path, os.path.join(dest_dir_path, dir))