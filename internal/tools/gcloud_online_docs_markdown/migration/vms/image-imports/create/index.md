# gcloud migration vms image-imports create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create)*

**NAME**

: **gcloud migration vms image-imports create - import Virtual Disk images to Google Compute Engine**

**SYNOPSIS**

: **`gcloud migration vms image-imports create` (`[IMAGE_IMPORT_NAME](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#IMAGE_IMPORT_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--location)`=`LOCATION`) `[--source-file](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--source-file)`=`SOURCE_FILE` [`[--additional-licenses](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--additional-licenses)`=[`ADDITIONAL_LICENSES`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--description)`=`DESCRIPTION`] [`[--family-name](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--family-name)`=`FAMILY_NAME`] [`[--image-name](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--image-name)`=`IMAGE_NAME`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--single-region-storage](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--single-region-storage)`] [`[--target-project](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--target-project)`=`TARGET_PROJECT`] [`[--skip-os-adaptation](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--skip-os-adaptation)`     | `[--boot-conversion](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--boot-conversion)`=`BOOT_CONVERSION` `[--generalize](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--generalize)` `[--license-type](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#--license-type)`=`LICENSE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud migration vms image-imports create imports images such as VMWare VMDK
files and VHD files, from a Google Cloud Storage file (gs://…) to Google
Compute Engine, using the Migrate to Virtual Machines service API. This command
creates an Image Import resource with a nested Image Import Job resource. The
Image Import Job resource tracks the image import progress. To use this command,
you must enable VM Migration API in your project.

**EXAMPLES**

: To import my-ubuntu22.04.vmdk from my-images-bucket to my-target-project in
us-central1, create my-image-import resource in my-project in us-central1. Run:
```
gcloud migration vms image-imports create my-image-import --source-file=gs://my-images-bucket/my-ubuntu22.04.vmdk --image-name=my-ubuntu-image --location=us-central1 --target-project=projects/my-project/locations/global/targetProjects/my-target-project --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Image import resource - The Image Import resource you want to create. This would
be the image name if --image-name is not given. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--source-file**:
The path to the Google Cloud Storage file from which the image should be
imported.

**OPTIONAL FLAGS**

: **--additional-licenses**:
Comma-separated list of the additional licenses to assign to the image.

**--description**:
A description of the image.

**--family-name**:
The name of the image family to which the new image belongs.

**--image-name**:
The name of the image that will be imported to Google Compute Engine. Default is
the Image Import name.

**--kms-key**:
Fully qualified identifier for the Cloud KMS (Key Management Service) cryptokey
that will be used to protect the image.

**--labels**:
A map of labels to associate with the image.

**--single-region-storage**:
If true, the location of the imported image will be the region of the import
job. Otherwise the closest multi-region is selected. Default is false.

**--target-project**:
The target project resource path to which the image will be imported. Default is
the customer project. To get a list of the target projects run the gcloud alpha
migration vms target-projects list command.

**--skip-os-adaptation**

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
gcloud alpha migration vms image-imports create
```