# gcloud compute target-pools  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools)*

**NAME**

: **gcloud compute target-pools - control Compute Engine target pools for network load balancing**

**SYNOPSIS**

: **`gcloud compute target-pools` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Control Compute Engine target pools for external passthrough Network Load
Balancers.
For more information about target pools, see the [target pools
documentation](https://cloud.google.com/load-balancing/docs/target-pools).
See also: [Target
pools API](https://cloud.google.com/compute/docs/reference/rest/v1/targetPools).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks)`**:
Add a legacy HTTP health check to a target pool.

**`[add-instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-instances)`**:
Add instances to a target pool.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/create)`**:
Define a load-balanced pool of virtual machine instances.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/delete)`**:
Delete target pools.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/describe)`**:
Describe a Compute Engine target pool.

**`[get-health](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/get-health)`**:
Get the health of instances in a target pool.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/list)`**:
List Google Compute Engine target pools.

**`[remove-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks)`**:
Remove an HTTP health check from a target pool.

**`[remove-instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances)`**:
Remove instances from a target pool.

**`[set-backup](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/set-backup)`**:
Set a backup pool for a target pool.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/update)`**:
Update a Compute Engine target pool.

**NOTES**

: These variants are also available:

```
gcloud alpha compute target-pools
```

```
gcloud beta compute target-pools
```