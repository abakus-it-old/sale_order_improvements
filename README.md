#Sale order improvements
* It set the current date to the order date of quotations or sales orders.
* Invoice Address is alterable after sale order confirmation
* New field special condition. Will be included at the end of the quotation report.
* Attachment field in Quotations and Sale Orders
* It creates a field 'header_html' that will be used with a WYSIWYG and printed on SO reports
* It sets the 'note' fields to html (usable with a WYSIWYG)

!!! You need to add &quot;&lt;t t-if=&quot;o.special_condition_id&quot;&gt;&lt;span t-field=&quot;o.special_condition_id.name&quot;/&gt;&lt;/t&gt;&quot; at the end of the quotation report (sale.report_saleorder_document) !!!

This module has been developed by Bernard DELHEZ @ AbAKUS it-solution.
