import random
from faker import Faker
import shortuuid
from faker_commerce import Provider
from ..model import EventModel, IdRepo, ArrayModel
from datetime import datetime
fake = Faker("fr_FR")
fake.add_provider(Provider)

customer = EventModel({
    "id": shortuuid.uuid,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'email': fake.email,
    'phone': fake.phone_number,
    'address': fake.address,
    'city': fake.city,
    'zip_code': fake.postcode,
    'country': fake.country
})

employee = EventModel({
    "id": shortuuid.uuid,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'email': fake.email,
    'job_title': fake.job,
    'hire_date': lambda: fake.past_datetime().isoformat(timespec='milliseconds'),
    'phone': fake.phone_number,
    'address': fake.address,
    'city': fake.city,
    'zip_code': fake.postcode,
    'country': fake.country
})

supplier = EventModel({
    "id": shortuuid.uuid,
    'name': fake.company,
    'contact_person': fake.name,
    'email': fake.company_email,
    'phone': fake.phone_number,
    'address': fake.address,
    'city': fake.city,
    'zip_code': fake.postcode,
    'country': fake.country
})


store = EventModel({
    "id": shortuuid.uuid,
    'name': fake.company,
    'phone': fake.phone_number,
    'email': fake.company_email,
    'address': fake.address,
    'city': fake.city,
    'zip_code': fake.postcode,
    'country': fake.country
})

product = EventModel({
    'id': shortuuid.uuid,
    'name': fake.ecommerce_name,
    'description': fake.catch_phrase,
    'category':  fake.ecommerce_category,
    'retail_price': lambda: round(random.uniform(1, 1000), 2),
    'supplier_price': lambda: round(random.uniform(1, 800), 2),
    'supplier_id': IdRepo("suppliers")
})

order = EventModel({
    "id": shortuuid.uuid,
    'order_date': lambda:  datetime.now().isoformat(timespec='milliseconds'),
    'status': lambda: fake.random_element(elements=['Pending', 'Processing', 'Completed']),
    'items': ArrayModel(
        EventModel({
            'quantity': lambda: random.randint(1, 10),
            'unit_price': lambda:  round(random.uniform(1, 1000), 2),
            'product_id': IdRepo("products")
        }),
        size=lambda: random.randint(1, 10)
    ),
    'customer_id': IdRepo("customers"),
    'store_id': IdRepo("stores"),
    'employee_id': IdRepo("employees"),
})
"".lower()

mytest = EventModel({
    "id" : shortuuid.uuid,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'email': lambda __first_name,__last_name : f"{__first_name.lower()}.{__last_name.lower()}@{fake.free_email_domain()}" ,
})
