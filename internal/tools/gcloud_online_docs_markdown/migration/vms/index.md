# gcloud migration vms  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms](https://cloud.google.com/sdk/gcloud/reference/migration/vms)*

**NAME**

: **gcloud migration vms - provides Migrate to Virtual Machines (VM migration) service functionality**

**SYNOPSIS**

: **`gcloud migration vms` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/migration/vms#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud alpha migration vms command group provides the CLI for the Migrate to
Virtual Machines API. Google Cloud Migrate to Virtual Machines migrates VMs from
on-premises data center and other cloud providers to Google Compute Engine
virtual machine (VM) instances. VM Migration API must be enabled in your
project.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports)`**:
Imports images to Google Compute Engine from Google Cloud Storage.

**`[machine-image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports)`**:
Imports machine images to Google Compute Engine from Google Cloud Storage.

**`[target-projects](https://cloud.google.com/sdk/gcloud/reference/migration/vms/target-projects)`**:
Manage Target Projects.

**NOTES**

: This variant is also available:

```
gcloud alpha migration vms
```