# gcloud compute os-config patch-jobs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs)*

**NAME**

: **gcloud compute os-config patch-jobs - manage OS patches for Compute Engine VMs**

**SYNOPSIS**

: **`gcloud compute os-config patch-jobs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage OS patches for Compute Engine VMs.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cancel](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/cancel)`**:
Cancel a specific OS patch job which must currently be active.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/describe)`**:
Describe a specified OS patch job.

**`[execute](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute)`**:
Execute an OS patch on the specified VM instances.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list)`**:
List ongoing and completed patch jobs.

**`[list-instance-details](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/list-instance-details)`**:
List the instance details for an OS patch job.

**NOTES**

: This variant is also available:

```
gcloud beta compute os-config patch-jobs
```