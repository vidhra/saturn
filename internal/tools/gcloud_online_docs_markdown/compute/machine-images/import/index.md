# gcloud compute machine-images import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import)*

**NAME**

: **gcloud compute machine-images import - create a Compute Engine machine image from virtual appliance in OVA/OVF format**

**SYNOPSIS**

: **`gcloud compute machine-images import` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#IMAGE)` `[--source-uri](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--source-uri)`=`SOURCE_URI` [`[--no-address](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--address)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--async)`] [`[--byol](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--byol)`] [`[--can-ip-forward](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--can-ip-forward)`] [`[--cloudbuild-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--cloudbuild-service-account)`=`CLOUDBUILD_SERVICE_ACCOUNT`] [`[--compute-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--compute-service-account)`=`COMPUTE_SERVICE_ACCOUNT`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--description)`=`DESCRIPTION`] [`[--no-guest-environment](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--guest-environment)`] [`[--guest-flush](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--guest-flush)`] [`[--guest-os-features](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--guest-os-features)`=[`GUEST_OS_FEATURE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--labels)`=[`KEY`=`VALUE`,…]] [`[--log-location](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--log-location)`=`LOG_LOCATION`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--machine-type)`=`MACHINE_TYPE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--network)`=`NETWORK`] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--network-tier)`=`NETWORK_TIER`] [`[--os](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--os)`=`OS`] [`[--no-restart-on-failure](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--restart-on-failure)`] [`[--storage-location](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--storage-location)`=`LOCATION`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--subnet)`=`SUBNET`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#TAG)`,…]] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--timeout)`=`TIMEOUT`; default="2h"] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--zone)`=`ZONE`] [`[--custom-cpu](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--custom-cpu)`=`CUSTOM_CPU` `[--custom-memory](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--custom-memory)`=`CUSTOM_MEMORY` : `[--custom-extensions](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--custom-extensions)` `[--custom-vm-type](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--custom-vm-type)`=`CUSTOM_VM_TYPE`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--scopes)`=[`SCOPE`,…]     | `[--no-scopes](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--scopes)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--service-account)`=`SERVICE_ACCOUNT`     | `[--no-service-account](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#--service-account)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is being deprecated. Instead, use the
`[gcloud
migration vms machine-image-imports](https://cloud.google.com/sdk/gcloud/reference/migration/vms/machine-image-imports)` command. For more information,
See "gcloud alpha migration vms machine-image-imports --help".
`gcloud compute machine-images import` creates Compute Engine machine
image from virtual appliance in OVA/OVF format.
Importing OVF involves:

- Unpacking OVF package (if in OVA format) to Cloud Storage.
- Import disks from OVF to Compute Engine.
- Translate the boot disk to make it bootable in Compute Engine.
- Create a machine image using OVF metadata and imported disks.

Virtual instances, images, machine images, and disks in Compute engine and files
stored on Cloud Storage incur charges. See [https://cloud.google.com/compute/docs/images/importing-virtual-disks#resource_cleanup](https://cloud.google.com/compute/docs/images/importing-virtual-disks#resource_cleanup).

**EXAMPLES**

: To import an OVF package from Cloud Storage into a machine image named
`my-machine-image`, run:

```
gcloud compute machine-images import my-machine-image --source-uri=gs://my-bucket/my-dir
```

**POSITIONAL ARGUMENTS**

: **`IMAGE`**:
Name of the machineImage to import.

**REQUIRED FLAGS**

: **--source-uri**:
Cloud Storage path to one of: OVF descriptor OVA file Directory with OVF
package. For more information about Cloud Storage URIs, see [https://cloud.google.com/storage/docs/request-endpoints#json-api](https://cloud.google.com/storage/docs/request-endpoints#json-api).

**OPTIONAL FLAGS**

: **--no-address**:
Temporary VMs are created in your project during machine image import. Set this
flag so that these temporary VMs are not assigned external IP addresses.
Note: The machine image import process requires package managers to be installed
on the operating system for the virtual disk. These package managers might need
to make requests to package repositories that are outside Google Cloud. To allow
access for these updates, you need to configure Cloud NAT and Private Google
Access. For more information, see [https://cloud.google.com/nat/docs/gce-example#create-nat](https://cloud.google.com/nat/docs/gce-example#create-nat)
and [https://cloud.google.com/vpc/docs/private-access-options#pga](https://cloud.google.com/vpc/docs/private-access-options#pga).

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--byol**:
Specifies that you want to import an image with an existing license. Importing
an image with an existing license is known as bring your own license (BYOL).
`--byol` can be specified in any of the following ways:

```
+ `--byol --os=rhel-8`: imports a RHEL 8 image with an existing license.
+ `--os=rhel-8-byol`: imports a RHEL 8 image with an existing license.
+ `--byol`: detects the OS contained on the disk, and imports
   the image with an existing license.
```

For more information about BYOL, see: [https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses](https://cloud.google.com/compute/docs/nodes/bringing-your-own-licenses)

**--can-ip-forward**:
If provided, allows the VMs created from the imported machine image to send and
receive packets with non-matching destination or source IP addresses.

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
A temporary virtual machine instance is created in your project during machine
image import. Machine image import tooling on this temporary instance must be
authenticated.
A Compute Engine service account is an identity attached to an instance. Its
access tokens can be accessed through the instance metadata server and can be
used to authenticate machine image import tooling on the instance.
To set this option, specify the email address corresponding to the required
Compute Engine service account. If not provided, the machine image import on the
temporary instance uses the project's default Compute Engine service account.
At a minimum, you need to grant the following roles to the specified Cloud Build
service account:

- roles/compute.storageAdmin
- roles/storage.objectViewer

**--description**:
Specifies a text description of the machine image.

**--guest-environment**:
The guest environment will be installed on the machine image. Enabled by
default, use `--no-guest-environment` to disable.

**--guest-flush**:
Create an application-consistent machine image by informing the OS to prepare
for the snapshot process.

**--guest-os-features**:
Enables one or more features for VM instances that use the image for their boot
disks. See the descriptions of supported features at: [https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features](https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).
`GUEST_OS_FEATURE` must be (only one value is supported):
`UEFI_COMPATIBLE`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--log-location**:
Directory in Cloud Storage to hold build logs. If not set,
`gs://<project num>.cloudbuild-logs.googleusercontent.com/` is
created and used.

**--machine-type**:
Specifies the machine type used for the instances. To get a list of available
machine types, run 'gcloud compute machine-types list'. If unspecified, the
default type is n1-standard-1.

**--network**:
Specifies the network for the VMs that are created from the imported machine
image. If `--subnet` is also specified, then the subnet must be a
subnetwork of network specified by `--network`. If neither is
specified, the `default` network is used.

**--network-tier**:
Specifies the network tier that will be used to configure the machine image.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.

**--os**:
Specifies the OS of the machine image being imported. `OS`
must be one of: `centos-7`, `centos-stream-8`,
`centos-stream-9`, `debian-10`, `debian-11`,
`debian-8`, `debian-9`, `opensuse-15`,
`rhel-6`, `rhel-6-byol`, `rhel-7`,
`rhel-7-byol`, `rhel-8`, `rhel-8-byol`,
`rhel-9`, `rhel-9-byol`, `rocky-8`,
`rocky-9`, `sles-12`, `sles-12-byol`,
`sles-15`, `sles-15-byol`, `sles-sap-12`,
`sles-sap-12-byol`, `sles-sap-15`,
`sles-sap-15-byol`, `ubuntu-1404`,
`ubuntu-1604`, `ubuntu-1804`, `ubuntu-2004`,
`ubuntu-2204`, `windows-10-x64-byol`,
`windows-10-x86-byol`, `windows-11-x64-byol`,
`windows-2008r2`, `windows-2008r2-byol`,
`windows-2012`, `windows-2012-byol`,
`windows-2012r2`, `windows-2012r2-byol`,
`windows-2016`, `windows-2016-byol`,
`windows-2019`, `windows-2019-byol`,
`windows-2022`, `windows-2022-byol`,
`windows-7-x64-byol`, `windows-7-x86-byol`,
`windows-8-x64-byol`, `windows-8-x86-byol`.

**--restart-on-failure**:
The VMs created from the imported machine image are restarted if they are
terminated by Compute Engine. This does not affect terminations performed by the
user. Enabled by default, use `--no-restart-on-failure` to disable.

**--storage-location**:
Google Cloud Storage location, either regional or multi-regional, where machine
image's content is to be stored. If absent, a nearby regional or multi-regional
location is chosen automatically.

**--subnet**:
Specifies the subnet for the VMs created from the imported machine image. If
`--network` is also specified, the subnet must be a subnetwork of the
network specified by `--network`.

**--tags**:
Specifies a list of tags to apply to the VMs created from the imported machine
image. These tags allow network firewall rules and routes to be applied to
specified VMs. See `[gcloud compute
firewall-rules create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)`(1) for more details.
To read more about configuring network tags, read this guide: [https://cloud.google.com/vpc/docs/add-remove-network-tags](https://cloud.google.com/vpc/docs/add-remove-network-tags)
To list VMs with their respective status and tags, run:

```
gcloud compute instances list --format='table(name,status,tags.list())'
```

To list VMs tagged with a specific tag, `tag1`, run:

```
gcloud compute instances list --filter='tags:tag1'
```

**--timeout**:
Maximum time an import can last before it fails as "TIMEOUT". For example, if
you specify `2h`, the process fails after 2 hours. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information about duration formats.
This timeout option has a maximum value of 24 hours.

**--zone**:
Zone of the machine image to import. The zone in which to perform the import of
the machine image. If not specified and the
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

**--custom-cpu**

**--scopes**

**--service-account**

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
gcloud alpha compute machine-images import
```

```
gcloud beta compute machine-images import
```