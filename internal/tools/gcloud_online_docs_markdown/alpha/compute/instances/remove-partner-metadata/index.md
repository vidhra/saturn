# gcloud alpha compute instances remove-partner-metadata  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata)*

**NAME**

: **gcloud alpha compute instances remove-partner-metadata - remove partner metadata**

**SYNOPSIS**

: **`gcloud alpha compute instances remove-partner-metadata` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#INSTANCE_NAME)` [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#--zone)`=`ZONE`] [`[--all](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#--all)`     | `[--keys](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#--keys)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#KEY)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/remove-partner-metadata#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` gcloud alpha compute instances remove-partner-metadata can
be used to remove a specific entry in a namespace, a specific namespace, or all
namespaces.

**EXAMPLES**

: To remove partner metadata specific entry in a namespace
``test.compute.googleapis.com/entries/engine``
an instance named ``INSTANCE_NAME``, run:

```
gcloud alpha compute instances remove-partner-metadata INSTANCE_NAME --keys=test.compute.googleapis.com/entries/engine
```

To remove specific namespace with its data, run:
```
gcloud alpha compute instances remove-partner-metadata INSTANCE_NAME --keys=test.compute.googleapis.com
```

To remove all namespaces, run:
```
gcloud alpha compute instances remove-partner-metadata INSTANCE_NAME --all
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to set partner metadata on. For details on valid instance
names, refer to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--zone**:
Zone of the instance to set partner metadata on. If not specified, you might be
prompted to select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
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

**--all**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta compute instances remove-partner-metadata
```