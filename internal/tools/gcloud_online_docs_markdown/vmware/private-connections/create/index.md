# gcloud vmware private-connections create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create)*

**NAME**

: **gcloud vmware private-connections create - create a Google Cloud Private Connection**

**SYNOPSIS**

: **`gcloud vmware private-connections create` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#PRIVATE_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--location)`=`LOCATION`) `[--service-project](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--service-project)`=`SERVICE_PROJECT` `[--type](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--type)`=`TYPE` `[--vmware-engine-network](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--vmware-engine-network)`=`VMWARE_ENGINE_NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--description)`=`DESCRIPTION`] [`[--routing-mode](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--routing-mode)`=`ROUTING_MODE`] [`[--service-network](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#--service-network)`=`SERVICE_NETWORK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new private connection to connect VMware Engine Network to the
specified VPC network. This establishes private IP connectivity between the VPC
network and all the VMware Private Clouds attached to the VMware Engine Network.
Private connection creation is considered finished when the connection is in
ACTIVE state. Check the progress of the private connection using `[gcloud vmware
private-connections list](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/list)`.

**EXAMPLES**

: To create a Private Connection of type PRIVATE_SERVICE_ACCESS, first obtain the
service-project by listing vpc-peerings, run:

```
gcloud compute networks peerings list --network=my-vpc --project=my-project
```

where my-vpc is the VPC on which a private service access connection is created
and project is the one in which the private connection will be created.
The response will be of this format:
NAME NETWORK PEER_PROJECT
servicenetworking-googleapis-com my-vpc td096d594ece09650-tp
The PEER_PROJECT field in the output of the command will provide the value for
the service-project required for creating the private connection.
To create a Private Connection called `my-private-connection` of type
`PRIVATE_SERVICE_ACCESS` in project `my-project` and
region `us-west1` with routing_mode `REGIONAL` to connect
service networking VPC from project `td096d594ece09650-tp` to legacy
VMware Engine Network `us-west1-default`, run:

```
gcloud vmware private-connections create my-private-connection --location=us-west1 --project=my-project --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --routing-mode=REGIONAL --service-project=td096d594ece09650-tp --type=PRIVATE_SERVICE_ACCESS
```

Or:

```
gcloud vmware private-connections create my-private-connection --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --routing-mode=REGIONAL --service-project=td096d594ece09650-tp --type=PRIVATE_SERVICE_ACCESS
```

```
In the second example, the project and location are taken from gcloud properties core/project and compute/region, respectively.
```

To create a Private Connection called `my-private-connection` of type
`THIRD_PARTY_SERVICE` in project `my-project` and region
`us-west1` to connect VPC `my-service-network` from
project `td096d594ece09650-tp` to legacy VMware Engine Network
`us-west1-default`, run:

```
gcloud vmware private-connections create my-private-connection --location=us-west1 --project=my-project --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --service-network=my-service-network --service-project=td096d594ece09650-tp --type=THIRD_PARTY_SERVICE
```

Or:

```
gcloud vmware private-connections create my-private-connection --vmware-engine-network=us-west1-default --description="A short description for the new private connection" --service-network=my-service-network --service-project=td096d594ece09650-tp --type=THIRD_PARTY_SERVICE
```

```
In the above example, the project and location are taken from gcloud properties core/project and compute/region, respectively.
```

If you try to create a private connection of type=THIRD_PARTY_SERVICE, and do
not provide the service-network field, an error will be thrown with the message:
Missing required argument [--service-network]: For private connection of type
THIRD_PARTY_SERVICE, service-network field is required

**POSITIONAL ARGUMENTS**

: **Private Connection resource - private_connection. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PRIVATE_CONNECTION`**:
ID of the Private Connection or fully qualified identifier for the Private
Connection.
To set the `private-connection` attribute:

- provide the argument `private_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.**

**REQUIRED FLAGS**

: **--service-project**:
Project ID or project number of the service network.

**--type**:
Type of private connection. `TYPE` must be one of:

**`DELL_POWERSCALE`**:
Peering connection used for connecting to Dell PowerScale.

**`NETAPP_CLOUD_VOLUMES`**:
Peering connection used for connecting to NetApp Cloud Volumes.

**`PRIVATE_SERVICE_ACCESS`**:
Peering connection used for establishing [private
services access](https://cloud.google.com/vpc/docs/private-services-access).

**`THIRD_PARTY_SERVICE`**:
Peering connection used for connecting to third-party services. Most third-party
services require manual setup of reverse peering on the VPC network associated
with the third-party service.

**--vmware-engine-network**:
Resource ID of the legacy VMware Engine network. Provide the
{vmware_engine_network_id}, which will be in the form of {location}-default. The
{location} is the same as the location specified in the private connection
resource.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Text describing the private connection.

**--routing-mode**:
Type of the routing mode. Default value is set to GLOBAL. For
type=PRIVATE_SERVICE_ACCESS, this field can be set to GLOBAL or REGIONAL, for
other types only GLOBAL is supported. `ROUTING_MODE` must
be one of: `GLOBAL`, `REGIONAL`.

**--service-network**:
Resource ID of the service network to connect with the VMware Engine network to
create a private connection.

- For type=PRIVATE_SERVICE_ACCESS, this field represents service networking VPC.
In this case the field value will be automatically set to
`servicenetworking` and cannot be changed.
- For type=NETAPP_CLOUD_VOLUME, this field represents NetApp service VPC. In this
case the field value will be automatically set to `netapp-tenant-vpc`
and cannot be changed.
- For type=DELL_POWERSCALE, this field represents Dell service VPC. In this case
the field value will be automatically set to `dell-tenant-vpc` and
cannot be changed.
- For type=THIRD_PARTY_SERVICE, this field could represent a consumer VPC or any
other producer VPC to which the VMware Engine Network needs to be connected.
service-network field is required for this type.

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