# gcloud parametermanager parameters versions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe)*

**NAME**

: **gcloud parametermanager parameters versions describe - gets a single Parameter Manager parameter version**

**SYNOPSIS**

: **`gcloud parametermanager parameters versions describe` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe#VERSION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe#--location)`=`LOCATION` `[--parameter](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe#--parameter)`=`PARAMETER`) [`[--view](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe#--view)`=`VIEW`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gets a single parameter version, along with payload supplied by the user at the
time of creation. If the payload contains any references to secrets, these will
not be rendered in the output.

**EXAMPLES**

: To get a single parameter version `my-parameter-version` of parameter
`my-parameter` in location `global` run:

```
gcloud parametermanager parameters versions describe my-parameter-version --parameter=my-parameter --location=global
```

**POSITIONAL ARGUMENTS**

: **Version resource - Name of the resource in the format
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

: **--view**:
View of the ParameterVersion. In the default FULL view, all metadata &
payload associated with the ParameterVersion will be returned.
`VIEW` must be one of:

**`basic`**:
Include only the metadata for the resource.

**`full`**:
Include metadata & other relevant payload data as well. This is the default
view.

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