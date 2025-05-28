# gcloud vmware node-types describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/node-types/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/node-types/describe)*

**NAME**

: **gcloud vmware node-types describe - display data associated with a Google Cloud VMware Engine node type**

**SYNOPSIS**

: **`gcloud vmware node-types describe` (`[NODE_TYPE](https://cloud.google.com/sdk/gcloud/reference/vmware/node-types/describe#NODE_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/node-types/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/node-types/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display data associated with a VMware Engine node type, such as its compute,
storage, and memory.

**EXAMPLES**

: To describe node type `standard-72` in location
`us-west1-a`, run:

```
gcloud vmware node-types describe standard-72 --location=us-central1 --project=my-project
```

Or:

```
gcloud vmware node-types describe standard-72
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/zone.

**POSITIONAL ARGUMENTS**

: **Node type resource - node_type. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `node_type` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NODE_TYPE`**:
ID of the node type or fully qualified identifier for the node type.
To set the `node-type` attribute:

- provide the argument `node_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `node_type` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

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