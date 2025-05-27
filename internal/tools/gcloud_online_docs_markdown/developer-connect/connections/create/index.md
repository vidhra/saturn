# gcloud developer-connect connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create)*

**NAME**

: **gcloud developer-connect connections create - create a connection resource**

**SYNOPSIS**

: **`gcloud developer-connect connections create` `[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#CONNECTION)` [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--annotations)`=[`ANNOTATIONS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--async)`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--disabled)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--etag)`=`ETAG`] [`[--git-proxy-config-enabled](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--git-proxy-config-enabled)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--labels)`=[`LABELS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--location)`=`LOCATION`] [`[--namespace](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--namespace)`=`NAMESPACE`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--request-id)`=`REQUEST_ID`] [`[--secret](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--secret)`=`SECRET`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--validate-only)`] [`[--bitbucket-cloud-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-cloud-config-authorizer-credential-user-token-secret-version)`=`BITBUCKET_CLOUD_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version)`=`BITBUCKET_CLOUD_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-cloud-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-cloud-config-webhook-secret-version)`=`BITBUCKET_CLOUD_CONFIG_WEBHOOK_SECRET_VERSION` `[--bitbucket-cloud-config-workspace](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-cloud-config-workspace)`=`BITBUCKET_CLOUD_CONFIG_WORKSPACE`     | [`[--bitbucket-data-center-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-authorizer-credential-user-token-secret-version)`=`BITBUCKET_DATA_CENTER_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-data-center-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-host-uri)`=`BITBUCKET_DATA_CENTER_CONFIG_HOST_URI` `[--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version)`=`BITBUCKET_DATA_CENTER_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-data-center-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-webhook-secret-version)`=`BITBUCKET_DATA_CENTER_CONFIG_WEBHOOK_SECRET_VERSION` : `[--bitbucket-data-center-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-service-directory)`=`BITBUCKET_DATA_CENTER_CONFIG_SERVICE_DIRECTORY` `[--bitbucket-data-center-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--bitbucket-data-center-config-ssl-ca-certificate)`=`BITBUCKET_DATA_CENTER_CONFIG_SSL_CA_CERTIFICATE`]     | [`[--github-config-app](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-config-app)`=`GITHUB_CONFIG_APP` : `[--github-config-app-installation-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-config-app-installation-id)`=`GITHUB_CONFIG_APP_INSTALLATION_ID` `[--github-config-authorizer-credential-oauth-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-config-authorizer-credential-oauth-token-secret-version)`=`GITHUB_CONFIG_AUTHORIZER_CREDENTIAL_OAUTH_TOKEN_SECRET_VERSION`]     | [`[--github-enterprise-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-host-uri)`=`GITHUB_ENTERPRISE_CONFIG_HOST_URI` : `[--github-enterprise-config-app-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-app-id)`=`GITHUB_ENTERPRISE_CONFIG_APP_ID` `[--github-enterprise-config-app-installation-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-app-installation-id)`=`GITHUB_ENTERPRISE_CONFIG_APP_INSTALLATION_ID` `[--github-enterprise-config-private-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-private-key-secret-version)`=`GITHUB_ENTERPRISE_CONFIG_PRIVATE_KEY_SECRET_VERSION` `[--github-enterprise-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-service-directory)`=`GITHUB_ENTERPRISE_CONFIG_SERVICE_DIRECTORY` `[--github-enterprise-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-ssl-ca-certificate)`=`GITHUB_ENTERPRISE_CONFIG_SSL_CA_CERTIFICATE` `[--github-enterprise-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--github-enterprise-config-webhook-secret-version)`=`GITHUB_ENTERPRISE_CONFIG_WEBHOOK_SECRET_VERSION`]     | `[--gitlab-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-config-authorizer-credential-user-token-secret-version)`=`GITLAB_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-config-read-authorizer-credential-user-token-secret-version)`=`GITLAB_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-config-webhook-secret-version)`=`GITLAB_CONFIG_WEBHOOK_SECRET_VERSION`     | [`[--gitlab-enterprise-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-authorizer-credential-user-token-secret-version)`=`GITLAB_ENTERPRISE_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-enterprise-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-host-uri)`=`GITLAB_ENTERPRISE_CONFIG_HOST_URI` `[--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version)`=`GITLAB_ENTERPRISE_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-enterprise-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-webhook-secret-version)`=`GITLAB_ENTERPRISE_CONFIG_WEBHOOK_SECRET_VERSION` : `[--gitlab-enterprise-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-service-directory)`=`GITLAB_ENTERPRISE_CONFIG_SERVICE_DIRECTORY` `[--gitlab-enterprise-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--gitlab-enterprise-config-ssl-ca-certificate)`=`GITLAB_ENTERPRISE_CONFIG_SSL_CA_CERTIFICATE`]] [(`[--crypto-key-config-reference](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--crypto-key-config-reference)`=`CRYPTO_KEY_CONFIG_REFERENCE` : `[--key-ring](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#--key-ring)`=`KEY_RING`)] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a connection resource.

**EXAMPLES**

: To create a GitHub connection named `my-connection` in
`us-central1` run:

```
gcloud developer-connect connections create my-connection --github-config-app=developer-connect --github-config-authorizer-credential-oauth-token-secret-version=projects/my-project/secrets/my-oauth-token/versions/1 --github-config-app-installation-id=12345 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Identifier. The resource name of the connection, in the
format
`projects/{project}/locations/{location}/connections/{connection_id}`.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`CONNECTION`**:
ID of the connection or fully qualified identifier for the connection.
To set the `connection` attribute:

- provide the argument `connection` on the command line.**

**FLAGS**

: **--annotations**:
Allows clients to store small amounts of arbitrary data.

**`KEY`**:
Sets `KEY` value.

**`VALUE`**:
Sets `VALUE` value.

`Shorthand Example:`

```
--annotations=string=string
```

`JSON Example:`

```
--annotations='{"string": "string"}'
```

`File Example:`

```
--annotations=path_to_file.(yaml|json)
```

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--disabled**:
If disabled is set to true, functionality is disabled for this connection.
Repository based API methods and webhooks processing for repositories in this
connection will be disabled.

**--etag**:
This checksum is computed by the server based on the value of other fields, and
may be sent on update and delete requests to ensure the client has an up-to-date
value before proceeding.

**--git-proxy-config-enabled**

**--labels**:
Labels as key value pairs.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--location**:
For resources [connection, cryptoKey, service], provides fallback value for
resource location attribute. When the resource's full URI path is not provided,
location will fallback to this flag value.

**--namespace**:
For resources [service], provides fallback value for resource namespace
attribute. When the resource's full URI path is not provided, namespace will
fallback to this flag value.

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--secret**:
For resources [secretVersion], provides fallback value for resource secret
attribute. When the resource's full URI path is not provided, secret will
fallback to this flag value.

**--validate-only**:
If set, validate the request, but do not actually post it.

**Arguments for the connection config.
At most one of these can be specified:

**Configuration for connections to an instance of Bitbucket Cloud.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-cloud-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-cloud-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-cloud-config-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-cloud-config-authorizer-credential-user-token-secret-version`
on the command line.****

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

**SecretVersion resource - SecretManager resource containing the webhook secret
used to verify webhook events, formatted as
`projects/*/secrets/*/versions/*`. This is used to validate and
create webhooks. This represents a Cloud resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-cloud-config-webhook-secret-version` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-cloud-config-webhook-secret-version` on the command line
with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-cloud-config-webhook-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-cloud-config-webhook-secret-version` on the command
line.**

**--bitbucket-cloud-config-workspace**:
The Bitbucket Cloud Workspace ID to be connected to Google Cloud Platform.**

**Configuration for connections to an instance of Bitbucket Data Center.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-data-center-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-data-center-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-data-center-config-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-data-center-config-authorizer-credential-user-token-secret-version`
on the command line.****

**--bitbucket-data-center-config-host-uri**:
The URI of the Bitbucket Data Center host this connection is for.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

**SecretVersion resource - SecretManager resource containing the webhook secret
used to verify webhook events, formatted as
`projects/*/secrets/*/versions/*`. This is used to validate webhooks.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-data-center-config-webhook-secret-version` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--bitbucket-data-center-config-webhook-secret-version` on the
command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--bitbucket-data-center-config-webhook-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-data-center-config-webhook-secret-version` on the
command line.**

**ServiceDirectoryConfig represents Service Directory configuration for a
connection.

**Service resource - The Service Directory service name. Format:
projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument
`--bitbucket-data-center-config-service-directory` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument
`--bitbucket-data-center-config-service-directory` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.

To set the `namespace` attribute:

- provide the argument
`--bitbucket-data-center-config-service-directory` on the command
line with a fully specified name;
- provide the argument `--namespace` on the command line.

This must be specified.

**--bitbucket-data-center-config-service-directory**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument
`--bitbucket-data-center-config-service-directory` on the command
line.****

**--bitbucket-data-center-config-ssl-ca-certificate**:
SSL certificate authority to trust when making requests to Bitbucket Data
Center.**

**--github-config-app**

**--github-enterprise-config-host-uri**

**Configuration for connections to gitlab.com.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--gitlab-config-authorizer-credential-user-token-secret-version` on
the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--gitlab-config-authorizer-credential-user-token-secret-version` on
the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-config-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--gitlab-config-authorizer-credential-user-token-secret-version` on
the command line.****

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--gitlab-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--gitlab-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--gitlab-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

**SecretVersion resource - SecretManager resource containing the webhook secret of
a GitLab project, formatted as `projects/*/secrets/*/versions/*`.
This is used to validate webhooks. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--gitlab-config-webhook-secret-version` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument `--gitlab-config-webhook-secret-version` on the
command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-config-webhook-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument `--gitlab-config-webhook-secret-version` on the
command line.****

**Configuration for connections to an instance of GitLab Enterprise.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--gitlab-enterprise-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--gitlab-enterprise-config-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-enterprise-config-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--gitlab-enterprise-config-authorizer-credential-user-token-secret-version`
on the command line.****

**--gitlab-enterprise-config-host-uri**:
The URI of the GitLab Enterprise host this connection is for.

**Represents a personal access token that authorized the Connection, and
associated metadata.
This must be specified.

**SecretVersion resource - A SecretManager resource containing the user token that
authorizes the Developer Connect connection. Format:
`projects/*/secrets/*/versions/*`. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument
`--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version`
on the command line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

**SecretVersion resource - SecretManager resource containing the webhook secret of
a GitLab project, formatted as `projects/*/secrets/*/versions/*`.
This is used to validate webhooks. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument
`--gitlab-enterprise-config-webhook-secret-version` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `secret` attribute:

- provide the argument
`--gitlab-enterprise-config-webhook-secret-version` on the command
line with a fully specified name;
- provide the argument `--secret` on the command line.

This must be specified.

**--gitlab-enterprise-config-webhook-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--gitlab-enterprise-config-webhook-secret-version` on the command
line.**

**ServiceDirectoryConfig represents Service Directory configuration for a
connection.

**Service resource - The Service Directory service name. Format:
projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--gitlab-enterprise-config-service-directory`
on the command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--gitlab-enterprise-config-service-directory`
on the command line with a fully specified name;
- provide the argument `--location` on the command line.

To set the `namespace` attribute:

- provide the argument `--gitlab-enterprise-config-service-directory`
on the command line with a fully specified name;
- provide the argument `--namespace` on the command line.

This must be specified.

**--gitlab-enterprise-config-service-directory**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `--gitlab-enterprise-config-service-directory`
on the command line.****

**--gitlab-enterprise-config-ssl-ca-certificate**:
SSL Certificate Authority certificate to use for requests to GitLab Enterprise
instance.****

**The crypto key configuration. This field is used by the Customer-managed
encryption keys (CMEK) feature.

**CryptoKey resource - The name of the key which is used to encrypt/decrypt
customer data. For key in Cloud KMS, the key should be in the format of
`projects/*/locations/*/keyRings/*/cryptoKeys/*`. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--crypto-key-config-reference` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--crypto-key-config-reference` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--crypto-key-config-reference**:
ID of the cryptoKey or fully qualified identifier for the cryptoKey.
To set the `crypto-key` attribute:

- provide the argument `--crypto-key-config-reference` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--key-ring**:
The keyRing id of the cryptoKey resource.
To set the `key-ring` attribute:

- provide the argument `--crypto-key-config-reference` on the command
line with a fully specified name;
- provide the argument `--key-ring` on the command line.****

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

: This command uses the `developerconnect/v1` API. The full
documentation for this API can be found at: [http://cloud.google.com/developer-connect/docs/overview](http://cloud.google.com/developer-connect/docs/overview)

**NOTES**

: These variants are also available:

```
gcloud alpha developer-connect connections create
```

```
gcloud beta developer-connect connections create
```