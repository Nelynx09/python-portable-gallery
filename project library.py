import pymongo, base64, datetime, io
from PIL import ImageTk, Image

from resizeimage import resizeimage


# ACCOUNT
def register(usr, pss, displayname):
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('FinalProject')

        if db.Users.count_documents({'username': usr}) > 0:
            return False
        else:
            ins = db.Users.insert_one(
                {"uid": f"u{db.Users.count_documents({})}", "username": usr, "password": pss,
                 "displayname": displayname, "friend": []})
            print(f'{ins.inserted_id}')
            return True
    except Exception as e:
        print(e)


def login(usr, pss):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'username': usr, 'password': pss})

    if len(list(rs)) == 1:
        print('login success')
        return True
    else:
        print('login fail')
        return False


# FRIEND
def get_user_by_word(word):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    arg = {'displayname': {'$regex': f'^{word}', '$options': 'i'}}
    rs = db.Users.find(arg)

    print(db.Users.count_documents(arg))

    for x in rs:
        print(f'{x["uid"]} - {x["displayname"]}')

    return list(rs)


def follow(follower, followed):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'uid': follower})
    followed_list = rs[0]['friend']
    followed_list.append(followed)
    print(followed_list)

    db.Users.update_one({'uid': follower}, {'$set': {'friend': followed_list}})
    print(f"total friend: {len(followed_list)}")


def unfollow(follower, followed):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'uid': follower})
    followed_list = rs[0]['friend']
    followed_list.remove(followed)
    print(followed_list)

    db.Users.update_one({'uid': follower}, {'$set': {'friend': followed_list}})

    print(f"total friend: {len(followed_list)}")


# UPLOAD IMAGE
def resize_img(path):
    with open(f'{path}', 'r+b') as f:
        new_name = f'rs{datetime.datetime.today()}.png'
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [300, 300])
            cover.show()
            # cover.save(f'resource/{new_name}', image.format)
        return cover


def upload_image(file, caption, user):
    buf = io.BytesIO()
    file.save(buf, format='PNG')
    byte_im = buf.getvalue()

    str = base64.encodebytes(byte_im)
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('FinalProject')

        ins = db.Images.insert_one(
            {"pid": f"i{db.Images.count_documents({})}", "imagestr": str, "caption": caption, "like": 0,
             "owner": user, "timestamp": datetime.datetime.today()})
        print(f'{ins.inserted_id}')

    except Exception as e:
        print(e)
    return True


# GET IMAGE

def getImage(imgstr):
    imgdata = base64.b64decode(imgstr)
    img = Image.open(io.BytesIO(imgdata))
    img.show()
    return img


def get_all_user_image_str(user):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'owner': user})
    img_list = []

    for x in rs:
        img_list.append(x["imagestr"])

    print(img_list)
    return img_list
    # return rs


def get_feed_image_str(userid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'uid': userid})
    friend_list = rs[0]['friend']
    print(friend_list)
    rs2 = db.Images.find({'owner': {'$in': friend_list}}).sort([('timestamp', -1)])

    img_list = []
    for x in rs2:
        img_list.append(x["imagestr"])

    print(img_list)
    return img_list
    # return rs2


# MANAGE IMAGE
def like(pid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'pid': pid})
    newlike = rs[0]['like'] + 1
    db.Images.update_one({'pid': pid}, {'$set': {'like': newlike}})

    print(f"total like: {newlike}")


def edit_caption(pid, newcaption):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    db.Images.update_one({'pid': pid}, {'$set': {'caption': newcaption}})

    print(f"new caption: {newcaption}")


def delete_image(pid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    db.Images.delete_one({'pid': pid})


if __name__ == "__main__":
    # register('a6', 'a', 'a6sang')
    # login('a', 'a')
    #
    # get_user_by_word('a')
    # follow('u1', 'u0')
    # unfollow('u0', 'u3')

    # upload_image(resize_img('resource/c4.jpeg'), 'test', 'u0')

    # print(len(get_all_user_image_str('u0')))
    # for x in get_all_user_image_str('u0'):
    #     getImage(x)

    # print(len(get_feed_image_str('u1')))
    # for x in get_feed_image_str('u1'):
    #     getImage(x)

    like('i0')

    # edit_caption('i0', 'newc')
    # delete_image('i4')
