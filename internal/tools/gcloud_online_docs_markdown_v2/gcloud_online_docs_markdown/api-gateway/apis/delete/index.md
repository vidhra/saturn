# gcloud api-gateway apis delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/delete](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/delete)*

**NAME**

: **gcloud api-gateway apis delete - deletes an API**

**SYNOPSIS**

: **`gcloud api-gateway apis delete` `[API](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/delete#API)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/api-gateway/apis/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes an API.
NOTE: All API configs belonging to the API will need to be deleted before the
API can be deleted.

**EXAMPLES**

: To delete an API 'my-api', run:

```
gcloud api-gateway apis delete my-api
```

NOTE: All API configs belonging to the API will need to be deleted before the
API can be deleted.

**POSITIONAL ARGUMENTS**

: **Api resource - Name for API which will be deleted. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
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
gcloud alpha api-gateway apis delete
```

```
gcloud beta api-gateway apis delete
```