import os
from blocktype import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    template = template.replace('action="/', f'action="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(entry_path) and entry.endswith('.md'):
            rel_path = os.path.relpath(entry_path, dir_path_content)
            dest_file_path = os.path.join(dest_dir_path, rel_path.replace('.md', '.html'))
            generate_page(entry_path, template_path, dest_file_path, basepath)
        elif os.path.isdir(entry_path):
            rel_dir = os.path.relpath(entry_path, dir_path_content)
            new_dest_dir = os.path.join(dest_dir_path, rel_dir)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, new_dest_dir, basepath)
