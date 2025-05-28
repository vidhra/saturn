# gcloud vmware private-clouds clusters delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete)*

**NAME**

: **gcloud vmware private-clouds clusters delete - delete a Google Cloud VMware Engine cluster**

**SYNOPSIS**

: **`gcloud vmware private-clouds clusters delete` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete#--private-cloud)`=`PRIVATE_CLOUD`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/clusters/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a cluster in a VMware Engine private cloud.

**EXAMPLES**

: To delete a cluster called `my-cluster` in private cloud
`my-private-cloud` and zone `us-west2-a`, run:

```
gcloud vmware private-clouds clusters delete my-cluster --location=us-west2-a --project=my-project --private-cloud=my-private-cloud
```

```
Or:
```

```
gcloud vmware private-clouds clusters delete my-cluster --private-cloud=my-private-cloud
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/zone.

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--private-cloud` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

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