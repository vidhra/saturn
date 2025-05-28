# gcloud vmware network-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create)*

**NAME**

: **gcloud vmware network-policies create - create a VMware Engine network policy**

**SYNOPSIS**

: **`gcloud vmware network-policies create` (`[NETWORK_POLICY](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#NETWORK_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--location)`=`LOCATION`) `[--edge-services-cidr](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--edge-services-cidr)`=`EDGE_SERVICES_CIDR` `[--vmware-engine-network](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--vmware-engine-network)`=`VMWARE_ENGINE_NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--description)`=`DESCRIPTION`] [`[--external-ip-access](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--external-ip-access)`] [`[--internet-access](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#--internet-access)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a VMware Engine network policy. Only one network policy applies to a
VMware Engine network per region. Check the progress of a network policy
creation using `[gcloud vmware
network-policies list](https://cloud.google.com/sdk/gcloud/reference/vmware/network-policies/list)`.

**EXAMPLES**

: To create a network policy called `my-network-policy` which connects
to the VMware Engine network `my-vmware-engine-network` using the
edge services address range `192.168.0.0/26` with the internet access
service enabled and the external IP access service disabled, run:

```
gcloud vmware network-policies create my-network-policy --location=us-west2 --project=my-project --vmware-engine-network=my-vmware-engine-network --edge-services-cidr=192.168.0.0/26 --internet-access --no-external-ip-access
```

Or:

```
gcloud vmware network-policies create my-network-policy --vmware-engine-network=my-vmware-engine-network --edge-services-cidr=192.168.0.0/26 --internet-access
```

In the second example, the project and the location are taken from gcloud
properties core/project and compute/region respectively. If the
`--external-ip-access` flag is not specified, it is taken as
`False`.

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

**REQUIRED FLAGS**

: **--edge-services-cidr**:
IP address range to use for internet access and external IP access gateways, in
CIDR notation. An RFC 1918 CIDR block with a "/26" prefix is required.

**--vmware-engine-network**:
Resource ID of the VMware Engine network to attach the new policy to.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
User-provided description of the network policy.

**--external-ip-access**:
Enable or disable network service that allows external IP addresses to be
assigned to VMware workloads. To enable this service,
`internet-access` must also be enabled. Use
`--no-external-ip-access` to disable. If the flag is not provided,
access to VMware workloads through external IP addresses is disabled.

**--internet-access**:
Enable or disable network service that allows VMware workloads to access the
internet. Use `--no-internet-access` to disable. If the flag is not
provided, internet access is disabled.

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