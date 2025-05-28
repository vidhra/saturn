# gcloud assured workloads violations acknowledge  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge)*

**NAME**

: **gcloud assured workloads violations acknowledge - acknowledge an existing Assured Workloads compliance violation**

**SYNOPSIS**

: **`gcloud assured workloads violations acknowledge` (`[VIOLATION](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#VIOLATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#--organization)`=`ORGANIZATION` `[--workload](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#--workload)`=`WORKLOAD`) `[--comment](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#--comment)`=`COMMENT` [`[--acknowledge-type](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#--acknowledge-type)`=`ACKNOWLEDGE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Acknowledge an existing Assured Workloads compliance violation.

**EXAMPLES**

: To acknowledge an Assured Workloads Violation in the `us-central1`
region, belonging to an organization with ID `123`, with workload ID
`456`, with violation ID `789` and comment as `test
ack`, run:

```
gcloud assured workloads violations acknowledge organizations/123/locations/us-central1/workloads/456/violations/789 --comment="test ack"
```

**POSITIONAL ARGUMENTS**

: **Violation resource - The Assured Workloads violation resource to acknowledge.
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`VIOLATION`**:
ID of the violation or fully qualified identifier for the violation.
To set the `violation` attribute:

- provide the argument `violation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the violation.
To set the `location` attribute:

- provide the argument `violation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The parent organization for the violation.
To set the `organization` attribute:

- provide the argument `violation` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.

**--workload**:
The workload for the violation.
To set the `workload` attribute:

- provide the argument `violation` on the command line with a fully
specified name;
- provide the argument `--workload` on the command line.**

**REQUIRED FLAGS**

: **--comment**:
Business justification used added to acknowledge a violation.

**OPTIONAL FLAGS**

: **--acknowledge-type**:
the acknowledge type for specified violation, which is one of: SINGLE_VIOLATION
- to acknowledge specified violation, EXISTING_CHILD_RESOURCE_VIOLATIONS - to
acknowledge specified org policy violation and all associated child resource
violations.

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
gcloud alpha assured workloads violations acknowledge
```

```
gcloud beta assured workloads violations acknowledge
```