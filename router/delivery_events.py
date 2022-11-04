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

@router.delete('/new')
def delete_delivery():
    pass



### Global Variables 


operations_info = {
'Employee#1': {'Id': '3332', 'JobType':'Delivery', 'Rating':'4.51', 'LifeTimeTrips':'1,500', 'Status':'Active', 'CanceledTrips':'15'},
'Employee#2': {'Id': '3333', 'JobType':'Trip', 'Rating':'4.82', 'LifeTimeTrips':'5,000', 'Status':'Active', 'CanceledTrips':'40'},
'Employee#3': {'Id': '3334', 'JobType':'Delivery', 'Rating':'4.64', 'LifeTimeTrips':'800', 'Status':'Inactive', 'CanceledTrips':'8'}
}
