from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum



router = APIRouter(
    prefix='/earnings',
    tags=['earnings']
)


@router.post('/{EmployeeId}')
def create_earnings():
    return "You create new earnings"


@router.get('/{EmployeeId}')
def get_earnings():
    return "Take all earnings"
    

@router.delete('/{EmployeeId}')
def delete_earnings():
    return "You delete earnings"

