# invoicingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# invoicing

## Description

**Amazon Web Services Invoice Configuration**

You can use Amazon Web Services Invoice Configuration APIs to programmatically create, update, delete, get, and list invoice units. You can also programmatically fetch the information of the invoice receiver. For example, business legal name, address, and invoicing contacts.

You can use Amazon Web Services Invoice Configuration to receive separate Amazon Web Services invoices based your organizational needs. By using Amazon Web Services Invoice Configuration, you can configure invoice units that are groups of Amazon Web Services accounts that represent your business entities, and receive separate invoices for each business entity. You can also assign a unique member or payer account as the invoice receiver for each invoice unit. As you create new accounts within your Organizations using Amazon Web Services Invoice Configuration APIs, you can automate the creation of new invoice units and subsequently automate the addition of new accounts to your invoice units.

Service endpoint

You can use the following endpoints for Amazon Web Services Invoice Configuration:

- `https://invoicing.us-east-1.api.aws`

## Available Commands

- [batch-get-invoice-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/batch-get-invoice-profile.html)
- [create-invoice-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/create-invoice-unit.html)
- [delete-invoice-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/delete-invoice-unit.html)
- [get-invoice-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/get-invoice-unit.html)
- [list-invoice-units](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/list-invoice-units.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/list-tags-for-resource.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/untag-resource.html)
- [update-invoice-unit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/invoicing/update-invoice-unit.html)