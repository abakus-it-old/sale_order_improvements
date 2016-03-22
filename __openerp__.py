{
    'name': "Sale order improvements",
    'version': '1.0',
    'depends': ['sale','account_reports_followup'],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'description': 
    """
    Sale order improvements.
        - It set the current date to the order date of quotations or sales orders.
        - Invoice Address is alterable after sale order confirmation.
        - New field special condition. Will be included at the end of the quotation report.
        - Attachment field in Quotations and Sale Orders
        - It creates a field 'header_html' that will be used with a WYSIWYG and printed on SO reports

	This module has been developed by Bernard DELHEZ @ AbAKUS it-solution under the control of Valentin THIRION.
    """,
    'data': ['view/report_saleorder.xml',
             'view/sale_order_view.xml',
             'security/ir.model.access.csv',
             ],
}
