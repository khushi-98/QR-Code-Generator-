import qrcode  

from PIL import Image


qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10, border=4)
# add link of website converted to qr
qr.add_data("https://www.youtube.com/watch?v=zj7upE8-VQg")

qr.make(fit=True)
# alter the color and size of qr
img=qr.make_image(fill_color="yellow",back_color="white")
img.save("C://Users//bansa//Desktop//python_projects//qrcode1.png")
