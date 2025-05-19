# gcloud compute sole-tenancy node-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create)*

**NAME**

: **gcloud compute sole-tenancy node-groups create - create a Compute Engine node group**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-groups create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#NAME)` `[--node-template](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--node-template)`=`NODE_TEMPLATE` `[--target-size](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--target-size)`=`TARGET_SIZE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--description)`=`DESCRIPTION`] [`[--maintenance-interval](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--maintenance-interval)`=`MAINTENANCE_INTERVAL`] [`[--maintenance-policy](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--maintenance-policy)`=`MAINTENANCE_POLICY`] [`[--maintenance-window-start-time](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--maintenance-window-start-time)`=`START_TIME`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--zone)`=`ZONE`] [`[--autoscaler-mode](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--autoscaler-mode)`=`AUTOSCALER_MODE` : `[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--min-nodes)`=`MIN_NODES`] [`[--share-setting](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--share-setting)`=`SHARE_SETTING` : `[--share-with](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#--share-with)`=`PROJECT`,[`[PROJECT](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#PROJECT)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine node group.

**EXAMPLES**

: To create a node group, run:

```
gcloud compute sole-tenancy node-groups create my-node-group --node-template=example-template --target-size=4
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node group to operate on.

**REQUIRED FLAGS**

: **--node-template**:
The name of the node template resource to be set for this node group.

**--target-size**:
The target initial number of nodes in the node group.

**OPTIONAL FLAGS**

: **--description**:
An optional description of this resource.

**--maintenance-interval**:
Specifies the frequency of planned maintenance events.
`MAINTENANCE_INTERVAL` must be one of:

**`as-needed`**:
hosts are eligible to receive infrastructure and hypervisor updates as they
become available.

**`recurrent`**:
hosts receive planned infrastructure and hypervisor updates on a periodic basis,
but not more frequently than every 28 days. This minimizes the number of planned
maintenance operations on individual hosts and reduces the frequency of
disruptions, both live migrations and terminations, on individual VMs.

**--maintenance-policy**:
Determines the maintenance behavior during host maintenance events. For more
information, see [https://cloud.google.com/compute/docs/nodes#maintenance_policies](https://cloud.google.com/compute/docs/nodes#maintenance_policies).
`MAINTENANCE_POLICY` must be one of:

**`default`**:
VM instances on the host are live migrated to a new physical server. This is the
default setting.

**`migrate-within-node-group`**:
VM instances on the host are live migrated to another node within the same node
group.

**`restart-in-place`**:
VM instances on the host are terminated and then restarted on the same physical
server after the maintenance event has completed.

**--maintenance-window-start-time**:
The time (in GMT) when planned maintenance operations window begins. The
possible values are 00:00, 04:00, 08:00, 12:00, 16:00, 20:00.

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

**--autoscaler-mode**

**--share-setting**

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
gcloud alpha compute sole-tenancy node-groups create
```

```
gcloud beta compute sole-tenancy node-groups create
```