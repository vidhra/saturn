# marketplace-agreementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# marketplace-agreement

## Description

AWS Marketplace is a curated digital catalog that customers can use to find, buy, deploy, and manage third-party software, data, and services to build solutions and run their businesses. The AWS Marketplace Agreement Service provides an API interface that helps AWS Marketplace sellers manage their product-related agreements, including listing, searching, and filtering agreements.

To manage agreements in AWS Marketplace, you must ensure that your AWS Identity and Access Management (IAM) policies and roles are set up. The user must have the required policies/permissions that allow them to carry out the actions in AWS:

- `DescribeAgreement` â Grants permission to users to obtain detailed meta data about any of their agreements.
- `GetAgreementTerms` â Grants permission to users to obtain details about the terms of an agreement.
- `SearchAgreements` â Grants permission to users to search through all their agreements.

## Available Commands

- [describe-agreement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/describe-agreement.html)
- [get-agreement-terms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/get-agreement-terms.html)
- [search-agreements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-agreement/search-agreements.html)