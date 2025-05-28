# gcloud iam service-accounts  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts)*

**NAME**

: **gcloud iam service-accounts - create and manipulate service accounts**

**SYNOPSIS**

: **`gcloud iam service-accounts` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create and manipulate IAM service accounts. A service account is a special
Google account that belongs to your application or a VM, instead of to an
individual end user. Your application uses the service account to call the
Google API of a service, so that the users aren't directly involved.
Note: Service accounts use client quotas for tracking usage.
More information on service accounts can be found at: [https://cloud.google.com/iam/docs/service-accounts](https://cloud.google.com/iam/docs/service-accounts)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[keys](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys)`**:
Manage service account keys.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding)`**:
Add an IAM policy binding to an IAM service account.

**`[create](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create)`**:
Create a service account for a project.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/delete)`**:
Delete a service account from a project.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe)`**:
Show metadata for a service account from a project.

**`[disable](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/disable)`**:
Disable an IAM service account.

**`[enable](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/enable)`**:
Enable an IAM service account.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy)`**:
Get the IAM policy for a service account.

**`[list](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)`**:
List all of a project's service accounts.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/remove-iam-policy-binding)`**:
Remove IAM policy binding from a service account.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy)`**:
Set IAM policy for a service account.

**`[sign-blob](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-blob)`**:
Sign a blob with a managed service account key.

**`[sign-jwt](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-jwt)`**:
Sign a JWT with a managed service account key.

**`[undelete](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/undelete)`**:
Undelete a service account for a project.

**`[update](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update)`**:
Update an IAM service account.

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts
```

```
gcloud beta iam service-accounts
```