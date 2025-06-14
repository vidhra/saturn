# gcloud vmware network-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update)*

**NAME**

: **gcloud vmware network-policies update - update a VMware Engine network policy**

**SYNOPSIS**

: **`gcloud vmware network-policies update` (`[NETWORK_POLICY](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#NETWORK_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--description)`=`DESCRIPTION`] [`[--edge-services-cidr](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--edge-services-cidr)`=`EDGE_SERVICES_CIDR`] [`[--external-ip-access](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--external-ip-access)`] [`[--internet-access](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#--internet-access)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a VMware Engine network policy.

**EXAMPLES**

: To update a network policy named `my-network-policy` so that it
disables the external IP access service, run:

```
gcloud vmware network-policies update my-network-policy --location=us-west2 --project=my-project --no-external-ip-access
```

Or:

```
gcloud vmware network-policies update my-network-policy --no-external-ip-access
```

In the second example, the project and the location are taken from gcloud
properties core/project and compute/regions respectively.

**POSITIONAL ARGUMENTS**

: **VMware Engine Network Policy resource - network_policy. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `network_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NETWORK_POLICY`**:
ID of the VMware Engine Network Policy or fully qualified identifier for the
VMware Engine Network Policy.
To set the `network-policy` attribute:

- provide the argument `network_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `network_policy` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Updated description for the network policy.

**--edge-services-cidr**:
Updated IP address range to use for internet access and external IP access
gateways, in CIDR notation.

**--external-ip-access**:
Enable or disable network service that allows external IP addresses to be
assigned to VMware workloads. To enable this service,
`internet-access` must also be enabled. Use
`--no-external-ip-access` to disable.

**--internet-access**:
Enable or disable network service that allows VMware workloads to access the
internet. Use `--no-internet-access` to disable.

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