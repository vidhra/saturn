# gcloud alpha assured workloads delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete)*

**NAME**

: **gcloud alpha assured workloads delete - delete Assured Workloads environment**

**SYNOPSIS**

: **`gcloud alpha assured workloads delete` (`[WORKLOAD](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete#WORKLOAD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete#--organization)`=`ORGANIZATION`) [`[--etag](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete a given Assured Workloads environment.

**EXAMPLES**

: To delete an Assured Workload environment in the us-central1 region, belonging
to an organization with ID 123, with workload ID 456 and an etag of 789, run:

```
gcloud alpha assured workloads delete organizations/123/locations/us-central1/workloads/456 --etag=789
```

**POSITIONAL ARGUMENTS**

: **Workload resource - The Assured Workloads environment resource to delete. The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`WORKLOAD`**:
ID of the workload or fully qualified identifier for the workload.
To set the `workload` attribute:

- provide the argument `workload` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the workload.
To set the `location` attribute:

- provide the argument `workload` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The parent organization for the workload.
To set the `organization` attribute:

- provide the argument `workload` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--etag**:
The etag acquired by reading the Assured Workloads environment or AW "resource".

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
gcloud assured workloads delete
```

```
gcloud beta assured workloads delete
```