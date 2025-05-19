# gcloud compute network-edge-security-services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services)*

**NAME**

: **gcloud compute network-edge-security-services - read and manipulate network edge security services**

**SYNOPSIS**

: **`gcloud compute network-edge-security-services` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate network edge security services.
Network edge security services are used to protect network load balancing
resources and instances with external IPs.
For example, to add advanced protection for a given region, create a network
edge security service in that region and attach a security policy with ADVANCED
DDoS protection enabled.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/create)`**:
Create a Compute Engine network edge security service.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/delete)`**:
Delete network edge security services.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/describe)`**:
Describe a Compute Engine network edge security service.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/list)`**:
List Google Compute Engine network edge security services.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services/update)`**:
Update a network edge security service.

**NOTES**

: These variants are also available:

```
gcloud alpha compute network-edge-security-services
```

```
gcloud beta compute network-edge-security-services
```