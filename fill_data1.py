def prepare_data(companies, employees, posts) -> tuple():
    for_companies = []
# przygotowanie listy krotek z nazwami firm
    for company in companies:
        for_companies.append((company, ))

    for_employees = []# dla tabeli employees

    for emp in employees:
        '''
        Aby wprowadzić dane do tabeli pracowników, musimy dodać stanowisko i identyfikator firmy. Domyślnie mieliśmy tyle firm:
        NUMBER_COMPANIES. Podczas tworzenia tabeli companies zaznaczyliśmy, że wartości w kolumnie id będą INTEGER AUTOINCREMENT - czyli
        każdy rekord będzie miał przypisany kolejny numer zwiększony o 1, zaczynając od 1. Dlatego firma jest
        wybierana losowo w dostępnym przedziale liczbowym.
        '''
        for_employees.append((emp, choice(posts), randint(1, NUMBER_COMPANIES)))

    '''
    Podobne operacje wykonamy w tabeli payments z wynagrodzeniami. Załóżmy, że wypłaty wynagrodzeń we wszystkich firmach
    odbywały się od 10 do 20 dnia każdego miesiąca. Wygenerujemy widełki wynagrodzeń w zakresie od 1000 do 10000 jednostek jakiejś waluty
    w każdym miesiącu i w przypadku każdego pracownika.
    '''
    for_payments = []

    for month in range(1, 12 + 1):
# Pętla po miesiącach'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_EMPLOYESS + 1):
# Pętla po pracownikach
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_companies, for_employees, for_payments
