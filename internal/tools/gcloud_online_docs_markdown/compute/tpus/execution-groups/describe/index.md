# gcloud compute tpus execution-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups/describe](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups/describe)*

**NAME**

: **gcloud compute tpus execution-groups describe - describe Google Compute TPU + VM combination**

**SYNOPSIS**

: **`gcloud compute tpus execution-groups describe` `[EXECUTION_GROUP_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups/describe#EXECUTION_GROUP_NAME)` [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/tpus/execution-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To describe the TPU and VM combination, run:

```
gcloud compute tpus execution-groups describe test-execution-group --zone=test-zone --project=test-project
```

**POSITIONAL ARGUMENTS**

: **`EXECUTION_GROUP_NAME`**:
The execution group name to delete.

**FLAGS**

: **--zone**:
Zone of the tpu to describe. If not specified and the
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
gcloud alpha compute tpus execution-groups describe
```

```
gcloud beta compute tpus execution-groups describe
```