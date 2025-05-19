# gcloud compute images export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/images/export](https://cloud.google.com/sdk/gcloud/reference/compute/images/export)*

**NAME**

: **gcloud compute images export - export a Compute Engine image**

**SYNOPSIS**

: **`gcloud compute images export` `[--destination-uri](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--destination-uri)`=`DESTINATION_URI` (`[--image](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--image)`=`IMAGE`     | `[--image-family](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--image-family)`=`IMAGE_FAMILY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--async)`] [`[--cloudbuild-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--cloudbuild-service-account)`=`CLOUDBUILD_SERVICE_ACCOUNT`] [`[--compute-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--compute-service-account)`=`COMPUTE_SERVICE_ACCOUNT`] [`[--export-format](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--export-format)`=`EXPORT_FORMAT`] [`[--image-project](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--image-project)`=`IMAGE_PROJECT`] [`[--log-location](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--log-location)`=`LOG_LOCATION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--network)`=`NETWORK`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--subnet)`=`SUBNET`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--timeout)`=`TIMEOUT`; default="2h"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/images/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute images export` exports virtual disk images from
Compute Engine.
By default, images are exported in the Compute Engine format, which is a
`disk.raw` file that is tarred and gzipped.
The `--export-format` flag exports the image to a format supported by
QEMU using qemu-img. Valid formats include `vmdk`, `vhdx`,
`vpc`, `vdi`, and `qcow2`.
Before exporting an image, set up access to Cloud Storage and grant required
roles to the user accounts and service accounts. For more information, see [https://cloud.google.com/compute/docs/import/requirements-export-import-images](https://cloud.google.com/compute/docs/import/requirements-export-import-images).

**EXAMPLES**

: To export a VMDK file ``my-image`` from a
project ``my-project`` to a Cloud Storage
bucket ``my-bucket``, run:

```
gcloud compute images export --image=my-image --destination-uri=gs://my-bucket/my-image.vmdk --export-format=vmdk --project=my-project
```

**REQUIRED FLAGS**

: **--destination-uri**:
The Cloud Storage URI destination for the exported virtual disk file.

**--image**

**OPTIONAL FLAGS**

: **--async**:
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
export. Image export tooling on this temporary instance must be authenticated.
A Compute Engine service account is an identity attached to an instance. Its
access tokens can be accessed through the instance metadata server and can be
used to authenticate image export tooling on the instance.
To set this option, specify the email address corresponding to the required
Compute Engine service account. If not provided, the image export on the
temporary instance uses the project's default Compute Engine service account.
At a minimum, you need to grant the following roles to the specified Cloud Build
service account:

- roles/compute.storageAdmin
- roles/storage.objectAdmin

**--export-format**:
Specify the format to export to, such as `vmdk`, `vhdx`,
`vpc`, or `qcow2`.

**--image-project**:
The Google Cloud project against which all image and image family references
will be resolved. It is best practice to define image-project. A full list of
available projects can be generated by running `[gcloud projects list](https://cloud.google.com/sdk/gcloud/reference/projects/list)`.

- If specifying one of our public images, image-project must be provided.
- If there are several of the same image-family value in multiple projects,
image-project must be specified to clarify the image to be used.
- If not specified and either image or image-family is provided, the current
default project is used.

**--log-location**:
Directory in Cloud Storage to hold build logs. If not set,
`gs://<project num>.cloudbuild-logs.googleusercontent.com/` is
created and used.

**--network**:
The name of the network in your project to use for the image export. When you
export an image, the export tool creates and uses temporary VMs in your project
for the export process. Use this flag to specify the network to use for these
temporary VMs.

**--subnet**:
Name of the subnetwork in your project to use for the image export. When you
export an image, the export tool creates and uses temporary VMs in your project
for the export process. Use this flag to specify the subnetwork to use for these
temporary VMs.

- If the network resource is in legacy mode, do not provide this property.
- If the network is in auto subnet mode, specifying the subnetwork is optional.
- If the network is in custom subnet mode, then this field must be specified.

**--timeout**:
Maximum time an export can last before it fails as "TIMEOUT". For example, if
you specify `2h`, the process fails after 2 hours. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information about duration formats.
This timeout option has a maximum value of 24 hours.
If you are exporting a large image that takes longer than 24 hours to export,
either use the RAW disk format to reduce the time needed for converting the
image, or split the data into several smaller images.

**--zone**:
The zone to use when exporting the image. When you export an image, the export
tool creates and uses temporary VMs in your project for the export process. Use
this flag to specify the zone to use for these temporary VMs. Overrides the
default `compute/zone` property value for this command invocation.

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
gcloud alpha compute images export
```

```
gcloud beta compute images export
```