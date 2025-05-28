# gcloud iam oauth-clients credentials create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create)*

**NAME**

: **gcloud iam oauth-clients credentials create - create an OAuth client credential**

**SYNOPSIS**

: **`gcloud iam oauth-clients credentials create` (`[CREDENTIAL](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#CREDENTIAL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#--location)`=`LOCATION` `[--oauth-client](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#--oauth-client)`=`OAUTH_CLIENT`) [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new OAuth client credential.

**EXAMPLES**

: To create a disabled OAuth client credential with ID
``my-oauth-client-credential`` in the default
project, run:

```
gcloud iam oauth-clients credentials create my-oauth-client-credential --location="global" --oauth-client="my-oauth-client" --display-name="My OAuth client credential" --disabled
```

**POSITIONAL ARGUMENTS**

: **Oauth client credential resource - The OAuth client credential to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `credential` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CREDENTIAL`**:
ID of the oauth client credential or fully qualified identifier for the oauth
client credential.
To set the `credential` attribute:

- provide the argument `credential` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `credential` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--oauth-client**:
ID to use for the OAuth client, which becomes the final component of the
resource name. This value should be 4-32 characters, and may contain the
characters [a-z0-9-]. The prefix `gcp-` is reserved for use by
Google, and may not be specified.
To set the `oauth-client` attribute:

- provide the argument `credential` on the command line with a fully
specified name;
- provide the argument `--oauth-client` on the command line.**

**FLAGS**

: **--disabled**:
Disables the OAuth client credential. You cannot use a disabled OAuth client
credential for OAuth. Include `--no-disabled` to enable a disabled
OAuth client credential.

**--display-name**:
A display name for the OAuth client credential. Cannot exceed 32 characters.

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

: This variant is also available:

```
gcloud alpha iam oauth-clients credentials create
```