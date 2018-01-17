# -*- coding: utf-8 -*-
# copyright reserved

{
    "name": "API Quality control",
    "version": "8.0",
    "category": "Quality control",
    'sequence': 1014,
   # 'author': '',
    #'website': 'http://abc.com',
    'description': '''
	   Every entry comming from Manufacture Order and Purchase Shipment is under Quality check
	   select Quantity to quality check
	   select Quantity to Reject to MO and PO
	''',
    "depends": [
        	"product","mrp","stock","purchase",
   		 ],
    "data": [
    	"security/quality_control_security.xml",
    	"security/ir.model.access.csv",
        "data/quality_control_data.xml",
        "data/stock_data.xml",
        "views/quality_view.xml",
        "wizard/test_wizard_view.xml",
        "views/quality_inspection_view.xml",
        "views/quality_test_view.xml",
        "views/dashboard_view.xml",
        "views/mrp_view.xml",
        'views/stock_view.xml',
        'res_config_view.xml',
    ],
    "demo": [
        "demo/quality_control_demo.xml",
    ],
    'test': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}


