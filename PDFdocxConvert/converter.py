import os
from pdf2docx import Converter
from docx2pdf import convert
from config import PDF_FOLDER, WORD_FOLDER


class WordDocx:
    def __init__(self):
        self.pdf_folder: str = PDF_FOLDER
        self.word_folder: str = WORD_FOLDER
        self.to_word: bool = True
    
    def convert(self) -> None:
        if self.to_word:
            self.convert_to_word()
        else:
            self.convert_to_pdf()
    
    def convert_to_word(self) -> None:
        for file in os.listdir(self.pdf_folder):
            if not file.endswith('.pdf'):
                continue
            pdf: str = f'{self.pdf_folder}/{file}'
            word: str = file.replace('.pdf', '.docx')
            doc: str = f'{self.word_folder}/{word}'
            WordDocx.pdf_to_docx(pdf, doc)
    
    def convert_to_pdf(self) -> None:
        for file in os.listdir(self.word_folder):
            if not file.endswith('.docx'):
                continue
            docx: str = f'{self.word_folder}/{file}'
            pd: str = file.replace('.docx', '.pdf')
            pdf: str = f'{self.pdf_folder}/{pd}'
            convert(docx, pdf)
    
    @staticmethod    
    def pdf_to_docx(pdf_file: str, docx_file: str) -> None:
        cn: Converter = Converter(pdf_file)
        cn.convert(docx_file, start=0, end=None)
        cn.close()
    