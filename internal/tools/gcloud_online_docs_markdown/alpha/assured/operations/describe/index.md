# gcloud alpha assured operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe)*

**NAME**

: **gcloud alpha assured operations describe - describe Assured Workloads operations**

**SYNOPSIS**

: **`gcloud alpha assured operations describe` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe#OPERATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Obtain details about a given Assured Workloads operation.

**EXAMPLES**

: To describe an Assured Workloads operation in the us-central1 region, belonging
to an organization with ID 123, with workload ID 456, run:

```
gcloud alpha assured operations describe organizations/123/locations/us-central1/operations/456
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The Assured Workloads operation resource to describe. The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the operation.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The parent organization for the operation.
To set the `organization` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

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
gcloud assured operations describe
```

```
gcloud beta assured operations describe
```