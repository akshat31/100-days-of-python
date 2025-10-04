import barcode
from barcode.writer import ImageWriter

text = "This is my python programming code"
code = barcode.get_barcode_class("code128")
image = code(text, writer=ImageWriter())
save_img = image.save("barcode_image")