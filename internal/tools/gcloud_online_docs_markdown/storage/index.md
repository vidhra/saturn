# gcloud storage  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage](https://cloud.google.com/sdk/gcloud/reference/storage)*

**NAME**

: **gcloud storage - create and manage Cloud Storage buckets and objects**

**SYNOPSIS**

: **`gcloud storage` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/storage#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/storage#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud storage command group lets you create and manage Cloud Storage
resources such as buckets and objects.
More information on Cloud Storage can be found here:
https://cloud.google.com/storage, and detailed documentation can be found here:
[https://cloud.google.com/storage/docs/](https://cloud.google.com/storage/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[batch-operations](https://cloud.google.com/sdk/gcloud/reference/storage/batch-operations)`**:
Manage Cloud Storage batch operations.

**`[buckets](https://cloud.google.com/sdk/gcloud/reference/storage/buckets)`**:
Manage Cloud Storage buckets.

**`[folders](https://cloud.google.com/sdk/gcloud/reference/storage/folders)`**:
Manage Cloud Storage folders.

**`[hmac](https://cloud.google.com/sdk/gcloud/reference/storage/hmac)`**:
Manage Cloud Storage service account HMAC keys.

**`[insights](https://cloud.google.com/sdk/gcloud/reference/storage/insights)`**:
Manage Cloud Storage inventory reports.

**`[managed-folders](https://cloud.google.com/sdk/gcloud/reference/storage/managed-folders)`**:
Manage Cloud Storage managed folders.

**`[objects](https://cloud.google.com/sdk/gcloud/reference/storage/objects)`**:
Manage Cloud Storage objects.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/storage/operations)`**:
Manage storage operations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cat](https://cloud.google.com/sdk/gcloud/reference/storage/cat)`**:
Outputs the contents of one or more URLs to stdout.

**`[cp](https://cloud.google.com/sdk/gcloud/reference/storage/cp)`**:
Upload, download, and copy Cloud Storage objects.

**`[du](https://cloud.google.com/sdk/gcloud/reference/storage/du)`**:
Displays the amount of space in bytes used by storage resources.

**`[hash](https://cloud.google.com/sdk/gcloud/reference/storage/hash)`**:
Calculates hashes on local or cloud files.

**`[ls](https://cloud.google.com/sdk/gcloud/reference/storage/ls)`**:
List Cloud Storage buckets and objects.

**`[mv](https://cloud.google.com/sdk/gcloud/reference/storage/mv)`**:
Moves or renames objects.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/storage/restore)`**:
Restore one or more soft-deleted objects.

**`[rm](https://cloud.google.com/sdk/gcloud/reference/storage/rm)`**:
Delete objects and buckets.

**`[rsync](https://cloud.google.com/sdk/gcloud/reference/storage/rsync)`**:
Synchronize content of two buckets/directories.

**`[service-agent](https://cloud.google.com/sdk/gcloud/reference/storage/service-agent)`**:
Manage a project's Cloud Storage service agent, which is used to perform Cloud
KMS operations.

**`[sign-url](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url)`**:
Generate a URL with embedded authentication that can be used by anyone.

**NOTES**

: This variant is also available:

```
gcloud alpha storage
```