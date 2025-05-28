# gcloud sql users set-password-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy)*

**NAME**

: **gcloud sql users set-password-policy - replaces a user's password policy in a given instance**

**SYNOPSIS**

: **`gcloud sql users set-password-policy` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#USERNAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--instance)`=`INSTANCE`, `[-i](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#-i)` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--async)`] [`[--clear-password-policy](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--clear-password-policy)`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--host)`=`HOST`] [`[--password-policy-allowed-failed-attempts](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--password-policy-allowed-failed-attempts)`=`PASSWORD_POLICY_ALLOWED_FAILED_ATTEMPTS`] [`[--[no-]password-policy-enable-failed-attempts-check](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--[no-]password-policy-enable-failed-attempts-check)`] [`[--[no-]password-policy-enable-password-verification](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--[no-]password-policy-enable-password-verification)`] [`[--password-policy-password-expiration-duration](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#--password-policy-password-expiration-duration)`=`PASSWORD_POLICY_PASSWORD_EXPIRATION_DURATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/users/set-password-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Replaces a user's password policy in a given instance with a specified username
and host.

**EXAMPLES**

: To replace the password policy with 2 minutes password expiration time for
``my-user`` in instance
``prod-instance``, run:

```
gcloud sql users set-password-policy my-user --instance=prod-instance --password-policy-password-expiration-duration=2m
```

To clear the existing password policy of
``my-user`` in instance
``prod-instance``, run:

```
gcloud sql users set-password-policy my-user --instance=prod-instance --clear-password-policy
```

**POSITIONAL ARGUMENTS**

: **`USERNAME`**:
Cloud SQL username.

**REQUIRED FLAGS**

: **--instance**:
Cloud SQL instance ID.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--clear-password-policy**:
Clear the existing password policy. This flag is only available for Postgres.

**--host**:
Cloud SQL user's hostname expressed as a specific IP address or address range.
`%` denotes an unrestricted hostname. Applicable flag for MySQL
instances; ignored for all other engines. Note, if you connect to your instance
using IP addresses, you must add your client IP address as an authorized
address, even if your hostname is unrestricted. For more information, see [Configure IP](https://cloud.google.com/sql/docs/mysql/configure-ip).

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
gcloud alpha sql users set-password-policy
```

```
gcloud beta sql users set-password-policy
```