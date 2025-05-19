# gcloud alpha api-gateway api-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create)*

**NAME**

: **gcloud alpha api-gateway api-configs create - add a new config to an API**

**SYNOPSIS**

: **`gcloud alpha api-gateway api-configs create` (`[API_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#API_CONFIG)` : `[--api](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--api)`=`API`) (`[--grpc-files](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--grpc-files)`=[`FILE`,…]     | `[--openapi-spec](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--openapi-spec)`=[`FILE`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--async)`] [`[--backend-auth-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--backend-auth-service-account)`=`BACKEND_AUTH_SERVICE_ACCOUNT`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Add a new config to an API.
NOTE: If the specified API does not exist it will be created.

**EXAMPLES**

: To create an API config for the API 'my-api' with an OpenAPI spec, run:

```
gcloud alpha api-gateway api-configs create my-config --api=my-api --openapi-spec=path/to/openapi_spec.yaml
```

**POSITIONAL ARGUMENTS**

: **Api config resource - Name for API Config which will be created. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `api_config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `api_config` on the command line with a fully
specified name;
- Location for API and API Configs. Defaults to global.

This must be specified.

**`API_CONFIG`**:
ID of the api-config or fully qualified identifier for the api-config.
To set the `api-config` attribute:

- provide the argument `api_config` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--api**:
API ID.
To set the `api` attribute:

- provide the argument `api_config` on the command line with a fully
specified name;
- provide the argument `--api` on the command line.**

**REQUIRED FLAGS**

: **--grpc-files**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backend-auth-service-account**:
Service account which will be used to sign tokens for backends with
authentication configured.

**--display-name**:
Human readable name which can optionally be supplied.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud api-gateway api-configs create
```

```
gcloud beta api-gateway api-configs create
```