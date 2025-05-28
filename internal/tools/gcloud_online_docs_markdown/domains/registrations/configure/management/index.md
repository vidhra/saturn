# gcloud domains registrations configure management  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management)*

**NAME**

: **gcloud domains registrations configure management - configure management settings of a Cloud Domains registration**

**SYNOPSIS**

: **`gcloud domains registrations configure management` `[REGISTRATION](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management#REGISTRATION)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management#--async)`] [`[--preferred-renewal-method](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management#--preferred-renewal-method)`=`PREFERRED_RENEWAL_METHOD`] [`[--transfer-lock-state](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management#--transfer-lock-state)`=`TRANSFER_LOCK_STATE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Configure management settings of a registration. This includes settings related
to transfers, billing and renewals of a registration.

**EXAMPLES**

: To start an interactive flow to configure management settings for
``example.com``, run:

```
gcloud domains registrations configure management example.com
```

To unlock a transfer lock of a registration for
``example.com``, run:

```
gcloud domains registrations configure management example.com --transfer-lock-state=unlocked
```

To disable automatic renewals for
``example.com``, run:

```
gcloud domains registrations configure management example.com --preferred-renewal-method=renewal-disabled
```

**POSITIONAL ARGUMENTS**

: **Registration resource - The domain registration to configure management settings
for. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `registration` on the command line with a fully
specified name;
- location is always global.

This must be specified.

**`REGISTRATION`**:
ID of the registration or fully qualified identifier for the registration.
To set the `registration` attribute:

- provide the argument `registration` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--preferred-renewal-method**:
Preferred Renewal Method of a registration. It defines how the registration
should be renewed. The actual Renewal Method can be set to renewal-disabled in
case of e.g. problems with the Billing Account or reporeted domain abuse.
`PREFERRED_RENEWAL_METHOD` must be one of:

**`automatic-renewal`**:
The domain is automatically renewed each year.

**`renewal-disabled`**:
The domain won't be renewed and will expire at its expiration time.

**--transfer-lock-state**:
Transfer Lock of a registration. It needs to be unlocked in order to transfer
the domain to another registrar. `TRANSFER_LOCK_STATE`
must be one of:

**`locked`**:
The transfer lock is locked.

**`unlocked`**:
The transfer lock is unlocked.

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
gcloud alpha domains registrations configure management
```

```
gcloud beta domains registrations configure management
```