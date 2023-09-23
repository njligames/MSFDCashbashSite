
#!/usr/local/bin/python3

import sys
import csv

available="""
<button
    type="button"
    class="btn btn-primary btn-custom"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal{ticket_number}"
    data-whatever="{ticket_number}">Ticket #{ticket_number}
</button>
"""

disabled="""
<button
    type="button"
    class="btn btn-primary btn-custom"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal{ticket_number}"
    data-whatever="{ticket_number}"
    disabled>Ticket #{ticket_number}
</button>
"""

filename="tickets.csv"
if(len(sys.argv) > 1):
    filename="tickets_test.csv"

num_sold=0
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)

    print('<div class="row gap-2">')
    for row in reader:
        ticket_number=row["ticket_number"]

        if row['available'].lower() == "true":
            print(available.format(ticket_number = row['ticket_number']))
        else:
            num_sold = num_sold + 1
            print(disabled.format(ticket_number = row['ticket_number']))
    print('</div>')

print("number sold = " + str(num_sold))
