import requests
from django.db import IntegrityError
from django.shortcuts import HttpResponse,render 
from .models import Company, Employee, Offer

# Create your views here.


def index(request):
    companies = Company.objects.all()
    error=""
    context = {"companies": companies, "msg": error}
    return render(request, "index.html", context)


def info(request):
    headers = {
        "Authorization": "Basic dXNlcjE6azdSMkxKSHdTQm1qRXRDdg==",
    }

    response = requests.get("http://49.12.237.145:5150/", headers=headers)

    if response.status_code == 401:
        companies = Company.objects.all()
        context ={"companies": companies,"msg": "A company with this display name already exists"}
        return render(request, "index.html", context)

    if response.status_code == 200:
        data = response.json()

        company_data = {
            "address_detail": data["company"]["address_detail"],
            "city_name": data["company"]["city_name"],
            "display_name": data["company"]["display_name"],
            "region_name": data["company"]["region_name"],
            "zip_code": data["company"]["zip_code"],
        }
        print(company_data)
        try:
            company = Company.objects.create(**company_data)
            company.save()
        except IntegrityError:
            companies = Company.objects.all()
            context ={"companies": companies,"msg": "A company with this display name already exists"}
            return render(request, "index.html", context)

        company_employees_data = []
        for employee in data["company_employees"]:
            empl = Employee.objects.create(
                pk=employee["employee_id"],
                company_id=company,
                email=employee["email"],
                fullname=employee["fullname"],
                phoneNumber=employee["phoneNumber"],
            )
            empl.save()

        offer_data = {
            "company_id": company,
            "product_1_budget": data["offer"]["product_1_budget"],
            "product_1_issuing_value": data["offer"]["product_1_issuing_value"],
            "product_1_mailing_value": data["offer"]["product_1_mailing_value"],
            "product_1_value": data["offer"]["product_1_value"],
            "product_2_budget": data["offer"]["product_2_budget"],
            "product_2_issuing_value": data["offer"]["product_2_issuing_value"],
            "product_2_mailing_value": data["offer"]["product_2_mailing_value"],
            "product_2_value": data["offer"]["product_2_value"],
            "product_3_budget": data["offer"]["product_3_budget"],
            "product_3_issuing_value": data["offer"]["product_3_issuing_value"],
            "product_3_mailing_value": data["offer"]["product_3_mailing_value"],
            "product_3_value": data["offer"]["product_3_value"],
        }

        offer = Offer.objects.create(**offer_data)
        offer.save()
        
        companies = Company.objects.all()
        context ={"companies": companies, "msg": ""}
    return render(request, 'index.html', context)


def get_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    offer = Offer.objects.get(company_id=company_id)
    employees = Employee.objects.filter(company_id=company_id)
    response = {"company": company, "offer":offer, "employees": employees}
    return render(request, "company.html", response)