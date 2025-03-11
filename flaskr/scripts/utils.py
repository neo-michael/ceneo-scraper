import markdown

def mark2html(file_name):
    with open(file_name, 'r', encoding="utf-8") as md_fp:
        md_contents = md_fp.read()
    
    return markdown.markdown(md_contents)