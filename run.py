from database.database_method import save_only_new_offer, delete_non_actual
from tg_client.tg import send_parse_info, send_error_info
from platforms.basketshop.basketshop import Basketshop
from loguru import logger

@logger.catch
def basketshop_parse():
    try:
        basketshop_client = Basketshop()
        list_shoes = basketshop_client.parse()
        print(list_shoes)

        list_shoes_id = []
        for shoes in list_shoes:
            shoes_db = save_only_new_offer(
                name=shoes['name'],
                price=shoes['price'],
                image_url=shoes['image_url'],
                discount_percent=shoes['discount'],
                platform='basketshop',
                unique_id=shoes['data_id']
            )
            if shoes_db != None:
                send_parse_info(shoes_db=shoes_db)
            list_shoes_id.append(shoes['data_id'])
        delete_non_actual(list_shoes_id=list_shoes_id, platform='basketshop')
    except:
        send_error_info(platform="basketshop")
        logger.exception("BasketshopParseFailed")

if __name__ == "__main__":
    logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB")
    basketshop_parse()
