# gcloud compute os-config os-policy-assignments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe)*

**NAME**

: **gcloud compute os-config os-policy-assignments describe - describe an OS policy assignment**

**SYNOPSIS**

: **`gcloud compute os-config os-policy-assignments describe` (`[OS_POLICY_ASSIGNMENT](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe#OS_POLICY_ASSIGNMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an OS policy assignment

**EXAMPLES**

: To describe an OS policy `my-assignment` in location
`us-central1-a`:

```
gcloud compute os-config os-policy-assignments describe my-assignment --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **OS policy assignment resource - OS policy assignment to describe. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `os_policy_assignment` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`OS_POLICY_ASSIGNMENT`**:
ID of the OS policy assignment or fully qualified identifier for the OS policy
assignment.
To set the `os_policy_assignment` attribute:

- provide the argument `os_policy_assignment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the OS policy assignment.
To set the `location` attribute:

- provide the argument `os_policy_assignment` on the command line with
a fully specified name;
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
gcloud alpha compute os-config os-policy-assignments describe
```