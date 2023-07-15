import argparse
import ast
import logging
from pathlib import Path
import toml
import os
import shutil

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
        sample_output_dir = BUILD_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)  / f"{config_file.parent.name}"
        sample_rst_out = sample_output_dir / f"{config_file.parent.name}.rst"
        with open(config_file) as f:
            content = f.read()
            config = toml.loads(content)
            
        if os.path.exists(sample_output_dir):
            #logger.info(f"Deleting: {sample_output_dir}")
            shutil.rmtree(sample_output_dir)

        sample_output_dir.mkdir(exist_ok=True)
        with open(sample_rst_out, "w") as f:
            doc = RstCloth(f)
            doc.directive("meta", 
                fields=[
                    ('description', config["metadata"]["description"]), 
                    ('keywords', ", ".join(config["metadata"]["keywords"]))
            ])
            doc.newline()
            doc.newline()
            
            with open(sample_source_dir / "header.md") as header_file:
                header_content = convertMarkdownToRst(header_file.read())
                doc._stream.write(header_content)
                doc.newline()
                doc.newline()
            

            doc.directive("tab-set")
            doc.newline()           
            
            code_flavors = {"USD Python" : "py_usd.md",
                            "Omni Python" : "py_omni.md",
                            "Kit Commands" : "py_kit_commands.md",  
                            "USD C++" : "cpp_usd.md",  
                            "USDA" : "usda.md",  
            }
            
            for tab_name in code_flavors:
                md_file_name = code_flavors[tab_name]
                md_file_path = sample_source_dir / code_flavors[tab_name]
                
                if md_file_path.exists():
                    doc.directive("tab-item", tab_name, None, None, 3)
                    doc.newline()
                    fields = [("parser" , "myst_parser.sphinx_")]
                    doc.directive( "include", md_file_name, fields, None, 6)
                    doc.newline()           
                    
            doc.newline()                       
                    
            shutil.copytree(sample_source_dir, sample_output_dir, ignore=shutil.ignore_patterns('header.md', 'config.toml'), dirs_exist_ok=True )


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