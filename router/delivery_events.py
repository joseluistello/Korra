from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/delivery_events',
    tags=['delivery_events']
)


@router.post('/{EmployeeId}')
def create_delivery():
    return "You create a new event"


@router.get('/{EmployeeId}')
def get_delivery():
    return "Take all events"

@router.delete('/{EmployeeId}')
def delete_delivery():
    return "You delete a event"



### Global Variables 

