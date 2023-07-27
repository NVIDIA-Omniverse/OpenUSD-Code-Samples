import argparse
import logging
import os
import shutil
import subprocess
from pathlib import Path

import toml
from rstcloth import RstCloth

REPO_ROOT = Path(__file__).parent
SOURCE_DIR = REPO_ROOT / "source"
SPHINX_DIR = REPO_ROOT / "sphinx"
SPHINX_CODE_SAMPLES_DIR = SPHINX_DIR / "usd"

# 0 = normal toctree
# 1 = :doc: tags
TOCTREE_STYLE = 1

logger = logging.getLogger(__name__)

def main():    

    # flush build dir 
    if os.path.exists(SPHINX_CODE_SAMPLES_DIR):
        shutil.rmtree(SPHINX_CODE_SAMPLES_DIR)    
    
    SPHINX_CODE_SAMPLES_DIR.mkdir(exist_ok=False)        

    samples = {}
    # each config.toml should be a sample
    for config_file in SOURCE_DIR.rglob("config.toml"):
        category_name = config_file.parent.parent.name
        sample_name = config_file.parent.name
        if category_name not in samples:
            samples[category_name] = []
            
        #print(f"config_file  == {config_file["core"]["title"]}")
        # print(f"config_file  == {config_file["core"]["title"]}")
        # samples[category_name].append(sample_name)#, config_file["core"]["title"]])

        logger.info(f"processing: {sample_name}")
        sample_source_dir = config_file.parent
        #logger.info(f"sample_source_dir:: {sample_source_dir}")
        
        sample_output_dir = SPHINX_CODE_SAMPLES_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)  / f"{sample_name}"
        #logger.info(f"sample_output_dir:: {sample_output_dir}")
        
        # make sure category dir exists
        category_output_dir = SPHINX_CODE_SAMPLES_DIR / sample_source_dir.parent.relative_to(SOURCE_DIR)
        #logger.info(f"category_output_dir:: {category_output_dir}")
               
        if not os.path.exists(category_output_dir):
            category_output_dir.mkdir(exist_ok=False)   
            
        sample_rst_out = category_output_dir / f"{sample_name}.rst"
        #logger.info(f"sample_rst_out: {sample_rst_out}")
        with open(config_file) as f:
            content = f.read()
            config = toml.loads(content)

        title = config["core"]["title"]
        samples[category_name].append([sample_name, title])

        sample_output_dir.mkdir(exist_ok=True)
        with open(sample_rst_out, "w") as f:
            doc = RstCloth(f)
            
            if TOCTREE_STYLE == 1:
                doc._add(":orphan:")
                doc.newline()
                                
            doc.directive("meta", 
                fields=[
                    ('description', config["metadata"]["description"]), 
                    ('keywords', ", ".join(config["metadata"]["keywords"]))
            ])
            doc.newline()
            doc.title(config["core"]["title"], overline=False)
            doc.newline()
            
            
            md_file_path = sample_source_dir / "header.md"
            new_md_name = sample_name + "_header.md"

            out_md = category_output_dir / new_md_name
            prepend_include_path(md_file_path, out_md, sample_name)
            fields = [("parser" , "myst_parser.sphinx_")]
            doc.directive( "include", new_md_name, fields)
            doc.newline()  
            doc.newline()            

            doc.directive("tab-set")
            doc.newline()           
            
            code_flavors = {"USD Python" : "py_usd.md",
                            "Python omni.usd" : "py_omni_usd.md",
                            "Python Kit Commands" : "py_kit_cmds.md",  
                            "USD C++" : "cpp_usd.md",  
                            "C++ omni.usd" : "cpp_omni_usd.md",
                            "C++ Kit Commands" : "cpp_kit_cmds.md",  
                            "USDA" : "usda.md",  
            }
            
            for tab_name in code_flavors:
                md_file_name = code_flavors[tab_name]
                md_file_path = sample_source_dir / code_flavors[tab_name]
                
                if md_file_path.exists():
                    doc.directive("tab-item", tab_name, None, None, 3)
                    doc.newline()
                    
                    # make sure all md flavor names are unique
                    new_md_name = sample_name + "_" + md_file_name
                    category_output_dir

                    out_md = category_output_dir / new_md_name
                    prepend_include_path(md_file_path, out_md, sample_name)
                       
                    fields = [("parser" , "myst_parser.sphinx_")]
                    doc.directive( "include", new_md_name, fields, None, 6)
                    doc.newline()        

                # copy all samples 
                shutil.copytree(sample_source_dir, sample_output_dir, ignore=shutil.ignore_patterns('*.md', 'config.toml'), dirs_exist_ok=True )
                    
            doc.newline()
    
    generate_sphinx_index(samples)

    sphinx_build_cmd = ["python", "-m" "sphinx.cmd.build", str(SPHINX_DIR), str(SPHINX_DIR / "_build"), "-b", "html"]
    subprocess.run(sphinx_build_cmd)


def prepend_include_path(in_file_path: str, out_file_path: str, dir_path: str):
    with open(in_file_path) as mdf:
        md_data = mdf.read()
          
    mdf.close()    
              
    md_lines = md_data.split("\n")
    lc = 0
    for line in md_lines:   
        inc_str ="``` {literalinclude}"
        sp = line.split(inc_str)
        if len(sp) > 1:
            filename = sp[1].strip()
            newl = inc_str + " " + dir_path + "/" + filename
            md_lines[lc] = newl
        lc += 1
        
    with open(out_file_path,"w") as nmdf:
        #mdf.writelines(md_lines)
        for line in md_lines:
            nmdf.writelines(line + "\n")
        nmdf.close()
    
    
def generate_sphinx_index(samples):
    cat_names_path = SOURCE_DIR / "category-display-names.toml"
    cat_names = toml.load(cat_names_path)["name_mappings"]
    print(f"CAT_NAMES: {cat_names}")
    
    ref_links = {}#"variant-sets" : "variant_sets_ref_test"}


    
    index_rst = SPHINX_DIR / "usd.rst"
    with open(index_rst, "w") as f:
        doc = RstCloth(f)
        doc.directive("include", "usd_header.rst")
        doc.newline()
        #doc.title("OpenUSD Code Samples")
        for category, cat_samples in samples.items():
            
            if category in ref_links:
                doc.ref_target(ref_links[category])
                doc.newline()
            
            human_readable = readable_from_category_dir_name(category)
            if category in cat_names.keys():
                human_readable = cat_names[category]
            else:
                human_readable = readable_from_category_dir_name(category)
            
            #doc.h2(human_readable)
            
            fields = [
                ("caption", human_readable),
                ("maxdepth", "2")
            ]
            
            doc.newline()
            
            if TOCTREE_STYLE == 0:
                sample_paths = [f"usd/{category}/{sample[0]}" for sample in cat_samples]
                doc.directive("toctree", None, fields, sample_paths)
                doc.newline()
            elif TOCTREE_STYLE == 1: 
                doc.h2(human_readable)
                doc.newline()
                for sample, title in cat_samples:
                    doc._add("- :doc:`" + title + f" <usd/{category}/" + sample + ">`")
                doc.newline()                              
    
        doc.directive("include", "usd_footer.rst")
        doc.newline()       
    f.close()



def readable_from_category_dir_name(category):
    sub_strs = category.split("-")
    readable = ""
    for sub in sub_strs:
        readable += sub.capitalize() + " "
        
    return readable.strip()
        
        

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