# gcloud alpha access-approval requests  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests)*

**NAME**

: **gcloud alpha access-approval requests - manage Access Approval requests**

**SYNOPSIS**

: **`gcloud alpha access-approval requests` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Approval requests are created by Google personnel to
request approval from Access Approval customers prior to making administrative
accesses to their resources. Customers can act on these requests using the
commands in this command group.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[approve](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests/approve)`**:
`(ALPHA)` Approve an Access Approval request.

**`[dismiss](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests/dismiss)`**:
`(ALPHA)` Dismiss an Access Approval request.

**`[get](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests/get)`**:
`(ALPHA)` Get an Access Approval request.

**`[invalidate](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests/invalidate)`**:
`(ALPHA)` Invalidate an Access Approval request.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval/requests/list)`**:
`(ALPHA)` List Access Approval requests.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-approval requests
```

```
gcloud beta access-approval requests
```