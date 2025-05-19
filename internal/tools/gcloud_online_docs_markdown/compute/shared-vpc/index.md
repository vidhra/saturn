# gcloud compute shared-vpc  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc)*

**NAME**

: **gcloud compute shared-vpc - configure shared VPC**

**SYNOPSIS**

: **`gcloud compute shared-vpc` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Configure Shared VPC configurations.
For more information about Shared VPC, see the [Shared VPC
documentation](https://cloud.google.com/vpc/docs/shared-vpc/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[associated-projects](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects)`**:
Configure associated projects for Shared VPC networking.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/organizations)`**:
Configure organizations for Shared VPC networking.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[disable](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/disable)`**:
Disable the given project as a shared VPC host.

**`[enable](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/enable)`**:
Enable the given project as a shared VPC host.

**`[get-host-project](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/get-host-project)`**:
Get the shared VPC host project that the given project is associated with.

**`[list-associated-resources](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/list-associated-resources)`**:
List the resources associated with the given shared VPC host project.

**NOTES**

: These variants are also available:

```
gcloud alpha compute shared-vpc
```

```
gcloud beta compute shared-vpc
```