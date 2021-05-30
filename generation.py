# qrcodegeneration
import qrcode
qr=qrcode.QRCode(
  version=1,
  box_size=10,
  border=5,
  )

data="685603,GECI,Painavu"
qr.add_data(data)
qr.make(fit=true)
img=qr.make_image(fill="black",back_color="white")
img.save("1.png")
