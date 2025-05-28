# gcloud migration vms machine-image-imports delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete)*

**NAME**

: **gcloud migration vms machine-image-imports delete - delete an Image Import resource**

**SYNOPSIS**

: **`gcloud migration vms machine-image-imports delete` (`[IMAGE_IMPORT_NAME](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete#IMAGE_IMPORT_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud migration vms machine-image-imports delete deletes an Image Import
resource. To use this command, you must enable VM Migration API in your project.
This command does not delete any machine images imported to Google Compute
Engine.

**EXAMPLES**

: To delete my-image-import resource in us-central1 in the default project, run:
```
gcloud migration vms machine-image-imports delete my-image-import --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Image import resource - The Image Import resource you want to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `image_import_name` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`IMAGE_IMPORT_NAME`**:
ID of the image_import or fully qualified identifier for the image_import.
To set the `image_import_name` attribute:

- provide the argument `image_import_name` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Resource location.
To set the `location` attribute:

- provide the argument `image_import_name` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.**

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

**API REFERENCE**

: This command uses the `vmmigration/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/migrate/virtual-machines](https://cloud.google.com/migrate/virtual-machines)

**NOTES**

: This variant is also available:

```
gcloud alpha migration vms machine-image-imports delete
```