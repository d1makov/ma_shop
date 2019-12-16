"""
CRUD
"""


def add_to(con, user_id: int, product_id: int) -> None:
    """
    Add new prodact and 
    user id to cart.
    :param con: str
    :param id_user: int
    :param id_product: int
    :return: None
    """
    with con.cursor() as cursor:
        cursor.execute("""INSERT INTO postgres.public.cart(user_id, product_id)
                            VALUES ('{}', '{}')""".format(user_id, product_id))
        try:
            cursor.fetchone()
        except TypeError:
            raise KeyError
    con.commit()


def get_all_from(con, user_id: int) -> list:
    """
    Get all products_id from db using index user_id.
    :param con: str
    :param product_id: int
    :return: list
    """
    with con.cursor() as cursor:
        cursor.execute("""SELECT product_id FROM postgres.public.cart
                    WHERE user_id = {}""".format(user_id))
        try:
            cursor.fetchone()
        except TypeError:
            raise KeyError
    result = cursor.fetchall()
    return [''.join(i) for i in result]


def get_one_from(con, user_id: int, prod) -> str:
    """
    Get product from db using index parameter.
    :param con: str
    :param product_id: int
    :return: str
    """
    with con.cursor() as cursor:
        cursor.execute("""SELECT product_id FROM postgres.public.cart
                    WHERE id_user = {}""".format(user_id))
        try:
            cursor.fetchone()
        except TypeError:
            raise KeyError
    result = cursor.fetchone()
    return result[0]


def delete_from(con, user_id, product_id,) -> None:
    """
    Delete task in db.
    :param con: str
    :param product_id: int
    :return: None
    """
    with con.cursor() as cursor:
        cursor.execute("""DELETE FROM postgres.public.cart 
                        WHERE (user_id, product_id) VALUES ({}, {})""".format(user_id, product_id))
        try:
            cursor.fetchone()
        except TypeError:
            raise KeyError
    con.commit()
