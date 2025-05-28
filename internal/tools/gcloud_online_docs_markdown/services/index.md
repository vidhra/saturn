# gcloud services  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services](https://cloud.google.com/sdk/gcloud/reference/services)*

**NAME**

: **gcloud services - list, enable and disable APIs and services**

**SYNOPSIS**

: **`gcloud services` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/services#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/services#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud services command group lets you manage your project's access to
services provided by Google and third parties.

**EXAMPLES**

: To see how to enable a service, run:

```
gcloud services enable --help
```

To see how to list services, run:

```
gcloud services list --help
```

To see how to disable a service, run:

```
gcloud services disable --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[api-keys](https://cloud.google.com/sdk/gcloud/reference/services/api-keys)`**:
Manage API keys.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/services/operations)`**:
Manage Operation for various services.

**`[peered-dns-domains](https://cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains)`**:
Peered DNS domains for various private service connections.

**`[vpc-peerings](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings)`**:
VPC Peerings to various services.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[disable](https://cloud.google.com/sdk/gcloud/reference/services/disable)`**:
Disable a service for consumption for a project.

**`[enable](https://cloud.google.com/sdk/gcloud/reference/services/enable)`**:
Enables a service for consumption for a project.

**`[list](https://cloud.google.com/sdk/gcloud/reference/services/list)`**:
List services for a project.

**NOTES**

: These variants are also available:

```
gcloud alpha services
```

```
gcloud beta services
```