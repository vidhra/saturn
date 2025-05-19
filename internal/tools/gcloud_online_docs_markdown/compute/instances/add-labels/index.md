# gcloud compute instances add-labels  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels)*

**NAME**

: **gcloud compute instances add-labels - add labels to Google Compute Engine virtual machine instances**

**SYNOPSIS**

: **`gcloud compute instances add-labels` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels#INSTANCE_NAME)` `[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels#--labels)`=[`KEY`=`VALUE`,…] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-labels#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances add-labels` adds labels to a Google Compute
Engine virtual machine instance.

**EXAMPLES**

: To add key-value pairs
``k0``=``v0``
and
``k1``=``v1``
to 'example-instance'

```
gcloud compute instances add-labels example-instance --labels=k0=v0,k1=v1
```

Labels can be used to identify the instance and to filter them. To find a
instance labeled with key-value pair ``k1``,
``v2``

```
gcloud compute instances list --filter='labels.k1:v2'
```

To list only the labels when describing a resource, use --format

```
gcloud compute instances describe example-instance --format='default(labels)'
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--labels**:
A list of labels to add.

**OPTIONAL FLAGS**

: **--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
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
gcloud alpha compute instances add-labels
```

```
gcloud beta compute instances add-labels
```