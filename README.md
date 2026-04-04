# Point of Service: Coffee Shop Kiosk

This program implements a POS (point of service) type of app for a coffee shop
kiosk. This application will provide two interfaces: admin and kiosk. Both of
which the user can interact with, by switching to the desired mode.

The coffee shop kiosk will allow the user to register a local database of
products (orented to a coffee business). With this, it'll allow the tracking
of sales and stock management.

Additional to the local database, the user will be able to generate sales
reports and logs receipts from sales.

## Design

### Point of Service App

The application starts as the POS app, and then this app will allow the user
to select a mode. There is only administrator and kiosk mode. The user must
select a mode, before continuing to utilize the program.

After selecting the kiosk mode, to go back to the mode selector, the user must
input ` ADMIN ` instead of a regular option. This will prompt for an admin
pass key. If the pass key is valid, the mode selector will show.

![Point of Service app](docs/pos_app_flow.svg)

### Administrator App

In the administrator mode, there is four principle activities the user may
choose. Product management, product category management, pricing options
management, and sales report generation.

Each of these options provides the facility to the user to manipulate its
business database. And view the business cash flow with tthe sales reports.

![Administrator App](docs/administrator_app_flow.svg)

### Kiosk App

In the kiosk mode, the user has three different options, all oriented to
making a purchase. Browse product menu, add item, and shopping cart.

The shopping cart option will show an interface to realize payments, to which
only cash and card are available. Card payment is simulated, by assuming only
tapping the card to pay is possible.

![Kiosk App](docs/kiosk_app_flow.svg)

## Usage

To run the program, the ` uv ` tool is required to run the code. Make sure,
you have ` uv ` installed in your machine.

```python
uv run python3 main.py
```
