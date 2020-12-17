from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(_file):
    """Returns text by converting the file to text format
    
    Keyword Arguments:
        _file {file} -- the reference file (default: {None})

    Returns:
        [str] -- text converted from the given file 
    """
    pagenums = set()
    
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    for page in PDFPage.get_pages(_file, pagenums):
        interpreter.process_page(page)
    converter.close()
    text = output.getvalue()
    output.close
    return text