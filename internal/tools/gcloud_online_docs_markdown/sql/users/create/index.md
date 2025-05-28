# gcloud sql users create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/users/create](https://cloud.google.com/sdk/gcloud/reference/sql/users/create)*

**NAME**

: **gcloud sql users create - creates a user in a given instance**

**SYNOPSIS**

: **`gcloud sql users create` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#USERNAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--async)`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--host)`=`HOST`] [`[--password](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--password)`=`PASSWORD`] [`[--password-policy-allowed-failed-attempts](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--password-policy-allowed-failed-attempts)`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`] [`[--[no-]password-policy-enable-failed-attempts-check](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--[no-]password-policy-enable-failed-attempts-check)`] [`[--[no-]password-policy-enable-password-verification](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--[no-]password-policy-enable-password-verification)`] [`[--password-policy-password-expiration-duration](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--password-policy-password-expiration-duration)`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#--type)`=`TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/users/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a user in a given instance with specified username, host, type, and
password.

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

**--password**:
Cloud SQL user's password.

**--password-policy-allowed-failed-attempts**:
Number of failed login attempts allowed before a user is locked out.

**--[no-]password-policy-enable-failed-attempts-check**:
Enables the failed login attempts check if set to true. Use
`--password-policy-enable-failed-attempts-check` to enable and
`--no-password-policy-enable-failed-attempts-check` to disable.

**--[no-]password-policy-enable-password-verification**:
The current password must be specified when altering the password. Use
`--password-policy-enable-password-verification` to enable and
`--no-password-policy-enable-password-verification` to disable.

**--password-policy-password-expiration-duration**:
Expiration duration after a password is updated, for example, 2d for 2 days. See
`[gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)` for information on duration formats.

**--type**:
Cloud SQL user's type. It determines the method to authenticate the user during
login. See the list of user types at [https://cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/SqlUserType](https://cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/SqlUserType)

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
gcloud alpha sql users create
```

```
gcloud beta sql users create
```