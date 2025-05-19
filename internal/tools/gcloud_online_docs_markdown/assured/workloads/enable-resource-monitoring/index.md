# gcloud assured workloads enable-resource-monitoring  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring)*

**NAME**

: **gcloud assured workloads enable-resource-monitoring - enables Resource Monitoring for an Assured Workloads environment**

**SYNOPSIS**

: **`gcloud assured workloads enable-resource-monitoring` (`[WORKLOAD](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring#WORKLOAD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/enable-resource-monitoring#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enable resource violation monitoring for a workload.

**EXAMPLES**

: To enable resource violation monitoring for a workload in the us-central1
region, belonging to an organization with ID 123, with workload ID 456, run:

```
gcloud assured workloads enable-resource-monitoring organizations/123/locations/us-central1/workloads/456
```

**POSITIONAL ARGUMENTS**

: **Workload resource - The Assured Workloads environment resource to
enable-resource-monitoring. The arguments in this group can be used to specify
the attributes of this resource.
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
gcloud alpha assured workloads enable-resource-monitoring
```

```
gcloud beta assured workloads enable-resource-monitoring
```