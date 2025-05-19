# gcloud compute os-config os-policy-assignment-reports describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe)*

**NAME**

: **gcloud compute os-config os-policy-assignment-reports describe - describe an OS policy assignment report**

**SYNOPSIS**

: **`gcloud compute os-config os-policy-assignment-reports describe` (`[INSTANCE_OS_POLICY_ASSIGNMENT](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe#INSTANCE_OS_POLICY_ASSIGNMENT)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe#--instance)`=`INSTANCE` `[--location](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignment-reports/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an OS policy assignment report

**EXAMPLES**

: To describe the report of an OS policy assignment `my-assignment` for
an instance `my-instance` in location `us-central1-a`:

```
gcloud compute os-config os-policy-assignment-reports describe my-assignment --instance=my-instance --location=us-central1-a
```

Or use the relative names or URI of the resource, assuming the project ID is
`my-project`:

```
gcloud compute os-config os-policy-assignment-reports describe projects/my-project/locations/us-central1-a/instances/my-instance/osPolicyAssignments/my-assignment/report
```

```
gcloud compute os-config os-policy-assignment-reports describe https://osconfig.googleapis.com/v1alpha/projects/my-project/\
locations/us-central1-a/instances/instance-name/\
osPolicyAssignments/assignment-id/report
```

**POSITIONAL ARGUMENTS**

: **OS policy assignment resource - OS policy assignment report. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance_os_policy_assignment` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE_OS_POLICY_ASSIGNMENT`**:
ID of the OS policy assignment or fully qualified identifier for the OS policy
assignment.
To set the `instance_os_policy_assignment` attribute:

- provide the argument `instance_os_policy_assignment` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Compute Engine VM instance.
To set the `instance` attribute:

- provide the argument `instance_os_policy_assignment` on the command
line with a fully specified name;
- provide the argument `--instance` on the command line.

**--location**:
Location of the OS policy assignment.
To set the `location` attribute:

- provide the argument `instance_os_policy_assignment` on the command
line with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

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

: This command uses the `osconfig/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha compute os-config os-policy-assignment-reports describe
```