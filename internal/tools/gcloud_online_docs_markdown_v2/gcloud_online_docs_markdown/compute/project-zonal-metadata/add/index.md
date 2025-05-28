# gcloud compute project-zonal-metadata add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add)*

**NAME**

: **gcloud compute project-zonal-metadata add - add or update project zonal metadata**

**SYNOPSIS**

: **`gcloud compute project-zonal-metadata add` `[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add#KEY)`=`VALUE`,…] `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute project-zonal-metadata add` is used to add or update
project zonal metadata for your VM instances. Project zonal metadata values
propagate to all VMs within the specified zone. Every VM has access to a
metadata server that you can use to query the configured project zonal metadata
values. To set metadata for individual instances, use `[gcloud compute
instances add-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata)`. For information about metadata, see [https://cloud.google.com/compute/docs/metadata](https://cloud.google.com/compute/docs/metadata).
Only the metadata keys that you provide in the command get mutated. All other
existing metadata entries remain the same.

**EXAMPLES**

: To set the project zonal metadata with key=value in the zone
``us-central1-a`` for the project
``my-gcp-project``, run:

```
gcloud compute project-zonal-metadata add --metadata=key=value --zone=us-central1-a --project=my-gcp-project
```

For more information and examples for setting project zonal metadata, see [https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-zonal-metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-zonal-metadata)

**REQUIRED FLAGS**

: **--metadata**:
The project zonal metadata key-value pairs that you want to add or update

**--zone**:
The zone in which you want to add or update project zonal metadata

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
gcloud alpha compute project-zonal-metadata add
```

```
gcloud beta compute project-zonal-metadata add
```