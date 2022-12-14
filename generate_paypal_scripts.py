
#!/usr/local/bin/python3

import csv

with open('tickets.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    col=1
    for row in reader:

        text = 'function initPayPalButton' + str(col) + '() { var ticketNumber = ' + str(col) + '; var shipping = 0; var itemOptions = document.querySelector( "#smart-button-container #item-options"); var quantity = parseInt(); var quantitySelect = document.querySelector( "#smart-button-container #quantitySelect"); if (!isNaN(quantity)) { quantitySelect.style.visibility = "visible"; } var orderDescription = "Ticket"; if (orderDescription === "") { orderDescription = "Item"; } orderDescription = "Ticket Number " + ticketNumber; paypal .Buttons({ style: { shape: "rect", color: "white", layout: "vertical", label: "buynow", }, createOrder: function (data, actions) { var selectedItemDescription = itemOptions.options[itemOptions.selectedIndex].value; var selectedItemPrice = parseFloat( itemOptions.options[itemOptions.selectedIndex].getAttribute("price")); var tax = 0 === 0 || false ? 0 : selectedItemPrice * (parseFloat(0) / 100); if (quantitySelect.options.length > 0) { quantity = parseInt( quantitySelect.options[quantitySelect.selectedIndex].value); } else { quantity = 1; } tax *= quantity; tax = Math.round(tax * 100) / 100; var priceTotal = quantity * selectedItemPrice + parseFloat(shipping) + tax; priceTotal = Math.round(priceTotal * 100) / 100; var itemTotalValue = Math.round(selectedItemPrice * quantity * 100) / 100; return actions.order.create({ purchase_units: [ { reference_id: ticketNumber, description: orderDescription, amount: { currency_code: "USD", value: priceTotal, breakdown: { item_total: { currency_code: "USD", value: itemTotalValue, }, shipping: { currency_code: "USD", value: shipping, }, tax_total: { currency_code: "USD", value: tax, }, }, }, items: [ { name: selectedItemDescription, unit_amount: { currency_code: "USD", value: selectedItemPrice, }, quantity: quantity, }, ], }, ], }); }, onApprove: function (data, actions) { return actions.order.capture().then(function (orderData) { console.log( "Capture result", orderData, JSON.stringify(orderData, null, 2)); const element = document.getElementById("paypal-button-container-' + str(col) + '"); element.innerHTML = ""; element.innerHTML = "<h3>Thank you for your payment!</h3>"; }); }, onError: function (err) { console.log(err); }, }) .render("#paypal-button-container-' + str(col) + '"); } /*initPayPalButton' + str(col) + '();*/'
        col += 1

        print(text)
