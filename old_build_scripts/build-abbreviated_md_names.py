import argparse
import logging
from pathlib import Path
import toml
import os
import shutil

from rstcloth import RstCloth
from md_to_rst import convertMarkdownToRst


REPO_ROOT = Path(__file__).parent
SOURCE_DIR = REPO_ROOT / "source2"
BUILD_DIR = REPO_ROOT / "_build" / "usd"

logger = logging.getLogger(__name__)

def main():    

    # flush build dir 
    sub_usd_build_dir = REPO_ROOT / "_build"
    if os.path.exists(sub_usd_build_dir):
        shutil.rmtree(sub_usd_build_dir)    
    
    sub_usd_build_dir.mkdir(exist_ok=False)    
    BUILD_DIR.mkdir(exist_ok=False)    

    # each config.toml should be a sample
    for config_file in SOURCE_DIR.rglob("config.toml"):
        logger.info(f"processing: {config_file.parent.name}")
        sample_source_dir = config_file.parent
        logger.info(f"sample_source_dir:: {sample_source_dir}")
        
        sample_output_dir = BUILD_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)  / f"{config_file.parent.name}"
        
        
        logger.info(f"sample_output_dir:: {sample_output_dir}")
        # make sure category dir exists
       
        category_output_dir = BUILD_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)
        logger.info(f"category_output_dir:: {category_output_dir}")

        
        if not os.path.exists(category_output_dir):
            category_output_dir.mkdir(exist_ok=False)   
            
        #logger.info(f"config_file.parent: {config_file.parent}")
                 
        sample_rst_out = category_output_dir / f"{config_file.parent.name}.rst"
        logger.info(f"sample_rst_out: {sample_rst_out}")
        with open(config_file) as f:
            content = f.read()
            config = toml.loads(content)
            
        abbreviated_suffix = ""
        name_starts = config_file.parent.name.split("-")
        for name_part in name_starts:
            abbreviated_suffix += name_part[0]

        logger.info(f"abbreviated_suffix: {abbreviated_suffix}")   

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
                            "omni.usd Python" : "py_omni_usd.md",
                            "Kit Commands" : "py_kit_cmds.md",  
                            "USD C++" : "cpp_usd.md",  
                            "USDA" : "usda.md",  
            }
            
            
            
            for tab_name in code_flavors:
                md_file_name = code_flavors[tab_name]
                md_file_path = sample_source_dir / code_flavors[tab_name]
                
                if md_file_path.exists():
                    doc.directive("tab-item", tab_name, None, None, 3)
                    doc.newline()
                    
                    # make sure that the abbreviation is unique, else number it
                    done = False
                    attempt_count = 0
                    new_md_name = ""
                    while not done:
                        new_abbreviated_suffix = abbreviated_suffix
                        if attempt_count > 0:
                            new_abbreviated_suffix = abbreviated_suffix + str(attempt_count)
                            logger.info(f"trying new markdown suffix:: {new_abbreviated_suffix}")
                            
                        attempt_count += 1
                        new_md_name = md_file_name.split(".")[0] + "_" + new_abbreviated_suffix + ".md"

                        new_md_path = category_output_dir / new_md_name
                        done = not os.path.exists(new_md_path) 

                    # copy md file to build dir, then rename to abbreviated name
                    shutil.copy(md_file_path, category_output_dir)
                    dst_file = os.path.join(category_output_dir, md_file_name)
                    new_dst_file_name = os.path.join(category_output_dir, new_md_name)
                    os.rename(dst_file, new_dst_file_name)#rename                    
                    #shutil.copy( md_file_path, category_output_dir)
                    
                    
                       
                    fields = [("parser" , "myst_parser.sphinx_")]
                    doc.directive( "include", new_md_name, fields, None, 6)
                    doc.newline()        
                    
                # copy all samples 
                shutil.copytree(sample_source_dir, sample_output_dir, ignore=shutil.ignore_patterns('*.md', 'config.toml'), dirs_exist_ok=True )
                    
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