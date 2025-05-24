# securityhubÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# securityhub

## Description

Security Hub provides you with a comprehensive view of your security state in Amazon Web Services and helps you assess your Amazon Web Services environment against security industry standards and best practices.

Security Hub collects security data across Amazon Web Services accounts, Amazon Web Services services, and supported third-party products and helps you analyze your security trends and identify the highest priority security issues.

To help you manage the security state of your organization, Security Hub supports multiple security standards. These include the Amazon Web Services Foundational Security Best Practices (FSBP) standard developed by Amazon Web Services, and external compliance frameworks such as the Center for Internet Security (CIS), the Payment Card Industry Data Security Standard (PCI DSS), and the National Institute of Standards and Technology (NIST). Each standard includes several security controls, each of which represents a security best practice. Security Hub runs checks against security controls and generates control findings to help you assess your compliance against security best practices.

In addition to generating control findings, Security Hub also receives findings from other Amazon Web Services services, such as Amazon GuardDuty and Amazon Inspector, and supported third-party products. This gives you a single pane of glass into a variety of security-related issues. You can also send Security Hub findings to other Amazon Web Services services and supported third-party products.

Security Hub offers automation features that help you triage and remediate security issues. For example, you can use automation rules to automatically update critical findings when a security check fails. You can also leverage the integration with Amazon EventBridge to trigger automatic responses to specific findings.

This guide, the *Security Hub API Reference* , provides information about the Security Hub API. This includes supported resources, HTTP methods, parameters, and schemas. If youâre new to Security Hub, you might find it helpful to also review the ` *Security Hub User Guide* [https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub).html`__ . The user guide explains key concepts and provides procedures that demonstrate how to use Security Hub features. It also provides information about topics such as integrating Security Hub with other Amazon Web Services services.

In addition to interacting with Security Hub by making calls to the Security Hub API, you can use a current version of an Amazon Web Services command line tool or SDK. Amazon Web Services provides tools and SDKs that consist of libraries and sample code for various languages and platforms, such as PowerShell, Java, Go, Python, C++, and .NET. These tools and SDKs provide convenient, programmatic access to Security Hub and other Amazon Web Services services . They also handle tasks such as signing requests, managing errors, and retrying requests automatically. For information about installing and using the Amazon Web Services tools and SDKs, see [Tools to Build on Amazon Web Services](http://aws.amazon.com/developer/tools/) .

With the exception of operations that are related to central configuration, Security Hub API requests are executed only in the Amazon Web Services Region that is currently active or in the specific Amazon Web Services Region that you specify in your request. Any configuration or settings change that results from the operation is applied only to that Region. To make the same change in other Regions, call the same API operation in each Region in which you want to apply the change. When you use central configuration, API requests for enabling Security Hub, standards, and controls are executed in the home Region and all linked Regions. For a list of central configuration operations, see the [Central configuration terms and concepts](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html#central-configuration-concepts) section of the *Security Hub User Guide* .

The following throttling limits apply to Security Hub API operations.

- `BatchEnableStandards` - `RateLimit` of 1 request per second. `BurstLimit` of 1 request per second.
- `GetFindings` - `RateLimit` of 3 requests per second. `BurstLimit` of 6 requests per second.
- `BatchImportFindings` - `RateLimit` of 10 requests per second. `BurstLimit` of 30 requests per second.
- `BatchUpdateFindings` - `RateLimit` of 10 requests per second. `BurstLimit` of 30 requests per second.
- `UpdateStandardsControl` - `RateLimit` of 1 request per second. `BurstLimit` of 5 requests per second.
- All other operations - `RateLimit` of 10 requests per second. `BurstLimit` of 30 requests per second.

## Available Commands

- [accept-administrator-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-administrator-invitation.html)
- [batch-delete-automation-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-delete-automation-rules.html)
- [batch-disable-standards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-disable-standards.html)
- [batch-enable-standards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-enable-standards.html)
- [batch-get-automation-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-automation-rules.html)
- [batch-get-configuration-policy-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-configuration-policy-associations.html)
- [batch-get-security-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-security-controls.html)
- [batch-get-standards-control-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-standards-control-associations.html)
- [batch-import-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-import-findings.html)
- [batch-update-automation-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-automation-rules.html)
- [batch-update-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-findings.html)
- [batch-update-standards-control-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-standards-control-associations.html)
- [create-action-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-action-target.html)
- [create-automation-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-automation-rule.html)
- [create-configuration-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-configuration-policy.html)
- [create-finding-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-finding-aggregator.html)
- [create-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-insight.html)
- [create-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-members.html)
- [decline-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/decline-invitations.html)
- [delete-action-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-action-target.html)
- [delete-configuration-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-configuration-policy.html)
- [delete-finding-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-finding-aggregator.html)
- [delete-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-insight.html)
- [delete-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-invitations.html)
- [delete-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-members.html)
- [describe-action-targets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-action-targets.html)
- [describe-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-hub.html)
- [describe-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-organization-configuration.html)
- [describe-products](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-products.html)
- [describe-standards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-standards.html)
- [describe-standards-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-standards-controls.html)
- [disable-import-findings-for-product](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-import-findings-for-product.html)
- [disable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-organization-admin-account.html)
- [disable-security-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-security-hub.html)
- [disassociate-from-administrator-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-from-administrator-account.html)
- [disassociate-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-members.html)
- [enable-import-findings-for-product](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-import-findings-for-product.html)
- [enable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-organization-admin-account.html)
- [enable-security-hub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-security-hub.html)
- [get-administrator-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-administrator-account.html)
- [get-configuration-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy.html)
- [get-configuration-policy-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy-association.html)
- [get-enabled-standards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-enabled-standards.html)
- [get-finding-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-finding-aggregator.html)
- [get-finding-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-finding-history.html)
- [get-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-findings.html)
- [get-insight-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insight-results.html)
- [get-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insights.html)
- [get-invitations-count](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-invitations-count.html)
- [get-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-members.html)
- [get-security-control-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-security-control-definition.html)
- [invite-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/invite-members.html)
- [list-automation-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-automation-rules.html)
- [list-configuration-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-configuration-policies.html)
- [list-configuration-policy-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-configuration-policy-associations.html)
- [list-enabled-products-for-import](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-enabled-products-for-import.html)
- [list-finding-aggregators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-finding-aggregators.html)
- [list-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-invitations.html)
- [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-members.html)
- [list-organization-admin-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-organization-admin-accounts.html)
- [list-security-control-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-security-control-definitions.html)
- [list-standards-control-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-standards-control-associations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-tags-for-resource.html)
- [start-configuration-policy-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/start-configuration-policy-association.html)
- [start-configuration-policy-disassociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/start-configuration-policy-disassociation.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/untag-resource.html)
- [update-action-target](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-action-target.html)
- [update-configuration-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-configuration-policy.html)
- [update-finding-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-finding-aggregator.html)
- [update-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-findings.html)
- [update-insight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-insight.html)
- [update-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-organization-configuration.html)
- [update-security-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-control.html)
- [update-security-hub-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-hub-configuration.html)
- [update-standards-control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-standards-control.html)