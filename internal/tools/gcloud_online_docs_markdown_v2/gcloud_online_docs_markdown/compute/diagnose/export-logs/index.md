# gcloud compute diagnose export-logs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs)*

**NAME**

: **gcloud compute diagnose export-logs - triggers instance to gather logs and upload them to a Cloud Storage Bucket**

**SYNOPSIS**

: **`gcloud compute diagnose export-logs` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs#INSTANCE_NAME)` [`[--collect-process-traces](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs#--collect-process-traces)`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gathers logs from a running Compute Engine VM and exports them to a Google Cloud
Storage Bucket. Outputs a path to the logs within the Bucket.

**EXAMPLES**

: To export logs and upload them to a Cloud Storage Bucket, run:

```
gcloud compute diagnose export-logs example-instance --zone=us-central1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--collect-process-traces**:
Collect a 10 minute trace of the running system. On Windows, this utilizes
Windows Performance Recorder. It records CPU, disk, file, and network activity
during that time.

**--zone**:
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
gcloud alpha compute diagnose export-logs
```

```
gcloud beta compute diagnose export-logs
```