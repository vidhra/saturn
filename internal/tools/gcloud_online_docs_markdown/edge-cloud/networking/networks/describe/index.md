# gcloud edge-cloud networking networks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe)*

**NAME**

: **gcloud edge-cloud networking networks describe - show details about the Distributed Cloud Edge Network network**

**SYNOPSIS**

: **`gcloud edge-cloud networking networks describe` (`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe#NETWORK)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/networks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about the Distributed Cloud Edge Network network.

**EXAMPLES**

: To show details about a network called 'my-network' in edge zone
'us-central1-edge-den1', run:

```
gcloud edge-cloud networking networks describe my-network --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Network resource - The Distributed Cloud Edge Network network you want to
describe. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
gcloud alpha edge-cloud networking networks describe
```