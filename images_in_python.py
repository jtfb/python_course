from PIL import Image

mac = Image.open('example.jpg')

mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)

#Cropping Images
mac.crop((0,0,100,100))
mac.save('example_cropped.jpg')

# cropped = Image.open('cropped.jpg')