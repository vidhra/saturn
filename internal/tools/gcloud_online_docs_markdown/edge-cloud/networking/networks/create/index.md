# gcloud edge-cloud networking networks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create)*

**NAME**

: **gcloud edge-cloud networking networks create - create a Distributed Cloud Edge Network network**

**SYNOPSIS**

: **`gcloud edge-cloud networking networks create` (`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#NETWORK)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--mtu](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#--mtu)`=`MTU`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Distributed Cloud Edge Network network resource.

**EXAMPLES**

: To create a network called 'my-network' with MTU value of 9000 bytes in edge
zone 'us-central1-edge-den1', run:

```
gcloud edge-cloud networking networks create my-network --location=us-central1 --zone=us-central1-edge-den1 --mtu=9000
```

**POSITIONAL ARGUMENTS**

: **Network resource - Distributed Cloud Edge Network network to create. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NETWORK`**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `network` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `network` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The name of the Google Distributed Cloud Edge zone.
To set the `zone` attribute:

- provide the argument `network` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
An optional, textual description for the network.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--mtu**:
Maximum transmission unit (MTU) is the size of the largest IP packet that can be
transmitted on this network. Default value is 1500 bytes, and the valid values
are 1500 and 9000.

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

: This command uses the `edgenetwork/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/distributed-cloud-edge/docs](https://cloud.google.com/distributed-cloud-edge/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking networks create
```