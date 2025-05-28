# gcloud network-connectivity spokes linked-producer-vpc-network create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create)*

**NAME**

: **gcloud network-connectivity spokes linked-producer-vpc-network create - create a new Producer VPC spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes linked-producer-vpc-network create` `[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#SPOKE)` `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--hub)`=`HUB` `[--network](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--network)`=`NETWORK` `[--peering](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--peering)`=`PEERING` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--description)`=`DESCRIPTION`] [`[--exclude-export-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--exclude-export-ranges)`=[`CIDR_RANGE`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--global)`] [`[--include-export-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--include-export-ranges)`=[`CIDR_RANGE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Producer VPC spoke.

**EXAMPLES**

: To create a Producer VPC spoke named
``myspoke``, run:

```
gcloud network-connectivity spokes linked-producer-vpc-network create myspoke --hub="https://www.googleapis.com/networkconnectivity/v1/project\
 s/my-project/locations/global/hubs/my-hub" --global \
     --network="https://www.googleapis.com/compute/v1/projects/my-pro\
 ject/global/networks/my-vpc" --peering="my-peering-name" \
```

**POSITIONAL ARGUMENTS**

: **Spoke resource - Name of the spoke to create. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--global` on the command line.

This must be specified.

**`SPOKE`**:
ID of the spoke or fully qualified identifier for the spoke.
To set the `spoke` attribute:

- provide the argument `spoke` on the command line.**

**REQUIRED FLAGS**

: **--hub**:
Hub that the spoke will attach to. The hub must already exist.

**--network**:
Your VPC network that contains the peering to the Producer VPC, which this spoke
connects to the Hub. The peering must already exist and be in the ACTIVE state.

**--peering**:
Peering between your network and the Producer VPC, which this spoke connects to
the Hub. The peering must already exist and be in the ACTIVATE state.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the spoke to create.

**--exclude-export-ranges**:
Subnet IP address range(s) to hide from other VPC networks that are connected
through Network Connectivity Center.

**--global**:
Indicates that the spoke is global.

**--include-export-ranges**:
Subnet IP address range(s) to export to other VPC networks that are connected
through Network Connectivity Center.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity spokes linked-producer-vpc-network create
```