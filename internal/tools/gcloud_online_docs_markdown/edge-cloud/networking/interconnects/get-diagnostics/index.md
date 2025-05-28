# gcloud edge-cloud networking interconnects get-diagnostics  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics)*

**NAME**

: **gcloud edge-cloud networking interconnects get-diagnostics - get the diagnostics of a specified Distributed Cloud Edge Network interconnect**

**SYNOPSIS**

: **`gcloud edge-cloud networking interconnects get-diagnostics` (`[INTERCONNECT](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics#INTERCONNECT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/interconnects/get-diagnostics#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the diagnostics of a specified Distributed Cloud Edge Network interconnect.

**EXAMPLES**

: To get the diagnostics of the Distributed Cloud Edge Network interconnect
'my-interconnect' in edge zone 'us-central1-edge-den1' , run:

```
gcloud edge-cloud networking interconnects get-diagnostics my-interconnect --location=us-central1 --zone=us-central1-edge-den1
```

**POSITIONAL ARGUMENTS**

: **Interconnect resource - The interconnect to get diagnostics. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `interconnect` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCONNECT`**:
ID of the interconnect or fully qualified identifier for the interconnect.
To set the `interconnect` attribute:

- provide the argument `interconnect` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the interconnect.
To set the `location` attribute:

- provide the argument `interconnect` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The zone of the interconnect.
To set the `zone` attribute:

- provide the argument `interconnect` on the command line with a fully
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

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking interconnects get-diagnostics
```