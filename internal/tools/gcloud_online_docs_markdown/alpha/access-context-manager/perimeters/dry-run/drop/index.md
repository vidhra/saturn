# gcloud alpha access-context-manager perimeters dry-run drop  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop)*

**NAME**

: **gcloud alpha access-context-manager perimeters dry-run drop - reset the dry-run mode configuration of a Service Perimeter**

**SYNOPSIS**

: **`gcloud alpha access-context-manager perimeters dry-run drop` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop#--policy)`=`POLICY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/drop#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Removes the explicit dry-run mode configuration for a
Service Perimeter. After this operation, the effective dry-run mode
configuration is implicitly inherited from the enforcement mode configuration.
No audit logs will be generated in this state.

**EXAMPLES**

: To reset the dry-run mode configuration for a Service Perimeter:

```
gcloud alpha access-context-manager perimeters dry-run drop my-perimeter
```

**POSITIONAL ARGUMENTS**

: **Perimeter resource - The service perimeter to reset. The arguments in this group
can be used to specify the attributes of this resource.
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager perimeters dry-run drop
```

```
gcloud beta access-context-manager perimeters dry-run drop
```