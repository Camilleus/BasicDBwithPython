from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_COMPANIES = 3
NUMBER_EMPLOYESS = 30
NUMBER_POST = 5

def generate_fake_data(number_companies, number_employees, number_post) -> tuple():
    fake_companies = []# tu będą przechowywane firmy
    fake_employees = []# tu będą przechowywane pracownicy
    fake_posts = []# tu będą przechowywane stanowiska
    '''Weźmy trzy firmy z Fakera i umieśćmy je w odpowiedniej zmiennej'''
    fake_data = faker.Faker()

# Tworzymy tyle firm: number_companies
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

# Generujemy tyle pracowników: number_employees'''
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

# Oraz tyle stanowisk: number_post
    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts
