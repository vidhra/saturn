# gcloud compute instance-groups unmanaged delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete)*

**NAME**

: **gcloud compute instance-groups unmanaged delete - delete Compute Engine unmanaged instance groups**

**SYNOPSIS**

: **`gcloud compute instance-groups unmanaged delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete#NAME)` …] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups unmanaged delete` deletes one or more
Compute Engine unmanaged instance groups. This command just deletes the instance
group and does not delete the individual virtual machine instances in the
instance group. For example:

```
gcloud compute instance-groups unmanaged delete example-instance-group-1 example-instance-group-2 --zone us-central1-a
```

The above example deletes two instance groups, example-instance-group-1 and
example-instance-group-2, in the
``us-central1-a`` zone.

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the instance groups to delete.

**FLAGS**

: **--zone**:
Zone of the instance groups to delete. If not specified and the
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
gcloud alpha compute instance-groups unmanaged delete
```

```
gcloud beta compute instance-groups unmanaged delete
```