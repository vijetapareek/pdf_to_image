
from config import pdf_to_image_config

import logging
import os

# ---- Configuration file parameters ----
gs_path = pdf_to_image_config.val_gs_path
log_file_path = pdf_to_image_config.val_log_file_path

# ---- Logging set up ------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# ---------- User inputs ----

'''pdf_input_path = r"D:\workspace\ghostscript\data\resume.pdf"
output_directory_path = r"D:\workspace\ghostscript\data"
format = 'jpg'
dpi = 300'''


# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")

def pdftoimg(ghost_path=None,
             dpi=100,
             pdf_input_path=None,
             output_directory_path=None,
             image_format='jpg'):
    _, file_name = os.path.split(pdf_input_path)
    file_name_wo_ext = file_name.split('.')[0]
    text_output_path = os.path.join(output_directory_path, file_name_wo_ext)

    my_string = f'"{ghost_path}" -dNOPAUSE -dBATCH -sDEVICE={image_format} -r{dpi}' \
               f' -sOutputFile="{text_output_path}"_%0d."{image_format}" "{pdf_input_path}"'
    logger.info(my_string)

    logger.info(f"Executing the command")
    os.system(f'"{my_string}"')
    logger.info(f"Command completed")

def switch():
    logger.info("Select the respective option for your required format: ")
    logger.info("Enter the required format: \n png or \n png_gray or \n jpg ")
    option = input("Enter the format: ")

    dict1 = {
        'png': 'png16m',
        'png_gray': 'pnggray',
        'jpg': 'jpeg'
    }
    return dict1.get(option)


if __name__ == '__main__':
    ghostscript_path = r"C:\gs\gs9.52\bin\gswin64c.exe"
    input_path = input("Enter the pdf input path: ")  # "D:\workspace\ghostscript\data\resume.pdf"
    output_path = input("Enter the pdf output path: ")  # "D:\workspace\ghostscript\data"
    image_format = switch()
    logger.info(f"User inputs :: input_path: {input_path}, output_path: {output_path}, image_format: {image_format}")
    dpi = int(input("Enter the required dpi"))
    pdftoimg(ghost_path=ghostscript_path,
            dpi=dpi,
            pdf_input_path=input_path,
            output_directory_path=output_path,
            image_format=image_format)


# ghost_path = r"C:\gs\gs9.52\bin\gswin64c.exe"
# pdf_input_path = r"D:\workspace\ghostscript\data\resume.pdf"
# output_directory_path = r"D:\workspace\tesseract\data"
# dpi = int(input("Enter the required dpi"))
#


