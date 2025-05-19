# gcloud auth activate-service-account  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)*

**NAME**

: **gcloud auth activate-service-account - authorize access to Google Cloud with a service account**

**SYNOPSIS**

: **`gcloud auth activate-service-account` [`[ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account#ACCOUNT)`] `[--key-file](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account#--key-file)`=`KEY_FILE` [`[--password-file](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account#--password-file)`=`PASSWORD_FILE`     | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account#--prompt-for-password)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To allow `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` (and other
tools in Google Cloud CLI) to use service account credentials to make requests,
use this command to import these credentials from a file that contains a private
authorization key, and activate them for use in `[gcloud](https://cloud.google.com/sdk/gcloud/reference)`. gcloud auth
activate-service-account serves the same function as `[gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login)` but uses a
service account rather than Google user credentials.
For more information on authorization and credential types, see: [https://cloud.google.com/sdk/docs/authorizing](https://cloud.google.com/sdk/docs/authorizing).
`Key File`
To obtain the key file for this command, use either the [Google Cloud Console](https://console.cloud.google.com) or `gcloud
iam service-accounts keys create`. The key file can be .json (preferred)
or .p12 (legacy) format. In the case of legacy .p12 files, a separate password
might be required and is displayed in the Console when you create the key.
`Credentials`
Credentials will also be activated (similar to running `gcloud config set
account [ACCOUNT_NAME]`).
If a project is specified using the `--project` flag, the project is
set in active configuration, which is the same as running `gcloud config
set project [PROJECT_NAME]`. Any previously active credentials, will be
retained (though no longer default) and can be displayed by running `[gcloud auth list](https://cloud.google.com/sdk/gcloud/reference/auth/list)`.
If you want to delete previous credentials, see `[gcloud auth revoke](https://cloud.google.com/sdk/gcloud/reference/auth/revoke)`.
`Note:` Service accounts use client quotas for tracking
usage.

**EXAMPLES**

: To authorize `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` to access
Google Cloud using an existing service account while also specifying a project,
run:

```
gcloud auth activate-service-account SERVICE_ACCOUNT@DOMAIN.COM --key-file=/path/key.json --project=PROJECT_ID
```

**POSITIONAL ARGUMENTS**

: **[`ACCOUNT`]**:
E-mail address of the service account.

**REQUIRED FLAGS**

: **--key-file**:
Path to the private key file.

**OPTIONAL FLAGS**

: **--password-file**

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
gcloud alpha auth activate-service-account
```

```
gcloud beta auth activate-service-account
```