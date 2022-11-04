from typing import Optional
from fastapi import APIRouter, status, Response
from enum import Enum
from pydantic import BaseModel


router = APIRouter(
    prefix='/employee',
    tags=['employee']
)


@router.get('/{id}')
def get_employee_information():
    employee_information = {
    'Employee#1': {'id': 'd441', 'firstname': 'José Luis', 'country': 'México', 'city': 'Tampico', 'phonenumber': '8335387753'},
    'Employee#2': {'id': 'd443', 'firstname': 'Pedro', 'country': 'México', 'city': 'Jalisco', 'phonenumber': '8335697753'},
    'Employee#3': {'id': 'd461', 'firstname': 'Juan', 'country': 'México', 'city': 'Monterrey', 'phonenumber': '8335382253'}
    }
    return employee_information


@router.get('/{name}/company/{company_name}', status_code=status.HTTP_200_OK)
def create_employee(name: str, company: str, response: Response):
    companies = ['Uber', 'Didi', 'Pemex']
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



@router.post('/{id}')
def create_employee():
    pass

@router.delete('/{id}')
def delete_employee():
    pass

