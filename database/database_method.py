from database.db import Base, engine, SessionLocal
from database.db_models import Shoes, Platforms

from datetime import datetime

import requests
import os
from config import basedir

from sqlalchemy import and_

from contextlib import suppress

def save_offer(name, price, discount_percent, image_url, platform, unique_id):
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    # ----------------------------------------- save img ---------------------------------------------------------------
    img = requests.get(image_url).content
    f_name = os.path.join(
        os.path.join(basedir, 'static/shoes_image'),
        f"{platform}_{name}_{datetime.now().strftime('%d-%m-%Y %H-%M')}.jpg"
    ).replace('\\', '/')
    with open(f_name, 'wb') as f:
        f.write(img)
    # ------------------------------------------------------------------------------------------------------------------

    platform_ex = db.query(Platforms).filter_by(name=platform).first()
    new_shoes = Shoes(
        name=name,
        price=price,
        discount_percent=discount_percent,
        platform=platform_ex,
        img_path=f_name,
        unique_id=unique_id
    )
    db.add(new_shoes)
    db.commit()

    return db.query(Shoes).filter_by(id=new_shoes.id).first()

def save_only_new_offer(name, price, discount_percent, image_url, platform, unique_id):
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)

    # ----------------------------------------------- check already ----------------------------------------------------
    platform_id = db.query(Platforms).filter_by(name=platform).first().id
    shoes = db.query(Shoes).filter(
        (Shoes.name == name) &
        (Shoes.price == price) &
        (Shoes.platform_id == platform_id) &
        (Shoes.unique_id == unique_id)
    ).first()
    if shoes == None:
        new_shoes = save_offer(name=name, price=price, discount_percent=discount_percent, image_url=image_url, platform=platform, unique_id=unique_id)
        return new_shoes
    else:
        return None

def delete_non_actual(list_shoes_id, platform):
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    for shoes in db.query(Platforms).filter_by(name=platform).first().shoes:
        if list_shoes_id.count(shoes.unique_id) == 0:
            print(f'Удаляем {shoes.unique_id}')
            with suppress(Exception):
                os.remove(shoes.img_path)
            db.delete(shoes)
    db.commit()

if __name__ == '__main__':
    save_only_new_offer('a', '3', '30', 'https://www.basketshop.ru/files/catalog/34595/AJ5587-312(3).JPG', 'basketshop', "1")
    # delete_non_actual(['2'], 'basketshop')