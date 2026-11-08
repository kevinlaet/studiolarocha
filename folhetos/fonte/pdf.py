# Monta folhetos-a5.pdf (A5, 5 páginas) a partir dos PNGs. Uso: python3 pdf.py
from PIL import Image
n=['auriculoterapia','limpeza-de-pele','manicure-e-pedicure','massagem','produtos']
ims=[Image.open(f'../folheto-{x}.png').convert('RGB') for x in n]
ims[0].save('../folhetos-a5.pdf',save_all=True,append_images=ims[1:],resolution=600,quality=95)
