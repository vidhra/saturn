# appflowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# appflow

## Description

Welcome to the Amazon AppFlow API reference. This guide is for developers who need detailed information about the Amazon AppFlow API operations, data types, and errors.

Amazon AppFlow is a fully managed integration service that enables you to securely transfer data between software as a service (SaaS) applications like Salesforce, Marketo, Slack, and ServiceNow, and Amazon Web Services like Amazon S3 and Amazon Redshift.

Use the following links to get started on the Amazon AppFlow API:

- [Actions](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Operations.html) : An alphabetical list of all Amazon AppFlow API operations.
- [Data types](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Types.html) : An alphabetical list of all Amazon AppFlow data types.
- [Common parameters](https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonParameters.html) : Parameters that all Query operations can use.
- [Common errors](https://docs.aws.amazon.com/appflow/1.0/APIReference/CommonErrors.html) : Client and server errors that all operations can return.

If youâre new to Amazon AppFlow, we recommend that you review the [Amazon AppFlow User Guide](https://docs.aws.amazon.com/appflow/latest/userguide/what-is-appflow.html) .

Amazon AppFlow API users can use vendor-specific mechanisms for OAuth, and include applicable OAuth attributes (such as `auth-code` and `redirecturi` ) with the connector-specific `ConnectorProfileProperties` when creating a new connector profile using Amazon AppFlow API operations. For example, Salesforce users can refer to the ` *Authorize Apps with OAuth* [https://help.salesforce.com/articleView?id=remoteaccess_authenticate](https://help.salesforce.com/articleView?id=remoteaccess_authenticate).htm`__ documentation.

## Available Commands

- [cancel-flow-executions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/cancel-flow-executions.html)
- [create-connector-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html)
- [create-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-flow.html)
- [delete-connector-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/delete-connector-profile.html)
- [delete-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/delete-flow.html)
- [describe-connector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector.html)
- [describe-connector-entity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-entity.html)
- [describe-connector-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html)
- [describe-connectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connectors.html)
- [describe-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-flow.html)
- [describe-flow-execution-records](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-flow-execution-records.html)
- [list-connector-entities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-connector-entities.html)
- [list-connectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-connectors.html)
- [list-flows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-flows.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-tags-for-resource.html)
- [register-connector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/register-connector.html)
- [reset-connector-metadata-cache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/reset-connector-metadata-cache.html)
- [start-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/start-flow.html)
- [stop-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/stop-flow.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/tag-resource.html)
- [unregister-connector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/unregister-connector.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/untag-resource.html)
- [update-connector-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-connector-profile.html)
- [update-connector-registration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-connector-registration.html)
- [update-flow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/update-flow.html)