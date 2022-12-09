
#!/usr/bin/python

import csv


with open('tickets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    col=1
    idx=1
    for row in reader:
        text='<button onclick="initPayPalButton' + str(idx) + '()" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal' + str(idx) + '" data-whatever="{}">Ticket {}</button>'
        text_disabled='<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal' + str(idx) + '" data-whatever="{}" disabled>Ticket {}</button>'

        if 1 == col:
            print('<div class="row justify-content-md-center">')

        print('<div class="col d-grid gap-2">')
        if row['available'] == "true":
            print(text.format(row['ticket_number'], row['ticket_number']))
        else:
            print(text_disabled.format(row['ticket_number'], row['ticket_number']))
        print('</div>')

        col += 1
        idx += 1

        if 6 == col:
            print('</div></br>')
            col = 1

