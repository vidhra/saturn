# gcloud compute target-instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create)*

**NAME**

: **gcloud compute target-instances create - create a target instance for handling traffic from a forwarding rule**

**SYNOPSIS**

: **`gcloud compute target-instances create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#NAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#--instance)`=`INSTANCE` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#--description)`=`DESCRIPTION`] [`[--instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#--instance-zone)`=`INSTANCE_ZONE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#--network)`=`NETWORK`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-instances create` is used to create a target
instance for handling traffic from one or more forwarding rules. Target
instances are ideal for traffic that should be managed by a single source. For
more information on target instances, see [https://cloud.google.com/compute/docs/protocol-forwarding/#targetinstances](https://cloud.google.com/compute/docs/protocol-forwarding/#targetinstances)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the target instance to operate on.

**REQUIRED FLAGS**

: **--instance**:
The name of the virtual machine instance that will handle the traffic.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description of the target instance.

**--instance-zone**:
Zone of the instance to operate on. If not specified, it will be set to the same
as zone. Overrides the default `compute/zone` property value for this
command invocation.

**--network**:
Network that this target instance applies to. This is only necessary if the
corresponding instance has multiple network interfaces. If not specified, the
default network interface will be used.

**--zone**:
Zone of the target instance to operate on. If not specified and the
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
gcloud alpha compute target-instances create
```

```
gcloud beta compute target-instances create
```