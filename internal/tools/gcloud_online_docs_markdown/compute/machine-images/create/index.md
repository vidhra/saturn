# gcloud compute machine-images create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create)*

**NAME**

: **gcloud compute machine-images create - create a Compute Engine machine image**

**SYNOPSIS**

: **`gcloud compute machine-images create` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#IMAGE)` `[--source-instance](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--source-instance)`=`SOURCE_INSTANCE` [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--csek-key-file)`=`FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--description)`=`DESCRIPTION`] [`[--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--guest-flush)`] [`[--no-require-csek-key-create](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--require-csek-key-create)`] [`[--source-disk-csek-key](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--source-disk-csek-key)`=[`PROPERTY`=`VALUE`,…]] [`[--source-instance-zone](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--source-instance-zone)`=`SOURCE_INSTANCE_ZONE`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--storage-location)`=`LOCATION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine machine image.

**EXAMPLES**

: To create a machine image, run:

```
gcloud compute machine-images create my-machine-image --source-instance=example-source --source-instance-zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`IMAGE`**:
Name of the machineImage to create.

**REQUIRED FLAGS**

: **--source-instance**:
The source instance to create a machine image from.

**OPTIONAL FLAGS**

: **--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine machine images to user managed keys to be used when creating, mounting,
or taking snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--description**:
Specifies a text description of the machine image.

**--guest-flush**:
Create an application-consistent machine image by informing the OS to prepare
for the snapshot process.

**--require-csek-key-create**:
Refuse to create machine images not protected by a user managed key in the key
file when --csek-key-file is given. This behavior is enabled by default to
prevent incorrect gcloud invocations from accidentally creating machine images
with no user managed key. Disabling the check allows creation of some machine
images without a matching Customer-Supplied Encryption Key in the supplied
--csek-key-file. See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details. Enabled by default, use
`--no-require-csek-key-create` to disable.

**--source-disk-csek-key**:
Customer-supplied encryption key of the disk attached to the source instance.
Required if the source disk is protected by a customer-supplied encryption key.
This flag can be repeated to specify multiple attached disks.

**`disk`**:
URL of the disk attached to the source instance. This can be a full or valid
partial URL

**`csek-key-file`**:
path to customer-supplied encryption key.

**--source-instance-zone**:
Zone of the instance to operate on. If not specified and the
``compute/zone`` property isn't set, you might
be prompted to select a zone (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
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

**--storage-location**:
Google Cloud Storage location, either regional or multi-regional, where machine
image's content is to be stored. If absent, a nearby regional or multi-regional
location is chosen automatically.

**--kms-key**

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
gcloud alpha compute machine-images create
```

```
gcloud beta compute machine-images create
```