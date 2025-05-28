# gcloud migration vms machine-image-imports create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create)*

**NAME**

: **gcloud migration vms machine-image-imports create - import machine images to Google Compute Engine**

**SYNOPSIS**

: **`gcloud migration vms machine-image-imports create` (`[IMAGE_IMPORT_NAME](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#IMAGE_IMPORT_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--location)`=`LOCATION`) `[--source-file](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--source-file)`=`SOURCE_FILE` [`[--additional-licenses](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--additional-licenses)`=[`ADDITIONAL_LICENSES`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--description)`=`DESCRIPTION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--machine-image-name](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--machine-image-name)`=`MACHINE_IMAGE_NAME`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--machine-type)`=`MACHINE_TYPE`] [`[--network-interface](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--network-interface)`=[`network`=`NETWORK`],[`networkTier`=`NETWORKTIER`],[`subnetwork`=`SUBNETWORK`]] [`[--single-region-storage](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--single-region-storage)`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--tags)`=[`TAGS`,…]] [`[--target-project](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--target-project)`=`TARGET_PROJECT`] [`[--enable-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--enable-integrity-monitoring)` `[--enable-vtpm](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--enable-vtpm)` `[--secure-boot](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--secure-boot)`=`SECURE_BOOT`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--scopes)`=[`SCOPES`,…] `[--service-account](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--skip-os-adaptation](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--skip-os-adaptation)`     | `[--boot-conversion](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--boot-conversion)`=`BOOT_CONVERSION` `[--generalize](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--generalize)` `[--license-type](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#--license-type)`=`LICENSE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud migration vms machine-image-imports create Imports machine images such as
OVA and OVF files, from a Google Cloud Storage file (gs://…) to Google
Compute Engine, using the Migrate to Virtual Machines service API. This command
creates an Image Import resource with a nested Image Import Job resource. The
Image Import Job resource tracks the image import progress. To use this command,
you must enable VM Migration API in your project.

**EXAMPLES**

: To import ub-14.04.5.ova from my-images-bucket to my-target-project in
us-central1, create my-image-import resource in my-project in us-central1. Run:
```
gcloud migration vms machine-image-imports create my-machine-image-import --source-file=gs://my-images-bucket/ub-14.04.5.ova --image-name=my-ubuntu-machine-image --location=us-central1 --target-project=projects/my-project/locations/global/targetProjects/my-target-project --project=my-project
```

**POSITIONAL ARGUMENTS**

: **Image import resource - The Image Import resource you want to create. This would
be the machine image name if --machine-image-name is not given. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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
Comma-separated list of the additional licenses to assign to the machine image.

**--description**:
A description of the machine image.

**--kms-key**:
Fully qualified identifier for the Cloud KMS (Key Management Service) cryptokey
that will be used to protect the image.

**--labels**:
A map of labels to associate with the machine image.

**--machine-image-name**:
The name of the machine image that will be imported to Google Compute Engine.
Default is the Image Import name.

**--machine-type**:
The machine type to create the machine image with. If not provided, the service
will choose a relevant machine type series based on the information from the
source image.

**--network-interface**:
The network interface to use for the instance created by the machine image. This
is a dicionary with the following keys:

- network: The network to use for this network interface.
- subnetwork: The subnetwork to use for this network interface.
- network-tier: The network tier to use for this network interface. This argument
can be specified multiple times in case of multiple nics.

**--single-region-storage**:
If true, the location of the imported machine image will be the region of the
import job. Otherwise the closest multi-region is selected. Default is false.

**--tags**:
The tags to apply to the instance created by the machine image.

**--target-project**:
The target project resource path to which the machine image will be imported.
Default is the host project. To get a list of the target projects run the gcloud
alpha migration vms target-projects list command.

**--enable-integrity-monitoring**

**--scopes**

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
gcloud alpha migration vms machine-image-imports create
```