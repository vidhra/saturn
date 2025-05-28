# gcloud compute project-zonal-metadata remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove)*

**NAME**

: **gcloud compute project-zonal-metadata remove - remove project zonal metadata**

**SYNOPSIS**

: **`gcloud compute project-zonal-metadata remove` `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove#--zone)`=`ZONE` [`[--all](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove#--all)`     | `[--keys](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove#--keys)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove#KEY)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute project-zonal-metadata remove` is used to remove
project zonal metadata from all VMs within the specified zone. For information
about metadata, see [https://cloud.google.com/compute/docs/metadata](https://cloud.google.com/compute/docs/metadata).
Only the metadata keys that you provide in the command get removed. All other
existing metadata entries remain the same.
After you remove a specific project zonal metadata entry, if that metadata key
has any project-wide value configured, then the VMs in the zone automatically
inherit that project-wide value.

**EXAMPLES**

: To remove the project zonal metadata with key=value in the zone
``us-central1-a`` for the project
``my-gcp-project``, run:

```
gcloud compute project-zonal-metadata remove --keys=key --zone=us-central1-a --project=my-gcp-project
```

For more information and examples about how to remove project zonal metadata,
see [https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#remove-custom-project-zonal-metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata#remove-custom-project-zonal-metadata)

**REQUIRED FLAGS**

: **--zone**:
The zone in which you want to remove project zonal metadata

**OPTIONAL FLAGS**

: **--all**

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
gcloud alpha compute project-zonal-metadata remove
```

```
gcloud beta compute project-zonal-metadata remove
```