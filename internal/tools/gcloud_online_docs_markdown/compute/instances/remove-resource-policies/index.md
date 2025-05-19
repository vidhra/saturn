# gcloud compute instances remove-resource-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies)*

**NAME**

: **gcloud compute instances remove-resource-policies - remove resource policies from Compute Engine VM instances**

**SYNOPSIS**

: **`gcloud compute instances remove-resource-policies` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies#INSTANCE_NAME)` `[--resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies#--resource-policies)`=[`RESOURCE_POLICY`,…] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/remove-resource-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances remove-resource-policies` removes resource
policies from Compute Engine virtual instances.

**EXAMPLES**

: To remove resource policy ``pol1`` from
instance ``inst1``, run this:

```
gcloud compute instances remove-resource-policies inst1 --resource-policies=pol1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to remove resource policies from. For details on valid
instance names, refer to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**REQUIRED FLAGS**

: **--resource-policies**:
A list of resource policy names to be removed from the instance. The policies
must exist in the same region as the instance.

**OPTIONAL FLAGS**

: **--zone**:
Zone of the instance to remove resource policies from. If not specified, you
might be prompted to select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
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
gcloud alpha compute instances remove-resource-policies
```

```
gcloud beta compute instances remove-resource-policies
```