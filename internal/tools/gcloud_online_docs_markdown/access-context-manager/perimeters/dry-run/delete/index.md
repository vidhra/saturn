# gcloud access-context-manager perimeters dry-run delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete)*

**NAME**

: **gcloud access-context-manager perimeters dry-run delete - mark the Service Perimeter as deleted in the dry-run mode**

**SYNOPSIS**

: **`gcloud access-context-manager perimeters dry-run delete` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete#--policy)`=`POLICY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: When this command completed successfully, the affected Service Perimeter will be
considered to have been deleted in the dry-run mode, but the enforcement mode
configuration will be left untouched.

**EXAMPLES**

: To mark the Service Perimeter as deleted in the dry-run mode:

```
gcloud access-context-manager perimeters dry-run delete my-perimeter
```

**POSITIONAL ARGUMENTS**

: **Perimeter resource - The service perimeter to delete. The arguments in this
group can be used to specify the attributes of this resource.
This must be specified.

**`PERIMETER`**:
ID of the perimeter or fully qualified identifier for the perimeter.
To set the `perimeter` attribute:

- provide the argument `perimeter` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `perimeter` on the command line with a fully
specified name;
- provide the argument `--policy` on the command line;
- set the property `access_context_manager/policy`.**

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
gcloud alpha access-context-manager perimeters dry-run delete
```

```
gcloud beta access-context-manager perimeters dry-run delete
```