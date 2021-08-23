# pip install python_barcode
import barcode 
from barcode.writer import ImageWriter

# text on the barcode
text = "Python Code"

# text to complete string
text1 = str(text)

#creating code for barcode
code = barcode.get_barcode_class("code128")

#creating image of the barcode
image = code(text,writer=ImageWriter())

#saving the barcode image
save_img = image.save('my final barcode')
