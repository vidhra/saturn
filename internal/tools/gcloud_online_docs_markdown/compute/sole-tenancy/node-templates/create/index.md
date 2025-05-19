# gcloud compute sole-tenancy node-templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create)*

**NAME**

: **gcloud compute sole-tenancy node-templates create - create a Compute Engine node template**

**SYNOPSIS**

: **`gcloud compute sole-tenancy node-templates create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#NAME)` (`[--node-requirements](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--node-requirements)`=[`localSSD`=`LOCALSSD`],[`memory`=`MEMORY`],[`vCPU`=`VCPU`]     | `[--node-type](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--node-type)`=`NODE_TYPE`) [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--cpu-overcommit-type](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--cpu-overcommit-type)`=`CPU_OVERCOMMIT_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--description)`=`DESCRIPTION`] [`[--disk](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--disk)`=[`count`=`COUNT`],[`size`=`SIZE`],[`type`=`TYPE`]] [`[--node-affinity-labels](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--node-affinity-labels)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--region)`=`REGION`] [`[--server-binding](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#--server-binding)`=`SERVER_BINDING`; default="restart-node-on-any-server"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine node template.

**EXAMPLES**

: To create a node template of type `n1-node-96-624`, run:

```
gcloud compute sole-tenancy node-templates create my-node-template --node-type=n1-node-96-624
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the node templates to operate on.

**REQUIRED FLAGS**

: **--node-requirements**

**OPTIONAL FLAGS**

: **--accelerator**:
Attaches accelerators (e.g. GPUs) to the node template.

**`type`**:
The specific type (e.g. nvidia-tesla-k80 for nVidia Tesla K80) of accelerator to
attach to the node template. Use 'gcloud compute accelerator-types list' to
learn about all available accelerator types.

**`count`**:
Number of accelerators to attach to each node template. The default value is 1.

**--cpu-overcommit-type**:
CPU overcommit type for nodes created based on this template. To overcommit CPUs
on a VM, set --cpu-overcommit-type equal to either standard or none, and then
when creating a VM, specify a value for the --min-node-cpu flag. Lower values
for --min-node-cpu specify a higher overcommit ratio, that is, proportionally
more vCPUs in relation to physical CPUs. You can only overcommit CPUs on VMs
that are scheduled on nodes that support it.
`CPU_OVERCOMMIT_TYPE` must be one of:
`enabled`, `none`.

**--description**:
An optional description of this resource.

**--disk**:
Option to specify disk properties. It is mutually exclusive with
'--node-requirements=[localSSD=LOCALSSD]' but
'--node-requirements=[memory=MEMORY],[vCPU=VCPU],any' are still available.

**`type`**:
Specifies the desired disk type on the node. This disk type must be a local
storage type. This should be the name of the disk type. Currently only
`local-ssd` is allowed.

**`size`**:
The size of the disk in GiB. Currently you can specify only 375 GiB or no value
at all.

**`count`**:
Specifies the number of such disks. Set to `16` or `24`.

**--node-affinity-labels**:
Labels to use for node affinity, which will be used in instance scheduling. This
corresponds to the `--node-affinity` flag on `compute instances
create` and `compute instance-templates create`.

**--region**:
Region of the node templates to operate on. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

**--server-binding**:
The server binding policy for nodes using this template, which determines where
the nodes should restart following a maintenance event.
`SERVER_BINDING` must be one of:

**`restart-node-on-any-server`**:
Nodes using this template will restart on any physical server following a
maintenance event.

**`restart-node-on-minimal-servers`**:
Nodes using this template will restart on the same physical server following a
maintenance event, instead of being live migrated to or restarted on a new
physical server. This means that VMs on such nodes will experience outages while
maintenance is applied. This option may be useful if you are using software
licenses tied to the underlying server characteristics such as physical sockets
or cores, to avoid the need for additional licenses when maintenance occurs.
Note that in some cases, Google Compute Engine may need to move your VMs to a
new underlying server. During these situations your VMs will be restarted on a
new physical server and assigned a new sole tenant physical server ID.

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
gcloud alpha compute sole-tenancy node-templates create
```

```
gcloud beta compute sole-tenancy node-templates create
```