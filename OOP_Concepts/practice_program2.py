import qrcode

url = input("Enter URL: ")

img = qrcode.make(url)

img.save("qrcode.png")

print("QR Code generated successfully!")