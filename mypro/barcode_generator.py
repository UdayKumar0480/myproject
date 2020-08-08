'''
import barcode
from barcode.writer import ImageWriter
data = '123456123'
data1 = str(data)
coder = barcode.get_barcode_class('code128')
write = coder(data,writer=ImageWriter())
result = write.save('barcode1')
print(write)
'''


import barcode

provi = (barcode.PROVIDED_BARCODES) #Bar code Providers
print("Bar Code Providers are:", provi)
bar = barcode.get('code128', '12345678')
# Now we look if the checksum was added
bar.get_fullcode()
u'12345678'
filename = bar.save('code128')
filename
u'code128.svg'
options = dict(compress=True)
filename = bar.save('code128', options)
filename
u'code128.svgz'