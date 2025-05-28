# gcloud workbench instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create)*

**NAME**

: **gcloud workbench instances create - creates a workbench instance**

**SYNOPSIS**

: **`gcloud workbench instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--async)`] [`[--disable-proxy-access](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--disable-proxy-access)`] [`[--enable-third-party-identity](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--enable-third-party-identity)`] [`[--instance-owners](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--instance-owners)`=`INSTANCE_OWNERS`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--confidential-compute-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--confidential-compute-type)`=`CONFIDENTIAL_COMPUTE_TYPE` `[--disable-public-ip](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--disable-public-ip)` `[--enable-ip-forwarding](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--enable-ip-forwarding)` `[--machine-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--machine-type)`=`MACHINE_TYPE`; default="n1-standard-4" `[--metadata](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--metadata)`=[`KEY`=`VALUE`,…] `[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--min-cpu-platform)`=`MIN_CPU_PLATFORM` `[--service-account-email](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--service-account-email)`=`SERVICE_ACCOUNT_EMAIL` `[--tags](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--tags)`=[`TAGS`,…] `[--accelerator-core-count](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--accelerator-core-count)`=`ACCELERATOR_CORE_COUNT` `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--accelerator-type)`=`ACCELERATOR_TYPE` `[--boot-disk-encryption](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-encryption)`=`BOOT_DISK_ENCRYPTION` `[--boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-size)`=`BOOT_DISK_SIZE` `[--boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-type)`=`BOOT_DISK_TYPE` [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY` : `[--boot-disk-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-encryption-key-keyring)`=`BOOT_DISK_ENCRYPTION_KEY_KEYRING` `[--boot-disk-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-encryption-key-location)`=`BOOT_DISK_ENCRYPTION_KEY_LOCATION` `[--boot-disk-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--boot-disk-encryption-key-project)`=`BOOT_DISK_ENCRYPTION_KEY_PROJECT`] [`[--container-repository](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--container-repository)`=`CONTAINER_REPOSITORY` : `[--container-tag](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--container-tag)`=`CONTAINER_TAG`]     | [(`[--vm-image-family](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--vm-image-family)`=`VM_IMAGE_FAMILY` | `[--vm-image-name](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--vm-image-name)`=`VM_IMAGE_NAME`) : `[--vm-image-project](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--vm-image-project)`=`VM_IMAGE_PROJECT`; default="deeplearning-platform-release"] `[--custom-gpu-driver-path](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--custom-gpu-driver-path)`=`CUSTOM_GPU_DRIVER_PATH` `[--install-gpu-driver](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--install-gpu-driver)` `[--data-disk-encryption](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-encryption)`=`DATA_DISK_ENCRYPTION` `[--data-disk-size](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-size)`=`DATA_DISK_SIZE` `[--data-disk-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-type)`=`DATA_DISK_TYPE` [`[--data-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-kms-key)`=`DATA_DISK_KMS_KEY` : `[--data-disk-encryption-key-keyring](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-encryption-key-keyring)`=`DATA_DISK_ENCRYPTION_KEY_KEYRING` `[--data-disk-encryption-key-location](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-encryption-key-location)`=`DATA_DISK_ENCRYPTION_KEY_LOCATION` `[--data-disk-encryption-key-project](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--data-disk-encryption-key-project)`=`DATA_DISK_ENCRYPTION_KEY_PROJECT`] `[--network](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--network)`=`NETWORK` `[--nic-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--nic-type)`=`NIC_TYPE` [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--subnet)`=`SUBNET` : `[--subnet-region](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--subnet-region)`=`SUBNET_REGION`] `[--reservation-key](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--reservation-key)`=`RESERVATION_KEY` `[--reservation-type](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--reservation-type)`=`RESERVATION_TYPE`; default="any" `[--reservation-values](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--reservation-values)`=[`VALUES`,…] `[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--shielded-integrity-monitoring)`=`SHIELDED_INTEGRITY_MONITORING` `[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--shielded-secure-boot)`=`SHIELDED_SECURE_BOOT` `[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#--shielded-vtpm)`=`SHIELDED_VTPM`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workbench/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a workbench instance.

**EXAMPLES**

: To create an instance from a VmImage family, run:

```
gcloud workbench instances create example-instance --vm-image-project=cloud-notebooks-managed --vm-image-family=workbench-instances --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance from a VmImage name, run:

```
gcloud workbench instances create example-instance --vm-image-project=cloud-notebooks-managed --vm-image-name=workbench-instances-v20230925-debian-11-py310 --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance from a Container Repository, run:

```
gcloud workbench instances create example-instance --container-repository=gcr.io/deeplearning-platform-release/base-cpu --container-tag=latest --machine-type=n1-standard-4 --location=us-central1-b
```

To create an instance with shielded-secure-boot, shielded-vtpm and
shielded-integrity-monitoring disabled, run:

```
gcloud workbench instances create example-instance --shielded-integrity-monitoring=false --shielded-secure-boot=false --shielded-vtpm=false --location=us-central1-b
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

**--disable-proxy-access**:
If true, the notebook instance will not register with the proxy.

**--enable-third-party-identity**:
If true, the notebook instance provide a proxy endpoint which allows for third
party identity.

**--instance-owners**:
The owners of this instance after creation. Format:
`alias@example.com`. Currently supports one owner only. If not
specified, all of the service account users of the VM instance's service account
can use the instance.

**--labels**:
Labels to apply to this instance. These can be later modified by the setLabels
method.

**--confidential-compute-type**

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