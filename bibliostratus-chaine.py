import os

bbs_path = "../bibliostratus"

# Etape 1 : marc2tables

#bibliostratus-cli.py [-h] --action {bib2id,aut2id,marc2tables,ark2records} --file FILE [--dir DIR] [--prefix PREFIX]
#                            [--filetype {iso2709-utf8,iso2709-8859-1,xml,xml-utf8}] [--recordtype {bib,aut,bib2aut}]
#bibliostratus-cli.py: error: the following arguments are required: --file

file_in = "data/koha.mrc" #"data/2022-10-16-notices_total.mrc"
command = f"python {bbs_path}/bibliostratus/bibliostratus-cli.py --action marc2tables --file {file_in} --dir data --prefix test --filetype iso2709-utf8 --recordtype bib"
os.system(command)
