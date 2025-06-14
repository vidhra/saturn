# gcloud vmware network-peerings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create)*

**NAME**

: **gcloud vmware network-peerings create - create a VMware Engine VPC network peering**

**SYNOPSIS**

: **`gcloud vmware network-peerings create` (`[NETWORK_PEERING](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#NETWORK_PEERING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--location)`=`LOCATION`) `[--peer-network](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--peer-network)`=`PEER_NETWORK` `[--peer-network-type](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--peer-network-type)`=`PEER_NETWORK_TYPE` `[--vmware-engine-network](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--vmware-engine-network)`=`VMWARE_ENGINE_NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--description)`=`DESCRIPTION`] [`[--no-exchange-subnet-routes](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--exchange-subnet-routes)`] [`[--no-export-custom-routes](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--export-custom-routes)`] [`[--no-export-custom-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--export-custom-routes-with-public-ip)`] [`[--no-import-custom-routes](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--import-custom-routes)`] [`[--no-import-custom-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--import-custom-routes-with-public-ip)`] [`[--peer-mtu](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--peer-mtu)`=`PEER_MTU`] [`[--peer-project](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--peer-project)`=`PEER_PROJECT`] [`[--vmware-engine-network-project](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#--vmware-engine-network-project)`=`VMWARE_ENGINE_NETWORK_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a VMware Engine VPC network peering. VPC network peering creation is
considered finished when the network peering is in ACTIVE state. Check the
progress of a VPC network peering using `[gcloud vmware
network-peerings list](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/list)`.

**EXAMPLES**

: To create a VPC network peering called `new-peering` that connects
the VMware Engine network `my-vmware-engine-network` with another
VMware Engine network `another-vmware-engine-network` from project
`another-project`, run:

```
gcloud vmware network-peerings create new-peering --vmware-engine-network=my-vmware-engine-network --peer-network=another-vmware-engine-network --peer-network-type=VMWARE_ENGINE_NETWORK --peer-project=another-project
```

In this example, the project is taken from gcloud properties core/project and
location is taken as `global`.

**POSITIONAL ARGUMENTS**

: **VMware Engine VPC network peering resource - network_peering. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `network_peering` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NETWORK_PEERING`**:
ID of the VMware Engine VPC network peering or fully qualified identifier for
the VMware Engine VPC network peering.
To set the `network-peering` attribute:

- provide the argument `network_peering` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `network_peering` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set location as 'global' (default).**

**REQUIRED FLAGS**

: **--peer-network**:
ID of the network to peer with the VMware Engine network. The peer network can
be a consumer VPC network or another VMware Engine network.

**--peer-network-type**:
Type of the VPC network to peer with the VMware Engine network.
PEER_NETWORK_TYPE must be one of the following:

- STANDARD: Peering connection used for connecting to another VPC network
established by the same user. For example, a peering connection to another VPC
network in the same project or to an on-premises network.
- VMWARE_ENGINE_NETWORK: Peering connection used for connecting to another VMware
Engine network.
- PRIVATE_SERVICES_ACCESS: Peering connection used for establishing private
services access.
- NETAPP_CLOUD_VOLUMES: Peering connection used for connecting to NetApp Cloud
Volumes.
- THIRD_PARTY_SERVICE: Peering connection used for connecting to third-party
services. Most third-party services require manual setup of reverse peering on
the VPC network associated with the third-party service.
- DELL_POWERSCALE: Peering connection used for connecting to Dell PowerScale
Filers.
- GOOGLE_CLOUD_NETAPP_VOLUMES: Peering connection used for connecting to Google
Cloud NetApp Volumes. `PEER_NETWORK_TYPE` must be one of:
`PEER_NETWORK_TYPE_UNSPECIFIED`, `STANDARD`,
`VMWARE_ENGINE_NETWORK`, `PRIVATE_SERVICES_ACCESS`,
`NETAPP_CLOUD_VOLUMES`, `THIRD_PARTY_SERVICE`,
`DELL_POWERSCALE`, `GOOGLE_CLOUD_NETAPP_VOLUMES`.

**--vmware-engine-network**:
ID of the VMware Engine network to attach the new peering to.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
User-provided description of the VPC network peering.

**--exchange-subnet-routes**:
True if full-mesh connectivity is created and managed automatically between
peered VPC networks; false otherwise. This field is always true because Google
Compute Engine automatically creates and manages subnetwork routes between two
VPC networks when the peering state is ACTIVE. Enabled by default, use
`--no-exchange-subnet-routes` to disable.

**--export-custom-routes**:
True if custom routes are exported to the peered VPC network; false otherwise.
The default value is true. Enabled by default, use
`--no-export-custom-routes` to disable.

**--export-custom-routes-with-public-ip**:
True if all subnet routes with public IP address range are exported; false
otherwise. The default value is true. Enabled by default, use
`--no-export-custom-routes-with-public-ip` to disable.

**--import-custom-routes**:
True if custom routes are imported to the peered VPC network; false otherwise.
The default value is true. Enabled by default, use
`--no-import-custom-routes` to disable.

**--import-custom-routes-with-public-ip**:
True if all subnet routes with public IP address range are imported; false
otherwise. The default value is true. Enabled by default, use
`--no-import-custom-routes-with-public-ip` to disable.

**--peer-mtu**:
Maximum transmission unit (MTU) in bytes.

**--peer-project**:
Project ID or project number of the peer network. Use this flag when the peer
network is in another project.

**--vmware-engine-network-project**:
Project of the VMware Engine network to attach the new peering to. Use this flag
when the VMware Engine network is in another project.

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