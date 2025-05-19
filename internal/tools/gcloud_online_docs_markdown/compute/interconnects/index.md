# gcloud compute interconnects  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects)*

**NAME**

: **gcloud compute interconnects - read and manipulate Compute Engine interconnects**

**SYNOPSIS**

: **`gcloud compute interconnects` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Cloud Interconnect connections.
For more information about Cloud Interconnect, see the [Cloud
Interconnect documentation](https://cloud.google.com//network-connectivity/docs/interconnect/concepts/overview).
See also: [Interconnects
API](https://cloud.google.com/compute/docs/reference/rest/v1/interconnects).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[attachments](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments)`**:
Read and manipulate Compute Engine interconnect attachments.

**`[groups](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups)`**:
Create or manipulate interconnect groups.

**`[locations](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/locations)`**:
Read and manipulate Compute Engine interconnect locations.

**`[macsec](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/macsec)`**:
Read and manipulate Compute Engine interconnect MACsec configuration.

**`[remote-locations](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/remote-locations)`**:
Read and manipulate Google Compute Engine interconnect remote locations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/create)`**:
Create a Compute Engine interconnect.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/delete)`**:
Delete Compute Engine interconnects.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/describe)`**:
Describe a Compute Engine interconnect.

**`[get-diagnostics](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/get-diagnostics)`**:
Get diagnostics of a Compute Engine interconnect.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/list)`**:
List Google Compute Engine interconnects.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/update)`**:
Update a Compute Engine interconnect.

**NOTES**

: These variants are also available:

```
gcloud alpha compute interconnects
```

```
gcloud beta compute interconnects
```