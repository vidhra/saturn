# gcloud compute sole-tenancy node-groups perform-maintenance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance)*

**NAME**

: **gcloud compute sole-tenancy node-groups perform-maintenance - perform maintenance on nodes in a Compute Engine node group**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-groups perform-maintenance` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#NAME)` `[--nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#--nodes)`=`NODE`,[`[NODE](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#NODE)`,…] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#--start-time)`=`START_TIME`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Perform maintenance on nodes in a Compute Engine node group.

**EXAMPLES**

: To perform maintenance on nodes in a node group, run:

```
gcloud compute sole-tenancy node-groups perform-maintenance my-node-group --nodes=node-1,node-2 --start-time=2023-05-01T00:00:00.000-08:00
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node group to operate on.

**REQUIRED FLAGS**

: **--nodes**:
The names of the nodes to perform maintenance on.

**OPTIONAL FLAGS**

: **--start-time**:
The requested time for the maintenance window to start. The timestamp must be an
RFC3339 valid string.

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
gcloud alpha compute sole-tenancy node-groups perform-maintenance
```

```
gcloud beta compute sole-tenancy node-groups perform-maintenance
```