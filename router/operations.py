from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(
    prefix='/operations',
    tags=['operations']
)


@router.get('/{EmployeeId}')
def get_operations():
    operations_info = {
    'Employee#1': {'TaxId': '3332', 'JobType':'Delivery', 'Rating':'4.51', 'LifeTimeTrips':'1,500', 'Status':'Active', 'CanceledTrips':'15'},
    'Employee#2': {'TaxId': '3333', 'JobType':'Trip', 'Rating':'4.82', 'LifeTimeTrips':'5,000', 'Status':'Active', 'CanceledTrips':'40'},
    'Employee#3': {'TaxId': '3334', 'JobType':'Delivery', 'Rating':'4.64', 'LifeTimeTrips':'800', 'Status':'Inactive', 'CanceledTrips':'8'}
    }
    return operations_info


@router.get('/{taxid}/status/', status_code=status.HTTP_200_OK)
def create_operations(taxid: str, response: Response):
    Taxid = ['3333']
    """
    Simulates retrieving a specific id an status
    - *taxid** mandatory path parameter
    """
    if taxid not in Taxid:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'taxid {taxid} not found'}
    else:
        response.status_code = status.HTTP_200_OK
    return {'taxid': f'taxid: {taxid}, status: Active'}



    





