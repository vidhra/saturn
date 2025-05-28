# gcloud edge-cache origins delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete)*

**NAME**

: **gcloud edge-cache origins delete - delete an EdgeCacheOrigin resource**

**SYNOPSIS**

: **`gcloud edge-cache origins delete` (`[ORIGIN](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete#ORIGIN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cache/origins/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a EdgeCacheOrigin resource.

**EXAMPLES**

: To delete a EdgeCacheOrigin resource called 'my-origin', run:

```
gcloud edge-cache origins delete my-origin
```

**POSITIONAL ARGUMENTS**

: **Origin resource - The name of the EdgeCacheOrigin resource to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `origin` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ORIGIN`**:
ID of the origin or fully qualified identifier for the origin.
To set the `origin` attribute:

- provide the argument `origin` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `origin` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- use global location.**

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

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cache origins delete
```