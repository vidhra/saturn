# gcloud compute target-pools remove-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances)*

**NAME**

: **gcloud compute target-pools remove-instances - remove instances from a target pool**

**SYNOPSIS**

: **`gcloud compute target-pools remove-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#INSTANCE)`,…] [`[--instances-zone](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#--instances-zone)`=`INSTANCES_ZONE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#--region)`=`REGION`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-pools remove-instances` is used to remove one
or more instances from a target pool. For more information on health checks and
load balancing, see [https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/](https://cloud.google.com/compute/docs/load-balancing-and-autoscaling/)

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the target pool from which to remove the instances.

**REQUIRED FLAGS**

: **--instances**:
Specifies a list of instances to remove from the target pool.

**OPTIONAL FLAGS**

: **--instances-zone**:
Zone of the instances to remove from the target pool. If not specified and the
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

**--region**:
Region of the target pool to operate on. If not specified, it will be set to the
region of the instances. Overrides the default `compute/region`
property value for this command invocation.

**--zone**:
Zone of the instances to remove from the target pool. DEPRECATED, use
--instances-zone. If not specified, you will be prompted to select a zone.
Overrides the default `compute/zone` property value for this command
invocation.

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
gcloud alpha compute target-pools remove-instances
```

```
gcloud beta compute target-pools remove-instances
```