# gcloud iam oauth-clients create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create)*

**NAME**

: **gcloud iam oauth-clients create - create an OAuth client**

**SYNOPSIS**

: **`gcloud iam oauth-clients create` (`[OAUTH_CLIENT](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#OAUTH_CLIENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--location)`=`LOCATION`) `[--allowed-grant-types](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--allowed-grant-types)`=[`ALLOWED_GRANT_TYPES`,…] `[--allowed-redirect-uris](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--allowed-redirect-uris)`=[`ALLOWED_REDIRECT_URIS`,…] `[--allowed-scopes](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--allowed-scopes)`=[`ALLOWED_SCOPES`,…] `[--client-type](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--client-type)`=`CLIENT_TYPE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/oauth-clients/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new OAuth client.

**EXAMPLES**

: The following command creates a disabled OAuth client with ID
``my-oauth-client`` in the default project:

```
gcloud iam oauth-clients create my-oauth-client --location="global" --client-type="confidential-client" --display-name="My oauth client" --description="My oauth client description" --disabled --allowed-grant-types="authorization-code-grant,refresh-token-grant" --allowed-scopes="https://www.googleapis.com/auth/cloud-platform\
,openid" --allowed-redirect-uris="https://example.com"
```

**POSITIONAL ARGUMENTS**

: **Oauth client resource - The OAuth client to create. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `oauth_client` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OAUTH_CLIENT`**:
ID of the oauth client or fully qualified identifier for the oauth client.
To set the `oauth_client` attribute:

- provide the argument `oauth_client` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `oauth_client` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--allowed-grant-types**:
A list of OAuth grant types that are allowed for the OAuth client.
The following grant types are currently supported:

- `authorization-code-grant`

- `refresh-token-grant`

**--allowed-redirect-uris**:
A list of redirect uris that is allowed for redirecting when the authorization
is completed.

**--allowed-scopes**:
A list of scopes that the OAuth client is allowed to request during OAuth flows.
The following scopes are currently supported:

- `https://www.googleapis.com/auth/cloud-platform`: View, edit,
configure, and delete your Google Cloud data, and view the email address for
your Google Account.

- `openid`: Associate you with your personal info on Google Cloud.

- `email`: The OAuth client can read a federated identity's email
address.

- `groups`: The OAuth client can read a federated identity's groups.

**--client-type**:
The type of OAuth client. `CLIENT_TYPE` must be one of:
`confidential-client`, `public-client`.

**OPTIONAL FLAGS**

: **--description**:
A description of the OAuth client. Cannot exceed 256 characters.

**--disabled**:
Disables the OAuth client. You cannot use a disabled OAuth client for login.
Include `--no-disabled` to enable a disabled OAuth client.

**--display-name**:
A display name for the OAuth client. Cannot exceed 32 characters.

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
gcloud alpha iam oauth-clients create
```