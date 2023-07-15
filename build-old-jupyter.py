import argparse
import ast
import logging
from pathlib import Path
import tomllib

from rstcloth import RstCloth
from md_to_rst import convertMarkdownToRst


REPO_ROOT = Path(__file__).parent
SOURCE_DIR = REPO_ROOT / "source"
BUILD_DIR = REPO_ROOT / "_build"

logger = logging.getLogger(__name__)

def main():
    BUILD_DIR.mkdir(exist_ok=True)
    for config_file in SOURCE_DIR.rglob("config.toml"):
        logger.info(f"Converting {config_file.parent.name}")
        sample_source_dir = config_file.parent
        sample_output_dir = BUILD_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)
        sample_rst_out = sample_output_dir / f"{config_file.parent.name}.rst"
        with open(config_file) as f:
            content = f.read()
            config = tomllib.loads(content)
        sample_output_dir.mkdir(exist_ok=True)
        with open(sample_rst_out, "w") as f:
            doc = RstCloth(f)
            doc.directive("metadata", 
                fields=[
                    ('description', config["metadata"]["description"]), 
                    ('keywords', ", ".join(config["metadata"]["keywords"]))
            ])
            doc.newline()
            with open(sample_source_dir / "header.md") as header_file:
                header_content = convertMarkdownToRst(header_file.read())
                doc._stream.write(header_content)
                doc.newline()
                doc.newline()
            
            parse_usd_py(doc, sample_source_dir)
            parse_kit_commands(doc, sample_source_dir)

def parse_python(python_file_path):
    with open(python_file_path) as f:
        content = f.read()
    content_lines = content.split("\n")
    tree = ast.parse(content)
    sample_info = {}
    sample_info["module_docstring"] = ast.get_docstring(tree)

    blocks = []
    current_block = None
    current_block_code_start = None
    current_block_code_end = None
    for obj in tree.body[1:]:
        if isinstance(obj, ast.Expr):
            current_block = {"intro": obj.value.value.strip(), "code": []}
            current_block_code_start = None
            current_block_code_end = None
        if isinstance(obj, (ast.Import, ast.ImportFrom)) and current_block_code_start is None:
            current_block_code_start = obj.lineno-1
        if isinstance(obj, ast.FunctionDef) and current_block_code_end is None:
            last_body = obj.body[-1]
            while isinstance (last_body,(ast.For,ast.While,ast.If)):
                last_body = last_body.body[-1]
            current_block_code_end = last_body.end_lineno
            current_block["code"] = "\n".join(content_lines[current_block_code_start:current_block_code_end])
            blocks.append(current_block)

    sample_info["blocks"] = blocks

    return sample_info


def parse_usd_py(doc: RstCloth, sample_source_dir):
    usd_py_file = sample_source_dir / "python" / "usd.py"
    if not usd_py_file.exists():
        logger.warning("USD Python code sample does not exist. Skipping...")
        return
    logger.info("Parsing usd.py")
    content = parse_python(usd_py_file)
    doc.h2("USD Python API")
    doc.content(content["module_docstring"])
    doc.newline()
    for block in content["blocks"]:
        doc.content(block["intro"])
        doc.newline()
        doc.codeblock(block["code"], language="python")
    doc.newline()

def parse_kit_commands(doc: RstCloth, sample_source_dir):
    kit_cmd_py_file = sample_source_dir / "python" / "kit_commands.py"
    if not kit_cmd_py_file.exists():
        logger.warning("Kit Commands code sample does not exist. Skipping...")
        return
    logger.info("Parsing kit_commands.py")
    content = parse_python(kit_cmd_py_file)
    doc.h2("Omniverse Kit Commands")
    doc.content(content["module_docstring"])
    doc.newline()
    for block in content["blocks"]:
        doc.content(block["intro"])
        doc.newline()
        doc.codeblock(block["code"], language="python")    
    doc.newline()        



if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Build rST documentation from code sample source.')

    # Add arguments
    parser.add_argument('--name', help='Specify the name')

    # Parse the arguments
    args = parser.parse_args()

    # Access the values provided for the arguments
    name = args.name
    logging.basicConfig(level=logging.INFO)
    main()