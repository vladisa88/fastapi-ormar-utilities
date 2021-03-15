from ormar.exceptions import NoMatch

from fastapi import HTTPException


def handle_exception(fetch_function):
    """
    Decorator for handling ormar `NoMatch` exceptions
    """
    async def wrapper(*args, **kwargs):
        try:
            return await fetch_function(*args, **kwargs)
        except NoMatch:
            return HTTPException(status_code=404, detail='Item not found')
    return wrapper
