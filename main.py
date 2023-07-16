import qrcode

#Data inside the QRCode
data = input("What is the data: ")

#Define QRCode Generator
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Create QRCode Image
image = qr.make_image()

#Save Image
image.save(f"{data}.png")