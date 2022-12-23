
#!/usr/local/bin/python3

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

with open('tickets.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    print('<div class="row gap-2">')
    for row in reader:
        ticket_number=row["ticket_number"]

        if row['available'] == "true":
            print(available.format(ticket_number = row['ticket_number']))
        else:
            print(disabled.format(ticket_number = row['ticket_number']))
    print('</div>')
