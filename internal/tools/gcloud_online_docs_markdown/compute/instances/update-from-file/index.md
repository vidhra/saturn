# gcloud compute instances update-from-file  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file)*

**NAME**

: **gcloud compute instances update-from-file - update a Compute Engine virtual machine instance using a configuration file**

**SYNOPSIS**

: **`gcloud compute instances update-from-file` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#INSTANCE_NAME)` [`[--minimal-action](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#--minimal-action)`=`MINIMAL_ACTION`] [`[--most-disruptive-allowed-action](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#--most-disruptive-allowed-action)`=`MOST_DISRUPTIVE_ALLOWED_ACTION`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#--source)`=`SOURCE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine virtual machine instance using a configuration file. For
more information, see [https://cloud.google.com/compute/docs/instances/update-instance-properties](https://cloud.google.com/compute/docs/instances/update-instance-properties).

**EXAMPLES**

: A virtual machine instance can be updated by running:

```
gcloud compute instances update-from-file my-instance --source=<path-to-file>
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to update. For details on valid instance names, refer to
the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--minimal-action**:
If specified, this action or higher level action is performed on the instance
irrespective of what action is required for the update to take effect. If not
specified, then Compute Engine acts based on the minimum action required.

**--most-disruptive-allowed-action**:
If specified, Compute Engine returns an error if the update requires a higher
action to be applied to the instance. If not specified, the default will be
REFRESH.

**--source**:
Path to a YAML file containing configuration export data. Alternatively, you may
omit this flag to read from standard input.For a schema describing the
export/import format, see:
$CLOUDSDKROOT/lib/googlecloudsdk/schemas/compute/v1/Instance.yaml.

```
Note: $CLOUDSDKROOT represents the Google Cloud CLI's installation directory.
```

**--zone**:
Zone of the instance to update. If not specified, you might be prompted to
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
gcloud alpha compute instances update-from-file
```

```
gcloud beta compute instances update-from-file
```