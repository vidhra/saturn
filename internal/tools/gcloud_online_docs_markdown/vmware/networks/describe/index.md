# gcloud vmware networks describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/networks/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/networks/describe)*

**NAME**

: **gcloud vmware networks describe - describe a Google Cloud VMware Engine network**

**SYNOPSIS**

: **`gcloud vmware networks describe` (`[VMWARE_ENGINE_NETWORK](https://cloud.google.com/sdk/gcloud/reference/vmware/networks/describe#VMWARE_ENGINE_NETWORK)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/networks/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/networks/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a VMware Engine network.

**EXAMPLES**

: To get a description of a network called `my-network` of type
`STANDARD` in project `my-project` and region
`global`, run:

```
gcloud vmware networks describe my-network --location=global --project=my-project
```

Or:

```
gcloud vmware networks describe my-network
```

In the second example, the project is taken from gcloud properties core/project
and the location is taken as `global`.
To get a description of a network called `my-network` of type
`LEGACY` in project `my-project` and region
`us-west2`, run:

```
gcloud vmware networks describe my-network --location=us-west2 --project=my-project
```

Or:

```
gcloud vmware networks describe my-network --location=us-west2
```

In the last example, the project is taken from gcloud properties core/project.
For VMware Engine networks of type `LEGACY`, you must always specify
a region as the location.

**POSITIONAL ARGUMENTS**

: **VMware Engine network resource - vmware_engine_network. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `vmware_engine_network` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VMWARE_ENGINE_NETWORK`**:
ID of the VMware Engine network or fully qualified identifier for the VMware
Engine network.
To set the `vmware-engine-network` attribute:

- provide the argument `vmware_engine_network` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `vmware_engine_network` on the command line with
a fully specified name;
- provide the argument `--location` on the command line;
- set location as 'global' (default) or a region.**

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