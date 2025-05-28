# gcloud notebooks instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create)*

**NAME**

: **gcloud notebooks instances create - request for creating an instance**

**SYNOPSIS**

: **`gcloud notebooks instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--async)`] [`[--instance-owners](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--instance-owners)`=`INSTANCE_OWNERS`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--machine-type)`=`MACHINE_TYPE`; default="n1-standard-1"] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--metadata)`=[`KEY`=`VALUE`,…]] [`[--post-startup-script](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--post-startup-script)`=`POST_STARTUP_SCRIPT`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--no-shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--shielded-secure-boot)`] [`[--no-shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--shielded-vtpm)`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--tags)`=[`TAGS`,…]] [`[--accelerator-core-count](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--accelerator-core-count)`=`ACCELERATOR_CORE_COUNT` `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--accelerator-type)`=`ACCELERATOR_TYPE`] [`[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--boot-disk-size)`=`BOOT_DISK_SIZE` `[--boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--boot-disk-type)`=`BOOT_DISK_TYPE`] [[`[--container-repository](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--container-repository)`=`CONTAINER_REPOSITORY` : `[--container-tag](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--container-tag)`=`CONTAINER_TAG`]     | [`[--environment](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--environment)`=`ENVIRONMENT` : `[--environment-location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--environment-location)`=`ENVIRONMENT_LOCATION`]     | `[--vm-image-project](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--vm-image-project)`=`VM_IMAGE_PROJECT`; default="deeplearning-platform-release" `[--vm-image-family](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--vm-image-family)`=`VM_IMAGE_FAMILY`; default="common-cpu"     | `[--vm-image-name](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--vm-image-name)`=`VM_IMAGE_NAME`] [`[--custom-gpu-driver-path](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--custom-gpu-driver-path)`=`CUSTOM_GPU_DRIVER_PATH` `[--install-gpu-driver](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--install-gpu-driver)`] [`[--data-disk-size](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--data-disk-size)`=`DATA_DISK_SIZE` `[--data-disk-type](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--data-disk-type)`=`DATA_DISK_TYPE` `[--no-remove-data-disk](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--remove-data-disk)`] [`[--disk-encryption](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--disk-encryption)`=`DISK_ENCRYPTION` [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--kms-project)`=`KMS_PROJECT`]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--network)`=`NETWORK` `[--no-proxy-access](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--proxy-access)` `[--no-public-ip](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--public-ip)` [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--subnet)`=`SUBNET` : `[--subnet-region](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--subnet-region)`=`SUBNET_REGION`]] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#--reservation-affinity)`=`RESERVATION_AFFINITY`; default=`"TYPE_UNSPECIFIED"`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/notebooks/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Request for creating notebook instances.

**EXAMPLES**

: To create an instance from an environment, run:

```
gcloud notebooks instances create example-instance --environment=example-env --environment-location=us-central1-a --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance from a VmImage family, run:

```
gcloud notebooks instances create example-instance --vm-image-project=deeplearning-platform-release --vm-image-family=caffe1-latest-cpu-experimental --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance from a VmImage name, run:

```
gcloud notebooks instances create example-instance --vm-image-project=deeplearning-platform-release --vm-image-name=tf2-2-1-cu101-notebooks-20200110 --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance from a Container Repository, run:

```
gcloud notebooks instances create example-instance --container-repository=gcr.io/deeplearning-platform-release/base-cpu --container-tag=test-tag --machine-type=n1-standard-4 --location=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **Instance resource - User-defined unique name of this instance. The instance name
must be 1 to 63 characters long and contain only lowercase letters, numeric
characters, and dashes. The first character must be a lowercase letter and the
last character cannot be a dash. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location of this environment [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `notebooks/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--instance-owners**:
The owners of this instance after creation.
Format:`alias@example.com`. Currently supports one owner only.If not
specified, all of the service account users of the VM instance's service account
can use the instance.

**--labels**:
Labels to apply to this instance. These can be later modified by the setLabels
method.

**--machine-type**:
The [Compute
Engine machine type](https://cloud.google.com/sdk/gcloud/reference/compute/machine-types) of this instance.

**--metadata**:
Custom metadata to apply to this instance.
For example, to specify a Cloud Storage bucket for automatic backup, you can use
the `gcs-data-bucket` metadata tag. Format:
`"--metadata=gcs-data-bucket=``BUCKET``"`.

**--post-startup-script**:
Path to a Bash script that automatically runs after a notebook instance fully
boots up. The path must be a URL or Cloud Storage path
(gs://`path-to-file`/`file-name`).

**--service-account**:
The service account on this instance, giving access to other Google Cloud
services. You can use any service account within the same project, but you must
have the service account user permission to use the instance. If not specified,
the [Compute
Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used.

**--shielded-integrity-monitoring**:
Enable monitoring of the boot integrity of the instance. Enabled by default, use
`--no-shielded-integrity-monitoring` to disable.

**--shielded-secure-boot**:
Boot instance with secure boot enabled. Disabled by default.

**--shielded-vtpm**:
Boot instance with TPM (Trusted Platform Module) enabled. Enabled by default,
use `--no-shielded-vtpm` to disable.

**--tags**:
Tags to apply to this instance.

**--accelerator-core-count**

**--boot-disk-size**

**--container-repository**

**--custom-gpu-driver-path**

**--data-disk-size**

**--disk-encryption**

**Network configs.

**Network resource - The name of the VPC that this instance is in. Format:
projects/`{project_id}`/global/networks/`{network_id}`.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `--network` on the command line.**

**--no-proxy-access**:
If true, the notebook instance will not register with the proxy.

**--no-public-ip**:
If specified, no public IP will be assigned to this instance.

**Subnetwork resource - The name of the subnet that this instance is in. Format:
projects/`{project_id}`/regions/`{region}`/subnetworks/`{subnetwork_id}`.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--subnet` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--subnet**:
ID of the subnetwork or fully qualified identifier for the subnetwork.
To set the `subnet` attribute:

- provide the argument `--subnet` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--subnet-region**:
Google Cloud region of this subnetwork [https://cloud.google.com/compute/docs/regions-zones/#locations](https://cloud.google.com/compute/docs/regions-zones/#locations).
To set the `subnet-region` attribute:

- provide the argument `--subnet` on the command line with a fully
specified name;
- provide the argument `--subnet-region` on the command line.****

**--reservation**

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
gcloud alpha notebooks instances create
```

```
gcloud beta notebooks instances create
```