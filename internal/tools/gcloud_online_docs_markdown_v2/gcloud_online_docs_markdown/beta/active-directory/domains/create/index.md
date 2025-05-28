# gcloud beta active-directory domains create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create)*

**NAME**

: **gcloud beta active-directory domains create - create a Managed Microsoft AD domain**

**SYNOPSIS**

: **`gcloud beta active-directory domains create` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#DOMAIN)` `[--region](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--region)`=[`REGION`,…] `[--reserved-ip-range](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--reserved-ip-range)`=`RESERVED_IP_RANGE` [`[--admin-name](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--admin-name)`=`ADMIN_NAME`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--async)`] [`[--authorized-networks](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--authorized-networks)`=[`AUTHORIZED_NETWORKS`,…]] [`[--enable-audit-logs](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--enable-audit-logs)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Create a new Managed Microsoft AD domain with the given name
using Google Cloud's Managed Service for Microsoft Active Directory.
This command can fail for the following reasons:

- An AD domain with the same name already exists.
- The active account does not have permission to create AD domains.
- There is an overlap between the provided CIDR range and authorized network's
CIDR.
- A valid region was not provided.

**EXAMPLES**

: The following command creates an AD domain with the name
`my-domain.com` in region `us-central1`, a network peering
to `my-network` and consuming the IP address range
`10.172.0.0/24`.

```
gcloud beta active-directory domains create my-domain.com --region=us-central1 --reserved-ip-range="10.172.0.0/24" --authorized-networks=projects/my-project/global/networks/my-network
```

**POSITIONAL ARGUMENTS**

: **Domain resource - Name of the managed Managed Microsoft AD domain you want to
create. This represents a Cloud resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `domain` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DOMAIN`**:
ID of the domain or fully qualified identifier for the domain.
To set the `domain` attribute:

- provide the argument `domain` on the command line.**

**REQUIRED FLAGS**

: **--region**:
Google Compute Engine region in which to provision domain controllers.

**--reserved-ip-range**:
Classless Inter-Domain Routing range of internal addresses that are reserved for
this domain.

**OPTIONAL FLAGS**

: **--admin-name**:
Name of the administrator that may be used to perform Active Directory
operations. This is a delegated administrator account provisioned by our
service. If left unspecified `MIAdmin` will be used. This is
different from both the domain administrator and the Directory Services Restore
Mode (DSRM) administrator.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--authorized-networks**:
Names of the Google Compute Engine networks to which the domain will be
connected.

**--enable-audit-logs**:
If specified, Active Directory data audit logs are enabled for the domain.

**--labels**:
List of label KEY=VALUE pairs to add.

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
gcloud active-directory domains create
```

```
gcloud alpha active-directory domains create
```