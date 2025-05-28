# gcloud iam  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam](https://cloud.google.com/sdk/gcloud/reference/iam)*

**NAME**

: **gcloud iam - manage IAM service accounts and keys**

**SYNOPSIS**

: **`gcloud iam` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/iam#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/iam#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud iam command group lets you manage Google Cloud Identity & Access
Management (IAM) service accounts and keys.
Cloud IAM authorizes who can take action on specific resources, giving you full
control and visibility to manage cloud resources centrally. For established
enterprises with complex organizational structures, hundreds of workgroups and
potentially many more projects, Cloud IAM provides a unified view into security
policy across your entire organization, with built-in auditing to ease
compliance processes.
More information on Cloud IAM can be found here: [https://cloud.google.com/iam](https://cloud.google.com/iam) and
detailed documentation can be found here: [https://cloud.google.com/iam/docs/](https://cloud.google.com/iam/docs/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[oauth-clients](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients)`**:
Create and manage OAuth clients.

**`[policies](https://cloud.google.com/sdk/gcloud/reference/iam/policies)`**:
Manage IAM deny policies.

**`[policy-bindings](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings)`**:
Manage policy bindings.

**`[principal-access-boundary-policies](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies)`**:
Manage principal access boundary policies.

**`[roles](https://cloud.google.com/sdk/gcloud/reference/iam/roles)`**:
Create and manipulate roles.

**`[service-accounts](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts)`**:
Create and manipulate service accounts.

**`[simulator](https://cloud.google.com/sdk/gcloud/reference/iam/simulator)`**:
Understand how an IAM policy change could impact access before deploying the
change.

**`[workforce-pools](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools)`**:
Create and manage workforce pools.

**`[workload-identity-pools](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools)`**:
Manage IAM workload identity pools.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list-grantable-roles](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles)`**:
List IAM grantable roles for a resource.

**`[list-testable-permissions](https://cloud.google.com/sdk/gcloud/reference/iam/list-testable-permissions)`**:
List IAM testable permissions for a resource.

**NOTES**

: These variants are also available:

```
gcloud alpha iam
```

```
gcloud beta iam
```