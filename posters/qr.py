"""QR (korekce H, tichá zóna 4 moduly) jako SVG data URI."""
import io, base64, qrcode, qrcode.image.svg
def qr_data_uri(url:str)->str:
    q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,border=4,box_size=10)
    q.add_data(url); q.make(fit=True)
    img=q.make_image(image_factory=qrcode.image.svg.SvgPathImage)
    buf=io.BytesIO(); img.save(buf)
    return "data:image/svg+xml;base64,"+base64.b64encode(buf.getvalue()).decode()
