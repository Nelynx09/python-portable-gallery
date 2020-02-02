import pymongo
from tkinter import *
from PIL import ImageTk, Image

from resizeimage import resizeimage

import base64

import io

import datetime


# with open("resource/c1.png", "rb") as imageFile:
#     print(type(imageFile))
#
#     str = base64.encodebytes(imageFile.read())
#
#
# image_data = base64.decodebytes(str)
# image = Image.open(io.BytesIO(image_data))
# image.show()


def resize_img(filename):
    with open(f'resource/{filename}', 'r+b') as f:
        new_name = f'rs{datetime.datetime.today()}.png'
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [300, 300])
            cover.save(f'resource/{new_name}', image.format)
        return new_name


def insert_to_mongodb_clound(filename):
    with open(f"resource/{filename}", "rb") as imageFile:
        str = base64.encodebytes(imageFile.read())
        try:
            client = pymongo.MongoClient(
                "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
            # db = client.test
            db = client.get_database('test_img')
            rs = db.Products.find({})
            ins = db.Products.insert_one(
                {"pid": f"i00{len(list(rs))}", "imagestr": str})
            print(f'{ins.inserted_id}')
        except Exception as e:
            print(e)


def getImage():
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('test_img')
    rs = db.Products.find({})

    imgdata = base64.b64decode(rs[2]["imagestr"])
    img = Image.open(io.BytesIO(imgdata))
    return img


print()
# insert_to_mongodb_clound(resize_img('c3.jpeg'))

root = Tk()

root.geometry("500x500")
root.title("Example of GUI by Tkinter")

# canvas = Canvas(root, width=300, height=300)
# canvas.pack()
img = ImageTk.PhotoImage(getImage())
# canvas.create_image(0, 0, anchor=NW, image=[img])

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, Image(img))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)


Label(root, text='Some', image=img).pack(side="top")
Label(root, text='Some', image=img).pack(side="top")
Label(root, text='Some', image=img).pack(side="top")

root.mainloop()
