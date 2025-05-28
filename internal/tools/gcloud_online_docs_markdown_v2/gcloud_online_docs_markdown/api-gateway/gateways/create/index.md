# gcloud api-gateway gateways create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create)*

**NAME**

: **gcloud api-gateway gateways create - create a new gateway**

**SYNOPSIS**

: **`gcloud api-gateway gateways create` (`[GATEWAY](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#GATEWAY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--location)`=`LOCATION`) (`[--api-config](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--api-config)`=`API_CONFIG` : `[--api](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--api)`=`API`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/api-gateway/gateways/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new gateway.

**EXAMPLES**

: To create a gateway in 'us-central1' run:

```
gcloud api-gateway gateways create my-gateway --api=my-api --api-config=my-config --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Gateway resource - Name for gateway which will be created. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `gateway` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GATEWAY`**:
ID of the gateway or fully qualified identifier for the gateway.
To set the `gateway` attribute:

- provide the argument `gateway` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Cloud location for gateway.
To set the `location` attribute:

- provide the argument `gateway` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **Api config resource - Resource name for API config the gateway will use. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--api-config` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--api-config` on the command line with a fully
specified name;
- Location for API and API Configs. Defaults to global.

This must be specified.

**--api-config**:
ID of the api-config or fully qualified identifier for the api-config.
To set the `api-config` attribute:

- provide the argument `--api-config` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--api**:
API ID.
To set the `api` attribute:

- provide the argument `--api-config` on the command line with a fully
specified name;
- provide the argument `--api` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: These variants are also available:

```
gcloud alpha api-gateway gateways create
```

```
gcloud beta api-gateway gateways create
```