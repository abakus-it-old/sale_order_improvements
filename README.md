#Sale order improvements
* It set the current date to the order date of quotations or sales orders.
* Invoice Address is alterable after sale order confirmation
* New field special condition. Will be included at the end of the quotation report.

!!! You need to add "<t t-if="o.special_condition_id"><span t-field="o.special_condition_id.name"/></t>" at the end of the quotation report (sale.report_saleorder_document) !!!

This module has been developed by Bernard DELHEZ @ AbAKUS it-solution.
