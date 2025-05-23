# acm-pcaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# acm-pca

## Description

This is the *Amazon Web Services Private Certificate Authority API Reference* . It provides descriptions, syntax, and usage examples for each of the actions and data types involved in creating and managing a private certificate authority (CA) for your organization.

The documentation for each action shows the API request parameters and the JSON response. Alternatively, you can use one of the Amazon Web Services SDKs to access an API that is tailored to the programming language or platform that you prefer. For more information, see [Amazon Web Services SDKs](https://aws.amazon.com/tools/#SDKs) .

Each Amazon Web Services Private CA API operation has a quota that determines the number of times the operation can be called per second. Amazon Web Services Private CA throttles API requests at different rates depending on the operation. Throttling means that Amazon Web Services Private CA rejects an otherwise valid request because the request exceeds the operationâs quota for the number of requests per second. When a request is throttled, Amazon Web Services Private CA returns a [ThrottlingException](https://docs.aws.amazon.com/privateca/latest/APIReference/CommonErrors.html) error. Amazon Web Services Private CA does not guarantee a minimum request rate for APIs.

To see an up-to-date list of your Amazon Web Services Private CA quotas, or to request a quota increase, log into your Amazon Web Services account and visit the [Service Quotas](https://console.aws.amazon.com/servicequotas/) console.

## Available Commands

- [create-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html)
- [create-certificate-authority-audit-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority-audit-report.html)
- [create-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-permission.html)
- [delete-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html)
- [delete-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-permission.html)
- [delete-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-policy.html)
- [describe-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html)
- [describe-certificate-authority-audit-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority-audit-report.html)
- [get-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html)
- [get-certificate-authority-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-certificate.html)
- [get-certificate-authority-csr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-csr.html)
- [get-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-policy.html)
- [import-certificate-authority-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html)
- [issue-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html)
- [list-certificate-authorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html)
- [list-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-permissions.html)
- [list-tags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-tags.html)
- [put-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/put-policy.html)
- [restore-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/restore-certificate-authority.html)
- [revoke-certificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/revoke-certificate.html)
- [tag-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html)
- [untag-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html)
- [update-certificate-authority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html)
- [wait](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/wait/index.html)