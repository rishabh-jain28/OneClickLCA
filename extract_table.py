import tabula
import pandas as pd

# set the file path of the PDF to be extracted
file_path_list = ["pdf_files/BREGENEPD000078.pdf","pdf_files/BREGENEPD000079.pdf"]

from tabula import read_pdf
from tabulate import tabulate

#reads table from pdf file
for i in range(len(file_path_list)):
    df_ = read_pdf(file_path_list[i],pages=4) #address of pdf file
    df_[0].to_excel('output{}.xlsx'.format(i))

