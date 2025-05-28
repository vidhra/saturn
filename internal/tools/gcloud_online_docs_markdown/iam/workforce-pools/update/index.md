# gcloud iam workforce-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update)*

**NAME**

: **gcloud iam workforce-pools update - update a workforce pool**

**SYNOPSIS**

: **`gcloud iam workforce-pools update` (`[WORKFORCE_POOL](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#WORKFORCE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--description)`=`DESCRIPTION`] [`[--disable-programmatic-signin](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--disable-programmatic-signin)`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--display-name)`=`DISPLAY_NAME`] [`[--session-duration](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--session-duration)`=`SESSION_DURATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a workforce pool.

**EXAMPLES**

: The following command updates a workforce pool with ID
``my-workforce-pool`` with explicit values for
all required and optional parameters:

```
gcloud iam workforce-pools update my-workforce-pool --location=global --display-name="My Workforce Pool" --description="My workforce pool description." --session-duration="7200s" --disabled
```

**POSITIONAL ARGUMENTS**

: **Workforce pool resource - The workforce pool to update. The arguments in this
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description for the workforce pool. Cannot exceed 256 characters in length.

**--disable-programmatic-signin**:
Disables the programmatic sign-in for workforce pool users. Specify
`--no-disable-security-token-exchange` to enable programmatic
sign-in. For more information, refer to Obtain short-lived tokens for workforce
identity federation at [https://cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials](https://cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials)

**--disabled**:
Disables the workforce pool. You cannot use a disabled workforce pool to perform
new token exchanges or sign-ins using any provider in the workforce pool.
Specify `--no-disabled` to enable a disabled pool.

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

**API REFERENCE**

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

```
gcloud alpha iam workforce-pools update
```

```
gcloud beta iam workforce-pools update
```