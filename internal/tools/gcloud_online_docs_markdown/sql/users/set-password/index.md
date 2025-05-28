# gcloud sql users set-password  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password)*

**NAME**

: **gcloud sql users set-password - changes a user's password in a given instance**

**SYNOPSIS**

: **`gcloud sql users set-password` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#USERNAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--async)`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--host)`=`HOST`] [`[--discard-dual-password](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--discard-dual-password)`     | `[--retain-password](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--retain-password)`] [`[--password](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--password)`=`PASSWORD`     | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#--prompt-for-password)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Changes a user's password in a given instance with specified username and host.

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
Cloud SQL username.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--host**:
Cloud SQL user's hostname expressed as a specific IP address or address range.
`%` denotes an unrestricted hostname. Applicable flag for MySQL
instances; ignored for all other engines. Note, if you connect to your instance
using IP addresses, you must add your client IP address as an authorized
address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip).

**--discard-dual-password**

**--password**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha sql users set-password
```

```
gcloud beta sql users set-password
```