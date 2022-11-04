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

@router.delete('/new')
def delete_operations():
    pass


### Global Variable

operations_info = {
'Employee#1': {'TaxId': '3332', 'JobType':'Delivery', 'Rating':'4.51', 'LifeTimeTrips':'1,500', 'Status':'Active', 'CanceledTrips':'15'},
'Employee#2': {'TaxId': '3333', 'JobType':'Trip', 'Rating':'4.82', 'LifeTimeTrips':'5,000', 'Status':'Active', 'CanceledTrips':'40'},
'Employee#3': {'TaxId': '3334', 'JobType':'Delivery', 'Rating':'4.64', 'LifeTimeTrips':'800', 'Status':'Inactive', 'CanceledTrips':'8'}
}
