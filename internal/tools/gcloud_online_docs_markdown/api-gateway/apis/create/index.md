# gcloud api-gateway apis create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create)*

**NAME**

: **gcloud api-gateway apis create - create a new API**

**SYNOPSIS**

: **`gcloud api-gateway apis create` `[API](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#API)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--managed-service](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#--managed-service)`=`MANAGED_SERVICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new API.

**EXAMPLES**

: To create an API, run:

```
gcloud api-gateway apis create my-api
```

**POSITIONAL ARGUMENTS**

: **Api resource - Name for API which created. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `api` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `api` on the command line with a fully specified
name;
- Location for API and API Configs. Defaults to global.

This must be specified.

**`API`**:
ID of the api or fully qualified identifier for the api.
To set the `api` attribute:

- provide the argument `api` on the command line.**

**FLAGS**

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

**--managed-service**:
The name of a pre-existing Google Managed Service.

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
gcloud alpha api-gateway apis create
```

```
gcloud beta api-gateway apis create
```