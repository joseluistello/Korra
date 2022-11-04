from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.post('/new')
def create_operations():
    pass 


@router.get('/new')
def get_operations():
    pass 

@router.get('/new')
def delete_operations():
    pass
