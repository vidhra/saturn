# gcloud compute images create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/images/create](https://cloud.google.com/sdk/gcloud/reference/compute/images/create)*

**NAME**

: **gcloud compute images create - create Compute Engine images**

**SYNOPSIS**

: **`gcloud compute images create` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#IMAGE_NAME)` (`[--source-disk](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-disk)`=`SOURCE_DISK`     | `[--source-image](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-image)`=`SOURCE_IMAGE`     | `[--source-image-family](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-image-family)`=`SOURCE_IMAGE_FAMILY`     | `[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-snapshot)`=`SOURCE_SNAPSHOT`     | `[--source-uri](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-uri)`=`SOURCE_URI`) [`[--architecture](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--architecture)`=`ARCHITECTURE`] [`[--csek-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--csek-key-file)`=`FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--description)`=`DESCRIPTION`] [`[--family](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--family)`=`FAMILY`] [`[--forbidden-database-file](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--forbidden-database-file)`=[`DBX_VALUE`,…]] [`[--force](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--force)`] [`[--guest-os-features](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--guest-os-features)`=[`GUEST_OS_FEATURE`,…]] [`[--key-exchange-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--key-exchange-key-file)`=[`KEK_VALUE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--licenses](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--licenses)`=[`LICENSES`,…]] [`[--platform-key-file](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--platform-key-file)`=`PLATFORM_KEY_FILE`] [`[--no-require-csek-key-create](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--require-csek-key-create)`] [`[--signature-database-file](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--signature-database-file)`=[`DB_VALUE`,…]] [`[--source-disk-project](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-disk-project)`=`SOURCE_DISK_PROJECT`] [`[--source-disk-zone](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-disk-zone)`=`SOURCE_DISK_ZONE`] [`[--source-image-project](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--source-image-project)`=`SOURCE_IMAGE_PROJECT`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--storage-location)`=`LOCATION`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/images/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute images create` is used to create custom disk images.
The resulting image can be provided during instance or disk creation so that the
instance attached to the resulting disks has access to a known set of software
or files from the image.
Images can be created from gzipped compressed tarball containing raw disk data,
existing disks in any zone, existing images, and existing snapshots inside the
same project.
Images are global resources, so they can be used across zones and projects.
To learn more about creating image tarballs, visit [https://cloud.google.com/compute/docs/creating-custom-image](https://cloud.google.com/compute/docs/creating-custom-image).

**EXAMPLES**

: To create an image 'my-image' from a disk 'my-disk' in zone 'us-east1-a', run:

```
gcloud compute images create my-image --source-disk=my-disk --source-disk-zone=us-east1-a
```

To create an image 'my-image' from a disk 'my-disk' in zone 'us-east1-a' with
source disk project 'source-disk-project' run:

```
gcloud compute images create my-image --source-disk=my-disk --source-disk-zone=us-east1-a --source-disk-project=source-disk-project
```

To create an image 'my-image' from another image 'source-image' with source
image project 'source-image-project', run:

```
gcloud compute images create my-image --source-image=source-image --source-image-project=source-image-project
```

To create an image 'my-image' from the latest non-deprecated image in the family
'source-image-family' with source image project 'source-image-project', run:

```
gcloud compute images create my-image --source-image-family=source-image-family --source-image-project=source-image-project
```

To create an image 'my-image' from a snapshot 'source-snapshot', run:

```
gcloud compute images create my-image --source-snapshot=source-snapshot
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
Name of the disk image to create.

**REQUIRED FLAGS**

: **--source-disk**

**OPTIONAL FLAGS**

: **--architecture**:
Specifies the architecture or processor type that this image can support. For
available processor types on Compute Engine, see [https://cloud.google.com/compute/docs/cpu-platforms](https://cloud.google.com/compute/docs/cpu-platforms).
`ARCHITECTURE` must be one of: `ARM64`,
`X86_64`.

**--csek-key-file**:
Path to a Customer-Supplied Encryption Key (CSEK) key file that maps Compute
Engine images to user managed keys to be used when creating, mounting, or taking
snapshots of disks.
If you pass `-` as value of the flag, the CSEK is read from stdin.
See [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details.

**--description**:
An optional, textual description for the image being created.

**--family**:
The family of the image. When creating an instance or disk, specifying a family
will cause the latest non-deprecated image in the family to be used.

**--forbidden-database-file**:
Comma-separated list of file paths that point to revoked X.509 certificates in
DER format or raw binary files. When you create a Shielded VM instance from this
image, these certificates or files are added to the forbidden signature database
(dbx).

**--force**:
By default, image creation fails when it is created from a disk that is attached
to a running instance. When this flag is used, image creation from disk will
proceed even if the disk is in use.

**--guest-os-features**:
Enables one or more features for VM instances that use the image for their boot
disks. See the descriptions of supported features at: [https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).
`GUEST_OS_FEATURE` must be one of:
`BARE_METAL_LINUX_COMPATIBLE`, `GVNIC`, `IDPF`,
`MULTI_IP_SUBNET`, `SEV_CAPABLE`,
`SEV_LIVE_MIGRATABLE`, `SEV_LIVE_MIGRATABLE_V2`,
`SEV_SNP_CAPABLE`, `SNP_SVSM_CAPABLE`,
`TDX_CAPABLE`, `UEFI_COMPATIBLE`,
`VIRTIO_SCSI_MULTIQUEUE`, `WINDOWS`.

**--key-exchange-key-file**:
Comma-separated list of file paths that point to X.509 certificates in DER
format or raw binary files. When you create a Shielded VM instance from this
image, these certificates or files are used as key exchange keys (KEK).

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--licenses**:
Comma-separated list of URIs to license resources.

**--platform-key-file**:
File path that points to an X.509 certificate in DER format or raw binary file.
When you create a Shielded VM instance from this image, this certificate or raw
binary file is used as the platform key (PK).

**--require-csek-key-create**:
Refuse to create images not protected by a user managed key in the key file when
--csek-key-file is given. This behavior is enabled by default to prevent
incorrect gcloud invocations from accidentally creating images with no user
managed key. Disabling the check allows creation of some images without a
matching Customer-Supplied Encryption Key in the supplied --csek-key-file. See
[https://cloud.google.com/compute/docs/disks/customer-supplied-encryption](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
for more details. Enabled by default, use
`--no-require-csek-key-create` to disable.

**--signature-database-file**:
Comma-separated list of file paths that point to valid X.509 certificates in DER
format or raw binary files. When you create a Shielded VM instance from this
image, these certificates or files are added to the signature database (db).

**--source-disk-project**:
Project name of the source disk. Must also specify --source-disk when using this
flag.

**--source-disk-zone**:
Zone of the source disk to operate on. If not specified and the
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

**--source-image-project**:
The project name of the source image. Must also specify either
``--source-image`` or
``--source-image-family`` when using this flag.

**--storage-location**:
Specifies a Cloud Storage location, either regional or multi-regional, where
image content is to be stored. If not specified, the multi-region location
closest to the source is chosen automatically.

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
gcloud alpha compute images create
```

```
gcloud beta compute images create
```