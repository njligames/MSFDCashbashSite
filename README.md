# Mount Sinai Fire Department Cash Bash Website

The site was written using Bootstrap v5.

## Button management
The ticket inventory is managed such that tickets can be bought in person AND online.  
The solution to allow for this was to have paypal buttons that have an inventory of one.  
Whether a person buys a ticket in-person or online, the website maintainer needs to be notified to update the website.  

### Ticket sales worflow
If a person buys a ticket online, paypal will not allow the same ticket to be bought again. If a person buys a ticket in-person, the website maintainer needs to be notified so that the same ticket cannot be bought again. The website should be updated either way.

#### Updating website
1. Edit the tickets.csv file such that the `available` column value of the `ticket_number` to `FALSE` for each ticket sold and save it. 
2. Run: `python3 generate_buttons.py | pbcopy` in the MacOS Terminal. This will put the updated html into your clipboard.
3. Edit the `index.html` file and change the code that is between: `<!-- generate_buttons start-->` and `<!-- generate_buttons end-->` and save it.
4. Upload the index.html file to the server.

## Utilities
* The `generate_models.py` utility is used to generate the bootstrap models. A model need to be coded for each ticket. It is updated in a simliar way as the `generate_buttons.py`.



# Reports 

https://www.paypal.com/reports/dlog


# Saved Button
https://www.paypal.com/cgi-bin/webscr?cmd=_button-management&login_cmd=_button-management


