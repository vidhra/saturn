# gcloud edge-cloud networking routers add-bgp-peer  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer)*

**NAME**

: **gcloud edge-cloud networking routers add-bgp-peer - add a BGP peer to a Distributed Cloud Edge Network router**

**SYNOPSIS**

: **`gcloud edge-cloud networking routers add-bgp-peer` (`[ROUTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#ROUTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--zone)`=`ZONE`) `[--interface](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--interface)`=`INTERFACE` `[--peer-asn](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--peer-asn)`=`PEER_ASN` `[--peer-ipv4-range](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--peer-ipv4-range)`=`PEER_IPV4_RANGE` `[--peer-name](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--peer-name)`=`PEER_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a BGP peer to a Distributed Cloud Edge Network router

**EXAMPLES**

: To create and add a BGP peer for the Distributed Cloud Edge Network router
'my-router' in edge zone 'us-central1-edge-den1' , run:

```
gcloud edge-cloud networking routers add-bgp-peer my-router --interface=my-int-r1 --peer-asn=33333 --peer-name=peer1 --peer-ipv4-range=208.117.254.232/31 --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Router resource - The router to which we add a bgp peer. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ROUTER`**:
ID of the router or fully qualified identifier for the router.
To set the `router` attribute:

- provide the argument `router` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the router.
To set the `location` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The zone of the router.
To set the `zone` attribute:

- provide the argument `router` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--interface**:
The name of the interface for this BGP peer.

**--peer-asn**:
The BGP autonomous system number (ASN) for this BGP peer. Must be a 16-bit or
32-bit private ASN as defined in https://tools.ietf.org/html/rfc6996, for
example `--asn=64512`.

**--peer-ipv4-range**:
The IPv4 link-local address range of the peer router.

**--peer-name**:
The name of the new BGP peer being added.

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

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking routers add-bgp-peer
```