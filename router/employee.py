from fastapi import APIRouter
from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum


router = APIRouter(
    prefix='/employee',
    tags=['employee']
)

@router.get('/all')
def get_employee_information():
    employee_information = {'Employee#1': {'id': 'd441', 'firstname': 'José Luis', 'country': 'México', 'city': 'Tampico', 'phonenumber': '8335387753'}}
    return employee_information



@router.post('/{name}/company/{company_name}', status_code=status.HTTP_200_OK)
def create_employee(name: str, company: str, response: Response):
    companies = ['uber', 'didi', 'pemex']
    """
    Simulates retrieving a name and company of an employee
    - **name** mandatory path parameter
    - **company** mandatory path parameter
    """
    if company not in companies:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'company {company} not found'}
    else:
        response.status_code = status.HTTP_200_OK
    return {'employee': f'employee_name: {name}, company: {company}'}


@router.get('/new')
def get_employee():
    pass 
