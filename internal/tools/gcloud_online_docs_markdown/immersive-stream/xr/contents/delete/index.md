# gcloud immersive-stream xr contents delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete)*

**NAME**

: **gcloud immersive-stream xr contents delete - delete an Immersive Stream for XR content resource**

**SYNOPSIS**

: **`gcloud immersive-stream xr contents delete` (`[CONTENT](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete#CONTENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/contents/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete an Immersive Stream for XR content resource.

**EXAMPLES**

: To delete a content called `my-content`, run:

```
gcloud immersive-stream xr contents delete my-content
```

**POSITIONAL ARGUMENTS**

: **Content resource - Immersive Stream for XR content resource to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `content` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONTENT`**:
ID of the content or fully qualified identifier for the content.
To set the `content` attribute:

- provide the argument `content` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Global location name.
To set the `location` attribute:

- provide the argument `content` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- global is the only supported location.**

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

**API REFERENCE**

: This command uses the `stream/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com](https://cloud.google.com)

**NOTES**

: This variant is also available:

```
gcloud alpha immersive-stream xr contents delete
```