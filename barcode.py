import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

# Teks yang akan diubah menjadi barcode
data = "123456789012"

# Membuat objek barcode EAN-13
ean = EAN13(data, writer=ImageWriter(), add_checksum=False)

# Menyimpan barcode dalam bentuk gambar
barcode_file = ean.save('ean13_barcode')
