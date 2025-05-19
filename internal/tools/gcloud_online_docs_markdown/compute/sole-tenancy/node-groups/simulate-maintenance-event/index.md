# gcloud compute sole-tenancy node-groups simulate-maintenance-event  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event)*

**NAME**

: **gcloud compute sole-tenancy node-groups simulate-maintenance-event - simulate maintenance of a Compute Engine node group**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-groups simulate-maintenance-event` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event#NAME)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event#--async)`] [`[--nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event#--nodes)`=[`NODE`,…]] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Simulate maintenance of a Compute Engine node group.

**EXAMPLES**

: To simulate maintenance of a node group, run:

```
gcloud compute sole-tenancy node-groups simulate-maintenance-event my-node-group --nodes=example-nodes
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node group to operate on.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--nodes**:
The names of the nodes to simulate maintenance event.

**--zone**:
Zone of the node group to operate on. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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

: These variants are also available:

```
gcloud alpha compute sole-tenancy node-groups simulate-maintenance-event
```

```
gcloud beta compute sole-tenancy node-groups simulate-maintenance-event
```