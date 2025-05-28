# gcloud iam workforce-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create)*

**NAME**

: **gcloud iam workforce-pools create - create a new workforce pool under an organization**

**SYNOPSIS**

: **`gcloud iam workforce-pools create` (`[WORKFORCE_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#WORKFORCE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--location)`=`LOCATION`) `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--organization)`=`ORGANIZATION` [`[--allowed-services](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--allowed-services)`=[`domain`=`DOMAIN`]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--description)`=`DESCRIPTION`] [`[--disable-programmatic-signin](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--disable-programmatic-signin)`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--display-name)`=`DISPLAY_NAME`] [`[--session-duration](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#--session-duration)`=`SESSION_DURATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a workforce pool under an organization given a valid organization ID.

**EXAMPLES**

: The following command creates a workforce pool with ID
`my-workforce-pool` in the organization
``12345``:

```
gcloud iam workforce-pools create my-workforce-pool --organization=12345
```

The following command creates a workforce pool with ID
`my-workforce-pool` with explicit values for all required and
optional parameters:

```
gcloud iam workforce-pools create my-workforce-pool --organization=12345 --location=global --display-name="My Workforce Pool" --description="My workforce pool
description." --session-duration="7200s" --disabled
```

**POSITIONAL ARGUMENTS**

: **Workforce pool resource - The workforce pool to create. The arguments in this
group can be used to specify the attributes of this resource.
This must be specified.

**`WORKFORCE_POOL`**:
ID of the workforce pool or fully qualified identifier for the workforce pool.
To set the `workforce_pool` attribute:

- provide the argument `workforce_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the workforce pool.
To set the `location` attribute:

- provide the argument `workforce_pool` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--organization**:
The parent organization of the workforce pool to create.

**OPTIONAL FLAGS**

: **--allowed-services**:
Services allowed for web sign-in with the workforce pool. The flag accepts
multiple values with the key as `domain` and value as the domain of
the service allowed for web sign-in. If not set, by default all the services are
allowed.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description for the workforce pool. Cannot exceed 256 characters in length.

**--disable-programmatic-signin**:
Disable programmatic sign-in for workforce pool users.

**--disabled**:
Whether or not the workforce pool is disabled.

**--display-name**:
A display name for the workforce pool. Cannot exceed 32 characters in length.

**--session-duration**:
How long the Google Cloud access tokens, console sign-in sessions, and gcloud
sign-in sessions from this workforce pool are valid. Must be greater than 15
minutes (900s) and less than 12 hours (43200s). If not configured, minted
credentials will have a default duration of one hour (3600s).

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
gcloud alpha iam workforce-pools create
```

```
gcloud beta iam workforce-pools create
```