import pymongo, base64, datetime, io
from PIL import ImageTk, Image

from resizeimage import resizeimage

import hashlib


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

    arg = {'username': usr, 'password': pss}
    rs = db.Users.find(arg)

    if db.Users.count_documents(arg) == 1:
        print(rs[0])
        print('login success')
        return rs[0]
    else:
        print('login fail')
        return None


# FRIEND
def get_user_by_word(word, userid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    arg = {'displayname': {'$regex': f'^{word}', '$options': 'i'}, '_id': {'$ne': userid}}
    rs = db.Users.find(arg).sort([("displayname", 1)])

    print(db.Users.count_documents(arg))

    _data = []
    for x in rs:
        _data.append(x)

    print(_data)
    return _data


def get_user_friend(follower):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    arg = {'_id': follower}
    rs = db.Users.find(arg)
    followed_list = rs[0]['friend']
    print(followed_list)
    return followed_list


def follow(user, follower):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'_id': user})
    follower_list = rs[0]['friend']
    follower_list.append(follower)
    print(follower_list)

    db.Users.update_one({'_id': user}, {'$set': {'friend': follower_list}})
    print(f"total friend: {len(follower_list)}")


def unfollow(follower, followed):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'_id': follower})
    followed_list = rs[0]['friend']
    followed_list.remove(followed)
    print(followed_list)

    db.Users.update_one({'_id': follower}, {'$set': {'friend': followed_list}})

    print(f"total friend: {len(followed_list)}")


# UPLOAD IMAGE
def get_preview_image(path):
    cover = resize_img(path)
    buf = io.BytesIO()
    cover.save(buf, format='PNG')
    byte_im = buf.getvalue()

    str = base64.encodebytes(byte_im)
    return str


def resize_img(path):
    with open(f'{path}', 'r+b') as f:
        new_name = f'rs{datetime.datetime.today()}.png'
        with Image.open(f) as image:
            cover = resizeimage.resize_height(image, 300)
            # cover.show()
            # cover.save(f'resource/{new_name}', image.format)
        return cover


def upload_image_by_path(path, caption, user):
    cover = resize_img(path)
    buf = io.BytesIO()
    cover.save(buf, format='PNG')
    byte_im = buf.getvalue()

    str = base64.encodebytes(byte_im)

    try:
        client = pymongo.MongoClient(
            "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
        db = client.get_database('FinalProject')

        ins = db.Images.insert_one(
            {"_id": f"i{db.Images.count_documents({})}", "imagestr": str, "caption": caption, "like": 0,
             "like_list": [], "owner": user, "timestamp": datetime.datetime.today()})
        print(f'{ins.inserted_id}')

    except Exception as e:
        print(e)


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
            {"_id": f"i{db.Images.count_documents({})}", "imagestr": str, "caption": caption, "like": 0,
             "like_list": [], "owner": user, "timestamp": datetime.datetime.today()})
        print(f'{ins.inserted_id}')

    except Exception as e:
        print(e)


# GET IMAGE

def getOwnerName(id):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'_id': id})
    print(rs[0]['displayname'])
    return rs[0]['displayname']


def getImage(imgstr):
    imgdata = base64.b64decode(imgstr)
    # img = Image.open(io.BytesIO(imgdata))
    # img.show()
    # return img
    return imgdata


def get_all_user_image_str(user):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'owner': user}).sort([('timestamp', -1)])
    img_list = []

    for x in rs:
        img_list.append(x["imagestr"])

    print(img_list)
    return img_list
    # return rs


def get_all_user_image_data(user):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'owner': user}).sort([('timestamp', -1)])
    _data = []
    for x in rs:
        _data.append(x)

    return _data


def get_feed_image_str(userid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'_id': userid})
    friend_list = rs[0]['friend']
    print(friend_list)
    rs2 = db.Images.find({'owner': {'$in': friend_list}}).sort([('timestamp', -1)])

    img_list = []
    for x in rs2:
        img_list.append(x["imagestr"])

    print(img_list)
    return img_list
    # return rs2


def get_feed_image_data(userid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Users.find({'_id': userid})
    friend_list = rs[0]['friend']
    friend_list.append(userid)
    print(friend_list)
    rs2 = db.Images.find({'owner': {'$in': friend_list}}).sort([('timestamp', -1)])
    _data = []
    for x in rs2:
        _data.append(x)
    return _data


# MANAGE IMAGE
def like(pid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'_id': pid})
    newlike = rs[0]['like'] + 1
    db.Images.update_one({'_id': pid}, {'$set': {'like': newlike}})

    print(f"total like: {newlike}")


def getUserLiked(pid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    rs = db.Images.find({'_id': pid})
    _list = rs[0]['like_list']
    return _list


def edit_caption(pid, newcaption):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    db.Images.update_one({'_id': pid}, {'$set': {'caption': newcaption}})

    print(f"new caption: {newcaption}")


def delete_image(pid):
    client = pymongo.MongoClient(
        "mongodb+srv://nelynx:nae181240@cluster0-xuwau.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database('FinalProject')

    db.Images.delete_one({'_id': pid})


if __name__ == "__main__":
    # register('a6', 'a', 'a6sang')
    # login('a', 'a')
    #
    # get_user_by_word('a')
    # follow('u0', 'u1')
    # unfollow('u0', 'u3')

    # upload_image(resize_img('resource/c2.png'), 'test', 'u0')
    # upload_image_by_path('resource/c2.png', 'testadd', 'u0')
    # print(len(get_all_user_image_str('u0')))
    # for x in get_all_user_image_str('u0'):
    #     getImage(x)

    # print(len(get_feed_image_str('u1')))
    # for x in get_feed_image_str('u1'):
    #     getImage(x)

    # like('i0')

    # edit_caption('i0', 'newc')
    # delete_image('i4')

    # get_all_user_image_data('u0')
    # getOwnerName('u0')

    # print(hashlib.md5('ca'.encode()).hexdigest())

    print(get_feed_image_data('u0')[0]['_id'])
