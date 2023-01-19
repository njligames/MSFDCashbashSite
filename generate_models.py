
#!/usr/local/bin/python3

import sys
import csv

txt = """
<div
  class="modal fade bd-example-modal-lg"
  id="exampleModal{ticket_number}"
  tabindex="-1"
  role="dialog"
  aria-labelledby="exampleModalLabel"
  aria-hidden="true"
>
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Cash Bash Ticket</h5>
        <button
          type="button"
          class="close"
          data-bs-dismiss="modal"
          aria-label="Close"
        >
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body" id="exampleModalBody">
        <h1 style="text-align: center"><strong>1st Prize: $10,000</strong></h1>
        <h1 style="text-align: center"><strong>2nd Prize: $2,500</strong></h1>
        <h1 style="text-align: center"><strong>13 Prizes: $500.00</strong></h1>
        <h1 style="text-align: center"><strong>10 Prizes: $100.00</strong></h1>
        <div>&nbsp;</div>
        <ol>
          <li>$100.00 Per Ticket. Winner need not be present.</li>
          <li>
            All numbers will be drawn on September 24th, 2022 at the Mt. Sinai
            Fire Department, Station 1, 133 Mount Sinai Avenue.
          </li>
          <li>
            Gates will open at 1 pm and event will run until 5 pm, rain or
            shine.
          </li>
          <li>All winning numbers are re-entered for additional prizes.</li>
          <li>
            Only 2 ADULTS per ticket will be allowed entry. Please bring your
            own lawn chair.
          </li>
          <li>
            Only (up to) 500 tickets will be sold. Tickets must be shown at the
            gate for entry.
          </li>
          <li>No one under 21 will be admited. NO EXCEPTIONS!!!</li>
          <li>
            <strong
              >All tickets will be mailed to the address you put on the
              application once your check clears. Tickets purchased after
              9/1/2022 can be picked up at the gate with photo ID.</strong
            >
          </li>
          <li>
            You can choose your personal number 1-500. If a ticket number choice
            is not available, a random number will then be sent to you in its
            place.
          </li>
          <li>
            For additional questions contact: Cash Bash Committee at:
            msfdcashbash@gmail.com
          </li>
          <li>
            Entertainment, BBQ and drinks will be available during drawing, all
            included with ticket purchase.
          </li>
        </ol>
        <p>
          <strong
            >IF LESS THAN 500 TICKETS ARE SOLD, ALL PRIZES WILL BE PRO-RATED AT
            60% OF TOTAL SOLD</strong
          >
        </p>
      </div>
      <div class="col-xs-1" align="center">


        <form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
           <input type="hidden" name="cmd" value="_s-xclick">
           <input type="hidden" name="hosted_button_id" value="{cart_value}">
           <table>
              <tr>
                 <td><input type="hidden" name="on0" value="Cash Bash Ticket #{ticket_number}">Cash Bash Ticket #{ticket_number}</td>
              </tr>
              <tr>
                 <td>
                    <select name="os0">
                       <option value="Ticket">Ticket $100.00 USD</option>
                       <option value="Ticket & Chance">Ticket & Chance $105.00 USD</option>
                    </select>
                 </td>
              </tr>
              <tr>
                 <td><input type="hidden" name="on1" value="Winner Contact #">Winner Contact #</td>
              </tr>
              <tr>
                 <td><input type="text" name="os1" maxlength="200"></td>
              </tr>
           </table>
           <input type="hidden" name="currency_code" value="USD">
           <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_cart_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
           <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
        </form>

      </div>
      <div class="modal-footer"></div>
    </div>
  </div>
</div>

"""

filename="cart_values.csv"
if(len(sys.argv) > 1):
    filename="cart_values_test.csv"

with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        ticket_number=row["ticket_number"]
        cart_value=row["cart_value"]

        print(txt.format(ticket_number = ticket_number, cart_value = cart_value))
