# gcloud alpha api-gateway gateways update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update)*

**NAME**

: **gcloud alpha api-gateway gateways update - update an API Gateway**

**SYNOPSIS**

: **`gcloud alpha api-gateway gateways update` (`[GATEWAY](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#GATEWAY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--api-config](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--api-config)`=`API_CONFIG` : `[--api](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--api)`=`API`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/gateways/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an API Gateway.

**EXAMPLES**

: To update the display name of a gateway, run:

```
gcloud alpha api-gateway gateways update my-gateway --location=us-central1 --display-name="New Display Name"
```

**POSITIONAL ARGUMENTS**

: **Gateway resource - Name for gateway which will be updated. The arguments in this
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
Human readable name which can optionally be supplied.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Api config resource - Resource name for API config the gateway will use. The
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

**--clear-labels**

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
gcloud api-gateway gateways update
```

```
gcloud beta api-gateway gateways update
```