# gcloud vmware network-peerings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/describe)*

**NAME**

: **gcloud vmware network-peerings describe - describe a Google Cloud VMware Engine VPC network peering**

**SYNOPSIS**

: **`gcloud vmware network-peerings describe` (`[NETWORK_PEERING](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/describe#NETWORK_PEERING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/network-peerings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get information about a VPC network peering.

**EXAMPLES**

: To get information about a VPC network peering called `new-peering`,
run:

```
gcloud vmware network-peerings describe new-peering
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