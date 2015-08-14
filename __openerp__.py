{
    'name': "Sale order improvements",
    'version': '1.0',
    'depends': ['sale',],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': 
    """
    Sale order improvements.
    - It set the current date to the order date of quotations or sales orders.
    - Invoice Address is alterable after sale order confirmation.
    - New field special condition. Will be included at the end of the quotation report.
    
    !!! You need to add "<t t-if="o.special_condition_id"><span t-field="o.special_condition_id.name"/></t>" at the end of the quotation report (sale.report_saleorder_document) !!!
    """,
    'data': [#'view/report_saleorder.xml',
             'view/sale_order_view.xml',
             'security/ir.model.access.csv',
             ],
}
