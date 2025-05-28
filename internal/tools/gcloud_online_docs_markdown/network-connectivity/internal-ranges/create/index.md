# gcloud network-connectivity internal-ranges create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create)*

**NAME**

: **gcloud network-connectivity internal-ranges create - create a new internal range**

**SYNOPSIS**

: **`gcloud network-connectivity internal-ranges create` (`[INTERNAL_RANGE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#INTERNAL_RANGE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--region)`=`REGION`) `[--network](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--network)`=`NETWORK` (`[--ip-cidr-range](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--ip-cidr-range)`=`IP_CIDR_RANGE`     | [`[--prefix-length](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--prefix-length)`=`PREFIX_LENGTH` : `--allocation_strategy`=`ALLOCATION_STRATEGY` `[--exclude-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--exclude-cidr-ranges)`=[`EXCLUDE_CIDR_RANGES`,…] `--first_available_ranges_lookup_size`=`FIRST_AVAILABLE_RANGES_LOOKUP_SIZE` `[--target-cidr-range](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--target-cidr-range)`=[`TARGET_CIDR_RANGE`,…]]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--description)`=`DESCRIPTION`] [`[--immutable](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--immutable)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--overlaps](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--overlaps)`=[`OVERLAPS`,…]] [`[--peering](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--peering)`=`PEERING`; default="for-self"] [`[--usage](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--usage)`=`USAGE`; default="for-vpc"] [`[--migration-source](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--migration-source)`=`MIGRATION_SOURCE` `[--migration-target](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#--migration-target)`=`MIGRATION_TARGET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new internal range with the given name.

**EXAMPLES**

: Create an internal range with name ``my-range``
and ip-cidr-range ``192.168.0.0/25`` in network
``https://www.googleapis.com/compute/v1/projects/my-project/locations/global/networks/my-network``:

```
gcloud network-connectivity internal-ranges create my-range --ip-cidr-range="192.168.0.0/25" --network="https://www.googleapis.com/compute/v1/projects/my-pro\
ject/locations/global/networks/my-network" --project=my-project
```

Create an internal range with name ``my-range``
and auto-allocated /25 block (prefix-length
``25``) in network
``my-network``:

```
gcloud network-connectivity internal-ranges create my-range --prefix-length=25 --network="my-network" --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Internal range resource - Name of the internal range to be created. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `internal_range` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERNAL_RANGE`**:
ID of the internal range or fully qualified identifier for the internal range.
To set the `internal_range` attribute:

- provide the argument `internal_range` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The location ID.
To set the `region` attribute:

- provide the argument `internal_range` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- use default global location .**

**REQUIRED FLAGS**

: **--network**:
The URL or resource ID of the network in which to reserve the internal range.
Legacy network is not supported. This can only be specified for a global
internal address.
For example:

- [https://www.googleapis.com/compute/v1/projects/my-project/locations/global/networks/my-network](https://www.googleapis.com/compute/v1/projects/my-project/locations/global/networks/my-network)
- /projects/my-project/locations/global/networks/my-network
- my-network

**--ip-cidr-range**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the internal range to be created.

**--immutable**:
Mark the internal range as immutable. Then only non-semantic fields like
description and labels could be modified after creation.

**--labels**:
List of label KEY=VALUE pairs to add.

**--overlaps**:
Overlap specifications for the range being created.
`OVERLAPS` must be one of:

**`overlap-existing-subnet-range`**:
Allows for creation of internal ranges that overlap with existing subnets.

**`overlap-route-range`**:
Allows for creation or existence of routes that have a more specific destination
than the created range.

**--peering**:
The type of peering set for the internal range. `PEERING`
must be one of:

**`for-peer`**:
This behavior can be set when the internal range is being reserved for usage by
the peers. This means that no resource within the VPC in which it is being
created can use this to associate with a cloud resource, but one of the peers
can. This represents "donating" a range for peers to use.

**`for-self`**:
This beharior represents the case that the internal range is intended to be used
in the VPC on which it is created and is accessible from its peers. This implies
that peers or peer-of-peers cannot use this range.

**`not-shared`**:
This behavior can be set when the internal range is being reserved for usage by
the VPC on which it is created but not shared with the peers. In a sense it is
local to the VPC. This can be used to create internal ranges for various
purposes like HTTP_INTERNAL_LOAD_BALANCER or for interconnect routes that are
not shared with peers. This also implies that peers cannot use this range in a
way that is visible to this VPC, but can re-use this range as long as it is
NOT_SHARED from the peer VPC too.

**--usage**:
The type of usage set for the internal range. `USAGE` must
be one of:

**`external-to-vpc`**:
Ranges created with EXTERNAL_TO_VPC cannot be associated with cloud resources
and are meant to block out address ranges for various use cases, like for
example, usage on-prem, with dynamic route announcements via interconnect.

**`for-migration`**:
Ranges created with FOR_MIGRATION are used as locks for migrating subnetworks
between peered VPC networks.

**`for-vpc`**:
A cloud resource can use the reserved CIDR block by associating it with the
internal range resource if usage is set to FOR_VPC.

**--migration-source**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha network-connectivity internal-ranges create
```