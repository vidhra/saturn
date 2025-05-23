# supportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# support

## Description

The *Amazon Web Services Support API Reference* is intended for programmers who need detailed information about the Amazon Web Services Support operations and data types. You can use the API to manage your support cases programmatically. The Amazon Web Services Support API uses HTTP methods that return results in JSON format.

### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API.
- If you call the Amazon Web Services Support API from an account that doesnât have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [Amazon Web Services Support](http://aws.amazon.com/premiumsupport/) .

You can also use the Amazon Web Services Support API to access features for [Trusted Advisor](http://aws.amazon.com/premiumsupport/trustedadvisor/) . You can return a list of checks and their descriptions, get check results, specify checks to refresh, and get the refresh status of checks.

You can manage your support cases with the following Amazon Web Services Support API operations:

- The  CreateCase ,  DescribeCases ,  DescribeAttachment , and  ResolveCase operations create Amazon Web Services Support cases, retrieve information about cases, and resolve cases.
- The  DescribeCommunications ,  AddCommunicationToCase , and  AddAttachmentsToSet operations retrieve and add communications and attachments to Amazon Web Services Support cases.
- The  DescribeServices and  DescribeSeverityLevels operations return Amazon Web Service names, service codes, service categories, and problem severity levels. You use these values when you call the  CreateCase operation.

You can also use the Amazon Web Services Support API to call the Trusted Advisor operations. For more information, see [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) in the *Amazon Web Services Support User Guide* .

For authentication of requests, Amazon Web Services Support uses [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

For more information about this service and the endpoints to use, see [About the Amazon Web Services Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html) in the *Amazon Web Services Support User Guide* .

## Available Commands

- [add-attachments-to-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-attachments-to-set.html)
- [add-communication-to-case](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-communication-to-case.html)
- [create-case](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/create-case.html)
- [describe-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-attachment.html)
- [describe-cases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html)
- [describe-communications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-communications.html)
- [describe-create-case-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-create-case-options.html)
- [describe-services](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-services.html)
- [describe-severity-levels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-severity-levels.html)
- [describe-supported-languages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-supported-languages.html)
- [describe-trusted-advisor-check-refresh-statuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-refresh-statuses.html)
- [describe-trusted-advisor-check-result](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html)
- [describe-trusted-advisor-check-summaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-summaries.html)
- [describe-trusted-advisor-checks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-checks.html)
- [refresh-trusted-advisor-check](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html)
- [resolve-case](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/resolve-case.html)