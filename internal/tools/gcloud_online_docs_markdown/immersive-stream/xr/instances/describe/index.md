# gcloud immersive-stream xr instances describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/describe](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/describe)*

**NAME**

: **gcloud immersive-stream xr instances describe - describe a specific Immersive Stream for XR service instance**

**SYNOPSIS**

: **`gcloud immersive-stream xr instances describe` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/describe#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a specific Immersive Stream for XR service instance.

**EXAMPLES**

: To describe the service instance, run:

```
gcloud immersive-stream xr instances describe my-instance
```

**POSITIONAL ARGUMENTS**

: **Instance resource - The name of the service instance you want to describe. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Global location name.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- global is the only supported location.**

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

: This command uses the `stream/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com](https://cloud.google.com)

**NOTES**

: This variant is also available:

```
gcloud alpha immersive-stream xr instances describe
```