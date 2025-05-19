# gcloud compute os-config os-policy-assignments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update)*

**NAME**

: **gcloud compute os-config os-policy-assignments update - update an OS policy assignment**

**SYNOPSIS**

: **`gcloud compute os-config os-policy-assignments update` (`[OS_POLICY_ASSIGNMENT](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#OS_POLICY_ASSIGNMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#--location)`=`LOCATION`) `[--file](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#--file)`=`FILE` [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an OS policy assignment

**EXAMPLES**

: To update an OS policy assignment `my-assignment` in location
`us-central1-a` with config file
`/path/to/file/config.yaml`, run:

```
gcloud compute os-config os-policy-assignments update my-assignment --location=us-central1-a --file=/path/to/file/config.yaml
```

**POSITIONAL ARGUMENTS**

: **OS policy assignment resource - OS policy assignment to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--file**:
Absolute path to the OS policy assignment file on your local client. File must
be in either JSON or YAML format. This file defines the OS policies that you
want to apply to your VMs, the target VMs that you want to apply the policies
to, and the rollout rate at which to apply the OS policies. For more information
about this resource and sample OS policy assignment files, see [https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies#os-policy-assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies#os-policy-assignment).

**OPTIONAL FLAGS**

: **--allow-missing**:
If set to true, and the OS policy assignment is not found, the new policy
assignment resource will be created.

**--async**:
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

: This command uses the `osconfig/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha compute os-config os-policy-assignments update
```