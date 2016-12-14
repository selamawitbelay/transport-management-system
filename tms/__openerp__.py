# -*- coding: utf-8 -*-
# Copyright 2012, Israel Cruz Argil, Argil Consulting
# Copyright 2016, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Freight Management",
    "version": "9.0.0.1.0",
    "category": "Transport",
    "author": "Argil Consulting, Jarsa Sistemas",
    "website": "http://www.argil.mx, https://www.jarsa.com.mx",
    "depends": [
        "account_accountant",
        "fleet",
        "hr",
        "purchase",
        "sale",
        "base_geoengine",
        "account_operating_unit",
    ],
    'external_dependencies': {
        'python': [
            'sodapy',
            'num2words',
        ],
    },
    "summary": "Management System for Carriers, Trucking and other companies",
    "license": "AGPL-3",
    "data": [
        'security/ir.model.access.csv',
        'views/tms_view.xml',
        'data/account_journal_data.xml',
        'views/operating_unit_view.xml',
        'views/fleet_vehicle_odometer_view.xml',
        'views/hr_employee_view.xml',
        'views/fleet_vehicle_view.xml',
        'views/fleet_vehicle_log_fuel_view.xml',
        'views/product_template_view.xml',
        'views/tms_advance_view.xml',
        'views/tms_config_settings_view.xml',
        'views/tms_event_view.xml',
        'views/tms_expense_view.xml',
        'views/tms_expense_line_view.xml',
        'views/tms_factor_view.xml',
        'views/tms_place_view.xml',
        'views/tms_route_view.xml',
        'views/tms_transportable_view.xml',
        'views/tms_travel_view.xml',
        'views/tms_unit_kit_view.xml',
        'views/tms_waybill_view.xml',
        'views/tms_waybill_extradata_view.xml',
        'views/account_invoice_view.xml',
        'views/tms_route_tollstation_view.xml',
        'views/fleet_vehicle_engine_view.xml',
        'views/tms_factor_special_view.xml',
        'views/tms_route_note_view.xml',
        'data/product_product_data.xml',
        'data/ir_sequence_data.xml',
        'data/tms_base_data.xml',
        'wizards/tms_advance_payment_view.xml',
        'wizards/tms_waybill_invoice_view.xml',
        'wizards/tms_fuelvoucher_invoice_view.xml',
        'wizards/tms_expense_payment_view.xml',
        'report/waybill_report.xml',
    ],
    "demo": [
        'demo/fleet_vehicle_engine.xml',
        'demo/fleet_vehicle.xml',
        'demo/hr_employee.xml',
        'demo/tms_place.xml',
        'demo/tms_route.xml',
        'demo/tms_travel.xml',
        'demo/tms_advance.xml',
        'demo/tms_route_fuelefficiency.xml',
        'demo/tms_transportable.xml',
        'demo/tms_travel.xml',
        'demo/tms_unit_kit.xml',
    ],
    "application": True,
    "installable": True,
}
