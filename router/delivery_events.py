from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/delivery_events',
    tags=['delivery_events']
)


@router.post('/new')
def create_delivery():
    pass 


@router.get('/new')
def get_delivery():
    pass 

@router.get('/new')
def delete_delivery():
    pass

