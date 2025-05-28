# gcloud compute instance-groups unmanaged remove-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances)*

**NAME**

: **gcloud compute instance-groups unmanaged remove-instances - removes resources from an unmanaged instance group by instance name**

**SYNOPSIS**

: **`gcloud compute instance-groups unmanaged remove-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances#INSTANCE)`,…] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/remove-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups unmanaged remove-instances` removes
instances from an unmanaged instance group using the instance name.
This does not delete the actual instance resources but removes it from the
instance group.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
The names of the instances to remove from the instance group.

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
gcloud alpha compute instance-groups unmanaged remove-instances
```

```
gcloud beta compute instance-groups unmanaged remove-instances
```