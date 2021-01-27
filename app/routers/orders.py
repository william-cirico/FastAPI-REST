from fastapi import APIRouter

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.delete('/')
def delete_order():
    pass


@router.get('/')
def get_order():
    pass


@router.put('/')
def update_order():
    pass


@router.post('/')
def post_order():
    pass
