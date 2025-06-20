# gcloud parametermanager parameters versions update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update)*

**NAME**

: **gcloud parametermanager parameters versions update - updates the properties of a single Parameter Manager parameter version**

**SYNOPSIS**

: **`gcloud parametermanager parameters versions update` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#VERSION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#--location)`=`LOCATION` `[--parameter](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#--parameter)`=`PARAMETER`) [`[--[no-]disabled](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#--[no-]disabled)`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#--request-id)`=`REQUEST_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates the properties of a single parameter version, including status of the
parameter version (enabled/disabled).

**EXAMPLES**

: To update a parameter version `my-parameter-version` of parameter
`my-parameter` in location `global` run:

```
gcloud parametermanager parameters versions update my-parameter-version --parameter=my-parameter --location=global
```

**POSITIONAL ARGUMENTS**

: **Version resource - Identifier. [Output only] The resource name of the
ParameterVersion in the format
`projects/*/locations/*/parameters/*/versions/*`. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VERSION`**:
ID of the version or fully qualified identifier for the version.
To set the `version` attribute:

- provide the argument `version` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the version resource.
To set the `location` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--parameter**:
The parameter id of the version resource.
To set the `parameter` attribute:

- provide the argument `version` on the command line with a fully
specified name;
- provide the argument `--parameter` on the command line.**

**FLAGS**

: **--[no-]disabled**:
Disabled boolean to determine if a ParameterVersion acts as a metadata only
resource (payload is never returned if disabled is true). If true any calls will
always default to BASIC view even if the user explicitly passes FULL view as
part of the request. A render call on a disabled resource fails with an error.
Default value is False. Use `--disabled` to enable and
`--no-disabled` to disable.

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

: This command uses the `parametermanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/secret-manager/parameter-manager/docs/overview](https://cloud.google.com/secret-manager/parameter-manager/docs/overview)