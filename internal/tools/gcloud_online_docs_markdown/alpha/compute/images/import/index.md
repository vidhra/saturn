# gcloud alpha compute images import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import)*

**NAME**

: **gcloud alpha compute images import - import an image into Compute Engine**

**SYNOPSIS**

: **`gcloud alpha compute images import` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#IMAGE_NAME)` (`[--source-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--source-file)`=`SOURCE_FILE`     | `[--source-image](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--source-image)`=`SOURCE_IMAGE`     | `[--aws-access-key-id](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-access-key-id)`=`AWS_ACCESS_KEY_ID` `[--aws-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-region)`=`AWS_REGION` `[--aws-secret-access-key](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-secret-access-key)`=`AWS_SECRET_ACCESS_KEY` `[--aws-session-token](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-session-token)`=`AWS_SESSION_TOKEN` (`[--aws-source-ami-file-path](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-source-ami-file-path)`=`AWS_SOURCE_AMI_FILE_PATH` | `[--aws-ami-export-location](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-ami-export-location)`=`AWS_AMI_EXPORT_LOCATION` `[--aws-ami-id](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--aws-ami-id)`=`AWS_AMI_ID`)) [`[--no-address](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--address)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--async)`] [`[--cloudbuild-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--cloudbuild-service-account)`=`CLOUDBUILD_SERVICE_ACCOUNT`] [`[--compute-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--compute-service-account)`=`COMPUTE_SERVICE_ACCOUNT`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--description)`=`DESCRIPTION`] [`[--family](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--family)`=`FAMILY`] [`[--no-guest-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--guest-environment)`] [`[--guest-os-features](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--guest-os-features)`=[`GUEST_OS_FEATURE`,…]] [`[--log-location](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--log-location)`=`LOG_LOCATION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--network)`=`NETWORK`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--storage-location)`=`STORAGE_LOCATION`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--subnet)`=`SUBNET`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--timeout)`=`TIMEOUT`; default="2h"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--zone)`=`ZONE`] [`[--data-disk](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--data-disk)`     | `[--byol](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--byol)` `[--os](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#--os)`=`OS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `(DEPRECATED)` This command is being deprecated.
Instead, use the `[gcloud migration vms
image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/image-imports)` command. For more information, see [https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import](https://cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import).
`gcloud alpha compute images import` imports Virtual Disk images,
such as VMWare VMDK files and VHD files, into Compute Engine.
Importing images involves four steps:

- Upload the virtual disk file to Cloud Storage.
- Import the image to Compute Engine.
- Detect the OS and bootloader contained on the disk.
- Translate the image to make a bootable image. This command performs all four of
these steps as required, depending on the input arguments specified.

Before importing an image, set up access to Cloud Storage and grant required
roles to the user accounts and service accounts. For more information, see [https://cloud.google.com/compute/docs/import/requirements-export-import-images](https://cloud.google.com/compute/docs/import/requirements-export-import-images).
To override the detected OS, specify the `--os` flag. You can omit
the translation step using the `--data-disk` flag.
If you exported your disk from Compute Engine then you don't need to re-import
it. Instead, use `[gcloud alpha compute
images create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/images/create)` to create more images from the disk.
Files stored on Cloud Storage and images in Compute Engine incur charges. See [https://cloud.google.com/compute/docs/images/importing-virtual-disks#resource_cleanup](https://cloud.google.com/compute/docs/images/importing-virtual-disks#resource_cleanup).
Troubleshooting: Image import/export tools rely on CloudBuild default behavior.
They has been using the default CloudBuild service account in order to
import/export images to/from Google Cloud Platform. However, Cloud Build has
changed this default behavior and in new projects a custom user managed service
account may need to be provided to perform the builds. If you get a CloudBuild
service account related error, run gcloud with
--cloudbuild-service-account=<custom service account>. See `gcloud
compute images import --help` for details.

**EXAMPLES**

: To import a centos-7 VMDK file, run:

```
gcloud alpha compute images import myimage-name --os=centos-7 --source-file=mysourcefile
```

To import a data disk without operating system, run:

```
gcloud alpha compute images import myimage-name --data-disk --source-file=mysourcefile
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to create.

**REQUIRED FLAGS**

: **--source-file**

**OPTIONAL FLAGS**

: **--no-address**:
Temporary VMs are created in your project during image import. Set this flag so
that these temporary VMs are not assigned external IP addresses.
Note: The image import process requires package managers to be installed on the
operating system for the virtual disk. These package managers might need to make
requests to package repositories that are outside Google Cloud. To allow access
for these updates, you need to configure Cloud NAT and Private Google Access.
For more information, see [https://cloud.google.com/compute/docs/import/importing-virtual-disks#no-external-ip](https://cloud.google.com/compute/docs/import/importing-virtual-disks#no-external-ip).

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cloudbuild-service-account**:
Image import and export tools use Cloud Build to import and export images to and
from your project. Cloud Build uses a specific service account to execute builds
on your behalf. The Cloud Build service account generates an access token for
other service accounts and it is also used for authentication when building the
artifacts for the image import tool.
Use this flag to to specify a user-managed service account for image import and
export. If you don't specify this flag, Cloud Build runs using your project's
default Cloud Build service account. To set this option, specify the email
address of the desired user-managed service account. Note: You must specify the
`--logs-location` flag when you set a user-managed service account.
At minimum, the specified user-managed service account needs to have the
following roles assigned:

- roles/compute.admin
- roles/iam.serviceAccountTokenCreator
- roles/iam.serviceAccountUser

**--compute-service-account**:
A temporary virtual machine instance is created in your project during image
import. Image import tooling on this temporary instance must be authenticated.
A Compute Engine service account is an identity attached to an instance. Its
access tokens can be accessed through the instance metadata server and can be
used to authenticate image import tooling on the instance.
To set this option, specify the email address corresponding to the required
Compute Engine service account. If not provided, the image import on the
temporary instance uses the project's default Compute Engine service account.
At a minimum, you need to grant the following roles to the specified Cloud Build
service account:

- roles/compute.storageAdmin
- roles/storage.objectViewer

**--description**:
Description to set for the imported image.

**--family**:
Family to set for the imported image.

**--guest-environment**:
Installs the guest environment on the image. See [https://cloud.google.com/compute/docs/images/guest-environment](https://cloud.google.com/compute/docs/images/guest-environment).
Enabled by default, use `--no-guest-environment` to disable.

**--guest-os-features**:
Enables one or more features for VM instances that use the image for their boot
disks. See the descriptions of supported features at: [https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).
`GUEST_OS_FEATURE` must be (only one value is supported):
`UEFI_COMPATIBLE`.

**--log-location**:
Directory in Cloud Storage to hold build logs. If not set,
`gs://<project num>.cloudbuild-logs.googleusercontent.com/` is
created and used.

**--network**:
Name of the network in your project to use for the image import. When you import
an image, the import tool creates and uses temporary VMs in your project for the
import process. Use this flag to specify the network to use for these temporary
VMs.

**--storage-location**:
Specifies a Cloud Storage location, either regional or multi-regional, where
image content is to be stored. If not specified, the multi-region location
closest to the source is chosen automatically.

**--subnet**:
Name of the subnetwork in your project to use for the image import. When you
import an image, the import tool creates and uses temporary VMs in your project
for the import process. Use this flag to specify the subnetwork to use for these
temporary VMs.

- If the network resource is in legacy mode, do not provide this property.
- If the network is in auto subnet mode, specifying the subnetwork is optional.
- If the network is in custom subnet mode, then this field must be specified.

**--timeout**:
Maximum time an import can last before it fails as "TIMEOUT". For example, if
you specify `2h`, the process fails after 2 hours. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information about duration formats.
This timeout option has a maximum value of 24 hours.
If you are importing a large image that takes longer than 24 hours to import,
either use the RAW disk format to reduce the time needed for converting the
image, or split the data into several smaller images.

**--zone**:
Zone to use when importing the image. When you import an image, the import tool
creates and uses temporary VMs in your project for the import process. Use this
flag to specify the zone to use for these temporary VMs. Overrides the default
`compute/zone` property value for this command invocation.

**--data-disk**

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
allowlist. These variants are also available:

```
gcloud compute images import
```

```
gcloud beta compute images import
```