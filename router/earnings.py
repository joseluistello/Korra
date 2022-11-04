from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum



router = APIRouter(
    prefix='/earnings',
    tags=['earnings']
)


@router.post('/new')
def create_earnings():
    pass 


@router.get('/new')
def get_earnings():
    pass 

@router.delete('/new')
def delete_earnings():
    pass

