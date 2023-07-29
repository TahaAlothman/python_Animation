from PIL import Image
import os



folder=input('Enter the Name of Folder :')
logo_name=input('Enter the logo Name :')

os.chdir('image')

if not os.path.isdir(folder):
    os.mkdir(folder)



logo=Image.open(logo_name)
logo_width, logo_height=logo.size



for filename in os.listdir('.'):
    if filename.endswith((".jpeg",".jpg",".png")):
        image=Image.open(filename)
        width ,height = image.size
        
        image.paste(logo,(width-logo_width , height-logo_height),logo)
        image.save(os.path.join(folder,filename.lower()))


