# gcloud compute networks peerings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update)*

**NAME**

: **gcloud compute networks peerings update - update a Compute Engine network peering**

**SYNOPSIS**

: **`gcloud compute networks peerings update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--network)`=`NETWORK` [`[--export-custom-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--export-custom-routes)`] [`[--export-subnet-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--export-subnet-routes-with-public-ip)`] [`[--import-custom-routes](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--import-custom-routes)`] [`[--import-subnet-routes-with-public-ip](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--import-subnet-routes-with-public-ip)`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#--stack-type)`=`STACK_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To update the peering named peering-name to both export and import custom
routes, run:

```
gcloud compute networks peerings update peering-name --export-custom-routes --import-custom-routes
```

To update the peering named peering-name to both export and import subnet routes
with public ip, run:

```
gcloud compute networks peerings update peering-name --export-subnet-routes-with-public-ip --import-subnet-routes-with-public-ip
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the peering.

**REQUIRED FLAGS**

: **--network**:
The name of the network in the current project to be peered with the peer
network.

**OPTIONAL FLAGS**

: **--export-custom-routes**:
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
gcloud alpha compute networks peerings update
```

```
gcloud beta compute networks peerings update
```