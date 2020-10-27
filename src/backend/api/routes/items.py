from fastapi import APIRouter


router = APIRouter()


@router.get('/items/{item_id}')
async def get_item(item_id: int):
    return {'item': item_id}
