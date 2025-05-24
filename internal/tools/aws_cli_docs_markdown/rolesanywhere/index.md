# rolesanywhereÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# rolesanywhere

## Description

Identity and Access Management Roles Anywhere provides a secure way for your workloads such as servers, containers, and applications that run outside of Amazon Web Services to obtain temporary Amazon Web Services credentials. Your workloads can use the same IAM policies and roles you have for native Amazon Web Services applications to access Amazon Web Services resources. Using IAM Roles Anywhere eliminates the need to manage long-term credentials for workloads running outside of Amazon Web Services.

To use IAM Roles Anywhere, your workloads must use X.509 certificates issued by their certificate authority (CA). You register the CA with IAM Roles Anywhere as a trust anchor to establish trust between your public key infrastructure (PKI) and IAM Roles Anywhere. If you donât manage your own PKI system, you can use Private Certificate Authority to create a CA and then use that to establish trust with IAM Roles Anywhere.

This guide describes the IAM Roles Anywhere operations that you can call programmatically. For more information about IAM Roles Anywhere, see the [IAM Roles Anywhere User Guide](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) .

## Available Commands

- [create-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/create-profile.html)
- [create-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/create-trust-anchor.html)
- [delete-attribute-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/delete-attribute-mapping.html)
- [delete-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/delete-crl.html)
- [delete-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/delete-profile.html)
- [delete-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/delete-trust-anchor.html)
- [disable-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/disable-crl.html)
- [disable-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/disable-profile.html)
- [disable-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/disable-trust-anchor.html)
- [enable-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/enable-crl.html)
- [enable-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/enable-profile.html)
- [enable-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/enable-trust-anchor.html)
- [get-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/get-crl.html)
- [get-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/get-profile.html)
- [get-subject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/get-subject.html)
- [get-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/get-trust-anchor.html)
- [import-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/import-crl.html)
- [list-crls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-crls.html)
- [list-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-profiles.html)
- [list-subjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-subjects.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-tags-for-resource.html)
- [list-trust-anchors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/list-trust-anchors.html)
- [put-attribute-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/put-attribute-mapping.html)
- [put-notification-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/put-notification-settings.html)
- [reset-notification-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/reset-notification-settings.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/untag-resource.html)
- [update-crl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/update-crl.html)
- [update-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/update-profile.html)
- [update-trust-anchor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rolesanywhere/update-trust-anchor.html)