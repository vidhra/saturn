# gcloud compute instance-groups unmanaged add-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances)*

**NAME**

: **gcloud compute instance-groups unmanaged add-instances - adds instances to an unmanaged instance group by name**

**SYNOPSIS**

: **`gcloud compute instance-groups unmanaged add-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances#INSTANCE)`,…] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups unmanaged add-instances` adds
existing instances to an unmanaged instance group by name. For example:

```
gcloud compute instance-groups unmanaged add-instances my-group --instances my-instance-1,my-instance-2 --zone us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
A list of names of instances to add to the instance group. These must exist
beforehand and must live in the same zone as the instance group.

**OPTIONAL FLAGS**

: **--zone**:
Zone of the instance group to operate on. If not specified and the
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
gcloud alpha compute instance-groups unmanaged add-instances
```

```
gcloud beta compute instance-groups unmanaged add-instances
```