# gcloud compute networks peerings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create)*

**NAME**

: **gcloud compute networks peerings create - create a Compute Engine network peering**

**SYNOPSIS**

: **`gcloud compute networks peerings create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--network)`=`NETWORK` `[--peer-network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--peer-network)`=`PEER_NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--async)`] [`[--auto-create-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--auto-create-routes)`] [`[--export-custom-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--export-custom-routes)`] [`[--export-subnet-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--export-subnet-routes-with-public-ip)`] [`[--import-custom-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--import-custom-routes)`] [`[--import-subnet-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--import-subnet-routes-with-public-ip)`] [`[--peer-project](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--peer-project)`=`PEER_PROJECT`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute networks peerings create` is used to create peerings
between virtual networks. Each side of a peering association is set up
independently. Peering will be active only when the configuration from both
sides matches.

**EXAMPLES**

: To create a network peering with the name 'peering-name' between the network
'local-network' and the network 'peer-network' which exports and imports custom
routes and subnet routes with public IPs, run:

```
gcloud compute networks peerings create peering-name --network=local-network --peer-network=peer-network --export-custom-routes --import-custom-routes --export-subnet-routes-with-public-ip --import-subnet-routes-with-public-ip
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the peering.

**REQUIRED FLAGS**

: **--network**:
The name of the network in the current project to be peered with the peer
network.

**--peer-network**:
The name of the network to be peered with the current network.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-create-routes**:
(DEPRECATED) If set, will automatically create routes for the network peering.
Flag auto-create-routes is deprecated. Peer network subnet routes are always
created in a network when peered.
Flag --auto-create-routes is deprecated and will be removed in a future release.

**--export-custom-routes**:
If set, the network will export custom routes to peer network. Use
--no-export-custom-routes to disable it.

**--export-subnet-routes-with-public-ip**:
If set, the network will export subnet routes with addresses in the public IP
ranges to peer network. Use --no-export-subnet-routes-with-public-ip to disable
it.

**--import-custom-routes**:
If set, the network will import custom routes from peer network. Use
--no-import-custom-routes to disable it.

**--import-subnet-routes-with-public-ip**:
If set, the network will import subnet routes with addresses in the public IP
ranges from peer network. Use --no-import-subnet-routes-with-public-ip to
disable it.

**--peer-project**:
The name of the project for the peer network. If not specified, defaults to
current project.

**--stack-type**:
Stack type of the peering. If not specified, defaults to IPV4_ONLY.
STACK_TYPE must be one of:

```
IPV4_ONLY
   Only IPv4 traffic and routes will be exchanged across this peering.
```

```
IPV4_IPV6
   IPv4 traffic and routes will be exchanged across this peering.
   IPv6 traffic and routes will be exchanged if the matching peering
   configuration also has stack_type set to IPV4_IPV6.
```

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

**NOTES**

: These variants are also available:

```
gcloud alpha compute networks peerings create
```

```
gcloud beta compute networks peerings create
```