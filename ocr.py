import cv2
import pytesseract

# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# baixar o arquivo por,**** e colar na pasta do tesseract

# pegar linguas: print(pytesseract.get_languages())

# windows instalar tesseract https://github.com/UB-Mannheim/tesseract/wiki


imagem = cv2.imread("2021-05-07 12_21_25-agente qualificado b3 - Pesquisa Google.jpg")

caminho = r"C:\Program Files\Tesseract-OCR"


pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang="por")
print(texto)

