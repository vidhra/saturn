# verifiedpermissionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# verifiedpermissions

## Description

Amazon Verified Permissions is a permissions management service from Amazon Web Services. You can use Verified Permissions to manage permissions for your application, and authorize user access based on those permissions. Using Verified Permissions, application developers can grant access based on information about the users, resources, and requested actions. You can also evaluate additional information like group membership, attributes of the resources, and session context, such as time of request and IP addresses. Verified Permissions manages these permissions by letting you create and store authorization policies for your applications, such as consumer-facing web sites and enterprise business systems.

Verified Permissions uses Cedar as the policy language to express your permission requirements. Cedar supports both role-based access control (RBAC) and attribute-based access control (ABAC) authorization models.

For more information about configuring, administering, and using Amazon Verified Permissions in your applications, see the [Amazon Verified Permissions User Guide](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/) .

For more information about the Cedar policy language, see the [Cedar Policy Language Guide](https://docs.cedarpolicy.com/) .

### Warning

When you write Cedar policies that reference principals, resources and actions, you can define the unique identifiers used for each of those elements. We strongly recommend that you follow these best practices:

- **Use values like universally unique identifiers (UUIDs) for all principal and resource identifiers.**   For example, if user `jane` leaves the company, and you later let someone else use the name `jane` , then that new user automatically gets access to everything granted by policies that still reference `User::"jane"` . Cedar canât distinguish between the new user and the old. This applies to both principal and resource identifiers. Always use identifiers that are guaranteed unique and never reused to ensure that you donât unintentionally grant access because of the presence of an old identifier in a policy. Where you use a UUID for an entity, we recommend that you follow it with the // comment specifier and the âfriendlyâ name of your entity. This helps to make your policies easier to understand. For example: principal == User::âa1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111â, // alice
- **Do not include personally identifying, confidential, or sensitive information as part of the unique identifier for your principals or resources.** These identifiers are included in log entries shared in CloudTrail trails.

Several operations return structures that appear similar, but have different purposes. As new functionality is added to the product, the structure used in a parameter of one operation might need to change in a way that wouldnât make sense for the same parameter in a different operation. To help you understand the purpose of each, the following naming convention is used for the structures:

- Parameter type structures that end in `Detail` are used in `Get` operations.
- Parameter type structures that end in `Item` are used in `List` operations.
- Parameter type structures that use neither suffix are used in the mutating (create and update) operations.

## Available Commands

- [batch-get-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/batch-get-policy.html)
- [batch-is-authorized](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/batch-is-authorized.html)
- [batch-is-authorized-with-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/batch-is-authorized-with-token.html)
- [create-identity-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-identity-source.html)
- [create-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy.html)
- [create-policy-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy-store.html)
- [create-policy-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy-template.html)
- [delete-identity-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-identity-source.html)
- [delete-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy.html)
- [delete-policy-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy-store.html)
- [delete-policy-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy-template.html)
- [get-identity-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-identity-source.html)
- [get-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy.html)
- [get-policy-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy-store.html)
- [get-policy-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy-template.html)
- [get-schema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-schema.html)
- [is-authorized](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/is-authorized.html)
- [is-authorized-with-token](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/is-authorized-with-token.html)
- [list-identity-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-identity-sources.html)
- [list-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policies.html)
- [list-policy-stores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policy-stores.html)
- [list-policy-templates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policy-templates.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-tags-for-resource.html)
- [put-schema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/put-schema.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/untag-resource.html)
- [update-identity-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-identity-source.html)
- [update-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy.html)
- [update-policy-store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy-store.html)
- [update-policy-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy-template.html)