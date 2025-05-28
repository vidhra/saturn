# gcloud parametermanager parameters versions render  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render)*

**NAME**

: **gcloud parametermanager parameters versions render - gets a single Parameter Manager parameter version render**

**SYNOPSIS**

: **`gcloud parametermanager parameters versions render` (`[VERSION](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render#VERSION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render#--location)`=`LOCATION` `[--parameter](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render#--parameter)`=`PARAMETER`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/parametermanager/parameters/versions/render#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gets a single parameter version render resource.

**EXAMPLES**

: To get a single parameter version render `my-parameter-version` of a
parameter `my-parameter` in location `global` run:

```
gcloud parametermanager parameters versions render my-parameter-version --parameter=my-parameter --location=global
```

**POSITIONAL ARGUMENTS**

: **Version resource - Name of the resource The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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