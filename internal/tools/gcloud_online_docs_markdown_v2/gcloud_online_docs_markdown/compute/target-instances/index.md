# gcloud compute target-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances)*

**NAME**

: **gcloud compute target-instances - read and manipulate Compute Engine virtual target instances**

**SYNOPSIS**

: **`gcloud compute target-instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Compute Engine virtual target instances.
For more information about target instances, see the [target
instances documentation](https://cloud.google.com/compute/docs/protocol-forwarding#targetinstances).
See also: [Target
instances API](https://cloud.google.com/compute/docs/reference/rest/v1/targetInstances).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create)`**:
Create a target instance for handling traffic from a forwarding rule.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/delete)`**:
Delete target instances.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/describe)`**:
Describe a target instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/list)`**:
List Google Compute Engine target instances.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/update)`**:
Update a Compute Engine target instance.

**NOTES**

: These variants are also available:

```
gcloud alpha compute target-instances
```

```
gcloud beta compute target-instances
```