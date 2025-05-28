# gcloud iam oauth-clients credentials delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete)*

**NAME**

: **gcloud iam oauth-clients credentials delete - delete an OAuth client credential**

**SYNOPSIS**

: **`gcloud iam oauth-clients credentials delete` (`[CREDENTIAL](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete#CREDENTIAL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete#--location)`=`LOCATION` `[--oauth-client](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete#--oauth-client)`=`OAUTH_CLIENT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/credentials/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an OAuth client credential.

**EXAMPLES**

: To delete the OAuth client credential with ID
``my-oauth-client-credential`` in the default
project, run:

```
gcloud iam oauth-clients credentials delete my-oauth-client-credential --location="global" --oauth-client="my-oauth-client"
```

**POSITIONAL ARGUMENTS**

: **Oauth client credential resource - The OAuth client credential to delete. The
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
gcloud alpha iam oauth-clients credentials delete
```