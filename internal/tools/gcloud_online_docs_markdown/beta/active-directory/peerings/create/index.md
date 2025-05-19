# gcloud beta active-directory peerings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create)*

**NAME**

: **gcloud beta active-directory peerings create - create a Managed Microsoft Active Directory domain peering**

**SYNOPSIS**

: **`gcloud beta active-directory peerings create` `[PEERING](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create#PEERING)` `[--authorized-network](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create#--authorized-network)`=`AUTHORIZED_NETWORK` `[--domain](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create#--domain)`=`DOMAIN` [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Create a new Managed Microsoft AD domain peering with the
given name using Google Cloud's Managed Service for Microsoft Active Directory.
This command can fail for the following reasons:

- A domain peering with the same name already exists.
- The active account does not have permission to create AD domains peerings.
- There is an overlap between the provided CIDR range and authorized network's
CIDR.

**EXAMPLES**

: The following command creates an AD domain peering with the name
``my-peering``, network
``my-network`` and domain
``projects/domain-project/locations/global/domains/domain.com``

```
gcloud beta active-directory peerings create my-peering --domain=projects/domain-project/locations/global/domains/domain.com --authorized-network=projects/network-project/global/networks/my-network
```

**POSITIONAL ARGUMENTS**

: **Peering resource - Name of the managed Managed Microsoft AD domain peering you
want to create. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `peering` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PEERING`**:
ID of the peering or fully qualified identifier for the peering.
To set the `peering` attribute:

- provide the argument `peering` on the command line.**

**REQUIRED FLAGS**

: **--authorized-network**:
Name of the Network that is authorized to communicate with Managed Microsoft AD
domain. This is usually the full path name of the network in the peer project.

**--domain**:
Name of the managed Managed Microsoft AD domain you want to peer to.

**OPTIONAL FLAGS**

: **--async**:
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

: This command uses the `managedidentities/v1beta1` API. The full
documentation for this API can be found at: [https://cloud.google.com/managed-microsoft-ad/](https://cloud.google.com/managed-microsoft-ad/)

**NOTES**

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud active-directory peerings create
```

```
gcloud alpha active-directory peerings create
```