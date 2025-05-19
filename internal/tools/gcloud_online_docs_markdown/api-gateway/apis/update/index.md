# gcloud api-gateway apis update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update)*

**NAME**

: **gcloud api-gateway apis update - update an API Gateway API**

**SYNOPSIS**

: **`gcloud api-gateway apis update` `[API](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#API)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an API Gateway API.
NOTE: Only the display name and labels attributes are mutable on an API.

**EXAMPLES**

: To update the display name of an API, run:

```
gcloud api-gateway apis update my-api --display-name="New Display Name"
```

NOTE: Only the display name and labels attributes are mutable on an API.

**POSITIONAL ARGUMENTS**

: **Api resource - Name for API which updated. This represents a Cloud resource.
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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

: These variants are also available:

```
gcloud alpha api-gateway apis update
```

```
gcloud beta api-gateway apis update
```