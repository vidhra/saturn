# gcloud alpha api-gateway api-configs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe)*

**NAME**

: **gcloud alpha api-gateway api-configs describe - show details about a specific API config**

**SYNOPSIS**

: **`gcloud alpha api-gateway api-configs describe` (`[API_CONFIG](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe#API_CONFIG)` : `[--api](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe#--api)`=`API`) [`[--view](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe#--view)`=`VIEW`; default="BASIC"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway/api-configs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Show details about a specific API config.

**EXAMPLES**

: To show details about an API config, run:

```
gcloud alpha api-gateway api-configs describe my-config --api=my-api
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

**FLAGS**

: **--view**:
The API Configuration view to return. If 'FULL' is specified, the base64 encoded
API Configuration's source file conent will be included in the response.
`VIEW` must be one of: `BASIC`,
`FULL`.

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
gcloud api-gateway api-configs describe
```

```
gcloud beta api-gateway api-configs describe
```