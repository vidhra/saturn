# gcloud sql users describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/users/describe](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe)*

**NAME**

: **gcloud sql users describe - retrieves information about a Cloud SQL user in a given instance**

**SYNOPSIS**

: **`gcloud sql users describe` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#USERNAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#INSTANCE)` [`[--host](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#--host)`=`HOST`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/users/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieves information about a Cloud SQL user in a given instance.

**EXAMPLES**

: To fetch a user with name 'my-user' and optional host '%' in instance
'my-instance', run:

```
gcloud sql users describe my-user --host=% --instance=my-instance
```

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
Cloud SQL username.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--host**:
Cloud SQL user's hostname expressed as a specific IP address or address range.
`%` denotes an unrestricted hostname. Applicable flag for MySQL
instances; ignored for all other engines. Note, if you connect to your instance
using IP addresses, you must add your client IP address as an authorized
address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip).

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
gcloud alpha sql users describe
```

```
gcloud beta sql users describe
```