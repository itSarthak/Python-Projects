# Import the required package
import qrcode

# Take input from the user
website_link = input("Enter the website link (add 'https://www.' beforehand): ")
file_name = input("Enter the file name you want to save it as(Enter '.png' after the name): ")

# Define the size of qr code you want
qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)

# Passing the website link into the qr function
qr.add_data(website_link)

# Making the qrcode by calling make() methon
qr.make()

# Fillling the qr with color and saving the image
img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save(file_name)