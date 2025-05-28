# gcloud developer-connect connections update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update)*

**NAME**

: **gcloud developer-connect connections update - update the parameters of a single connection**

**SYNOPSIS**

: **`gcloud developer-connect connections update` `[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#CONNECTION)` [`[--[no-]allow-missing](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--[no-]allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--async)`] [`[--[no-]disabled](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--[no-]disabled)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--etag)`=`ETAG`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--location)`=`LOCATION`] [`[--namespace](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--namespace)`=`NAMESPACE`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--request-id)`=`REQUEST_ID`] [`[--secret](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--secret)`=`SECRET`] [`[--[no-]validate-only](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--[no-]validate-only)`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--annotations)`=[`ANNOTATIONS`,…]     | `[--update-annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--update-annotations)`=[`UPDATE_ANNOTATIONS`,…] `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-annotations)`     | `[--remove-annotations](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--remove-annotations)`=[__REMOVE_ANNOTATIONS,…]] [`[--bitbucket-cloud-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-cloud-config-authorizer-credential-user-token-secret-version)`=`BITBUCKET_CLOUD_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version)`=`BITBUCKET_CLOUD_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-cloud-config-workspace](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-cloud-config-workspace)`=`BITBUCKET_CLOUD_CONFIG_WORKSPACE` `[--clear-bitbucket-cloud-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-bitbucket-cloud-config)`     | `[--bitbucket-data-center-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-data-center-config-authorizer-credential-user-token-secret-version)`=`BITBUCKET_DATA_CENTER_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-data-center-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-data-center-config-host-uri)`=`BITBUCKET_DATA_CENTER_CONFIG_HOST_URI` `[--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version)`=`BITBUCKET_DATA_CENTER_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--bitbucket-data-center-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-data-center-config-service-directory)`=`BITBUCKET_DATA_CENTER_CONFIG_SERVICE_DIRECTORY` `[--bitbucket-data-center-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--bitbucket-data-center-config-ssl-ca-certificate)`=`BITBUCKET_DATA_CENTER_CONFIG_SSL_CA_CERTIFICATE` `[--clear-bitbucket-data-center-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-bitbucket-data-center-config)`     | `[--clear-github-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-github-config)` `[--github-config-app-installation-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-config-app-installation-id)`=`GITHUB_CONFIG_APP_INSTALLATION_ID` `[--github-config-authorizer-credential-oauth-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-config-authorizer-credential-oauth-token-secret-version)`=`GITHUB_CONFIG_AUTHORIZER_CREDENTIAL_OAUTH_TOKEN_SECRET_VERSION`     | `[--clear-github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-github-enterprise-config)` `[--github-enterprise-config-app-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-app-id)`=`GITHUB_ENTERPRISE_CONFIG_APP_ID` `[--github-enterprise-config-app-installation-id](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-app-installation-id)`=`GITHUB_ENTERPRISE_CONFIG_APP_INSTALLATION_ID` `[--github-enterprise-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-host-uri)`=`GITHUB_ENTERPRISE_CONFIG_HOST_URI` `[--github-enterprise-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-service-directory)`=`GITHUB_ENTERPRISE_CONFIG_SERVICE_DIRECTORY` `[--github-enterprise-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-ssl-ca-certificate)`=`GITHUB_ENTERPRISE_CONFIG_SSL_CA_CERTIFICATE` `[--clear-github-enterprise-config-private-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-github-enterprise-config-private-key-secret-version)`     | `[--github-enterprise-config-private-key-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-private-key-secret-version)`=`GITHUB_ENTERPRISE_CONFIG_PRIVATE_KEY_SECRET_VERSION` `[--clear-github-enterprise-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-github-enterprise-config-webhook-secret-version)`     | `[--github-enterprise-config-webhook-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--github-enterprise-config-webhook-secret-version)`=`GITHUB_ENTERPRISE_CONFIG_WEBHOOK_SECRET_VERSION`     | `[--clear-gitlab-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-gitlab-config)` `[--gitlab-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-config-authorizer-credential-user-token-secret-version)`=`GITLAB_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-config-read-authorizer-credential-user-token-secret-version)`=`GITLAB_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION`     | `[--clear-gitlab-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-gitlab-enterprise-config)` `[--gitlab-enterprise-config-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-enterprise-config-authorizer-credential-user-token-secret-version)`=`GITLAB_ENTERPRISE_CONFIG_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-enterprise-config-host-uri](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-enterprise-config-host-uri)`=`GITLAB_ENTERPRISE_CONFIG_HOST_URI` `[--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-enterprise-config-read-authorizer-credential-user-token-secret-version)`=`GITLAB_ENTERPRISE_CONFIG_READ_AUTHORIZER_CREDENTIAL_USER_TOKEN_SECRET_VERSION` `[--gitlab-enterprise-config-service-directory](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-enterprise-config-service-directory)`=`GITLAB_ENTERPRISE_CONFIG_SERVICE_DIRECTORY` `[--gitlab-enterprise-config-ssl-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--gitlab-enterprise-config-ssl-ca-certificate)`=`GITLAB_ENTERPRISE_CONFIG_SSL_CA_CERTIFICATE`] [`[--clear-crypto-key-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-crypto-key-config)` [`[--crypto-key-config-reference](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--crypto-key-config-reference)`=`CRYPTO_KEY_CONFIG_REFERENCE` : `[--key-ring](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--key-ring)`=`KEY_RING`]] [`[--clear-git-proxy-config](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-git-proxy-config)` `[--[no-]git-proxy-config-enabled](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--[no-]git-proxy-config-enabled)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--labels)`=[`LABELS`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--update-labels)`=[`UPDATE_LABELS`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#--remove-labels)`=[__REMOVE_LABELS,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/developer-connect/connections/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a connection.

**EXAMPLES**

: To update the labels of a connection `my-connection` in location
`us-central1` run:

```
gcloud developer-connect connections update my-connection --labels=key1=value1 --location=us-central1
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

: **--[no-]allow-missing**:
If set to true, and the connection is not found a new connection will be
created. In this situation `update_mask` is ignored. The creation
will succeed only if the input connection has all the necessary information (e.g
a github_config with both user_oauth_token and installation_id properties). Use
`--allow-missing` to enable and `--no-allow-missing` to
disable.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--[no-]disabled**:
If disabled is set to true, functionality is disabled for this connection.
Repository based API methods and webhooks processing for repositories in this
connection will be disabled. Use `--disabled` to enable and
`--no-disabled` to disable.

**--etag**:
This checksum is computed by the server based on the value of other fields, and
may be sent on update and delete requests to ensure the client has an up-to-date
value before proceeding.

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

**--[no-]validate-only**:
If set, validate the request, but do not actually post it. Use
`--validate-only` to enable and `--no-validate-only` to
disable.

**--annotations**

**Arguments for the connection config.
At most one of these can be specified:

**Configuration for connections to an instance of Bitbucket Cloud.

**Represents a personal access token that authorized the Connection, and
associated metadata.

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

**--bitbucket-cloud-config-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-cloud-config-authorizer-credential-user-token-secret-version`
on the command line.****

**Represents a personal access token that authorized the Connection, and
associated metadata.

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

**--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-cloud-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

**--bitbucket-cloud-config-workspace**:
The Bitbucket Cloud Workspace ID to be connected to Google Cloud Platform.

**--clear-bitbucket-cloud-config**:
Set connection.bitbucketCloudConfig back to default value.**

**Configuration for connections to an instance of Bitbucket Data Center.

**Represents a personal access token that authorized the Connection, and
associated metadata.

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

**--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version**:
ID of the secretVersion or fully qualified identifier for the secretVersion.
To set the `secret-version` attribute:

- provide the argument
`--bitbucket-data-center-config-read-authorizer-credential-user-token-secret-version`
on the command line.****

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

**--bitbucket-data-center-config-service-directory**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument
`--bitbucket-data-center-config-service-directory` on the command
line.****

**--bitbucket-data-center-config-ssl-ca-certificate**:
SSL certificate authority to trust when making requests to Bitbucket Data
Center.

**--clear-bitbucket-data-center-config**:
Set connection.bitbucketDataCenterConfig back to default value.**

**--clear-github-config**

**--clear-github-enterprise-config**

**--clear-gitlab-config**

**--clear-gitlab-enterprise-config****

**--clear-crypto-key-config**

**--clear-git-proxy-config**

**--labels**

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
gcloud alpha developer-connect connections update
```

```
gcloud beta developer-connect connections update
```