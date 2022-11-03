from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum


router = APIRouter(
    prefix='/employee',
    tags=['employee']
)


@router.post('/new')
def create_employee():
    pass 


@router.get('/new')
def create_employee():
    pass 
