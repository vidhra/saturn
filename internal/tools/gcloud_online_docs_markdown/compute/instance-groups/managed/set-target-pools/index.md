# gcloud compute instance-groups managed set-target-pools  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools)*

**NAME**

: **gcloud compute instance-groups managed set-target-pools - set target pools of managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed set-target-pools` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools#NAME)` `[--target-pools](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools#--target-pools)`=[`TARGET_POOL`,…] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-target-pools#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed set-target-pools` sets the
target pools for an existing managed instance group. Instances that are part of
the managed instance group will be added to the target pool automatically.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--target-pools**:
Compute Engine Target Pools to add the instances to. Target Pools must be
specified by name or by URL. Example:
--target-pools=target-pool-1,target-pool-2. To clear the set of Target Pools
pass in an empty list. Example: --target-pools=""

**OPTIONAL FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed set-target-pools
```

```
gcloud beta compute instance-groups managed set-target-pools
```