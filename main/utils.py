from main import models


def handle_uploaded_file(f, folder):
    with open(f'src/main/upload/{folder}/'+f.name, 'wb+') as destination:
        if f.multiple_chunks:
            for chunk in f.chunks():
                destination.write(chunk)
        else:
            destination.write(f.read())


def parse_xlsx(wb, active=None):
    if not active:
        sheet = wb.active
    else:
        sheet = wb[active]
    records = []
    lst = list(sheet.iter_rows(values_only=True))
    for i in range(1, len(lst)):
        obj = {}
        for j, val in enumerate(lst[i]):
            if val:
                obj[lst[0][j]] = lst[i][j]
        records.append(obj)

    return records


def add_client(record, key):
    try:
        client = models.Client.objects.get(name=record[key])
    except models.Client.DoesNotExist:
        client = models.Client.objects.create(
            name=record[key]
        )

    return client

def import_bills(wb):
    records = parse_xlsx(wb)

    for record in records:
        try:
            print(record['client_org'])
            org = models.Organization.objects.get(name=record['client_org'])
        except models.Organization.DoesNotExist:
            org = None
            print('Add org first')

        if org:
            number = round(record['№'])
            try:
                models.Bill.objects.get(number_org=str(number)+org.name)
            except models.Bill.DoesNotExist:
                print('org', org.name)
                print(record)
                models.Bill.objects.create(
                    number=number,
                    organization=org,
                    sum_bill=record['sum'],
                    date_created=record['date']
                )


def import_org(wb):
    records_org = parse_xlsx(wb, active='organization')
    records_client = parse_xlsx(wb)

    for record in records_client:
        add_client(record, 'name')

    for record in records_org:
        client = add_client(record, 'client_name')
        try:
            models.Organization.objects.get(name=record['name'])
        except models.Organization.DoesNotExist:
            models.Organization.objects.create(
                name=record['name'],
                clients=client
            )

