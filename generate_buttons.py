
#!/usr/bin/python

import csv

text='<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-whatever="{}">Ticket {}</button>'
text_disabled='<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-whatever="{}" disabled>Ticket {}</button>'

with open('tickets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    col=0
    for row in reader:

        if 0 == col:
            print '<div class="row justify-content-md-center">'

        print '<div class="col d-grid gap-2">'
        if row['available'] == "true":
            print text.format(row['ticket_number'], row['ticket_number'])
        else:
            print text_disabled.format(row['ticket_number'], row['ticket_number'])
        print '</div>'

        col += 1

        if 5 == col:
            print '</div></br>'
            col = 0


# text='<button type="button" class="btn btn-primary btn-lg btn-block" data-bs-toggle="modal" data-bs-target="#exampleModal" data-whatever="{}">Ticket {}</button>'
# text_disabled='<button type="button" class="btn btn-primary btn-lg btn-block" data-bs-toggle="modal" data-bs-target="#exampleModal" data-whatever="{}" disabled>Ticket {}</button>'
#
#
# col=0
# for i in range(1,501):
    # if 0 == col:
    #     print '<div class="row justify-content-md-center">'

    # print '<div class="col">'
    # print text_disabled.format(i, i)
    # print '</div>'

    # col += 1

    # if 5 == col:
    #     print '</div>'
    #     col = 0
