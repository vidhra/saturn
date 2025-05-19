# gcloud colab runtime-templates create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create)*

**NAME**

: **gcloud colab runtime-templates create - create a runtime template**

**SYNOPSIS**

: **`gcloud colab runtime-templates create` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--display-name)`=`DISPLAY_NAME` [`[--async](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--region)`=`REGION`] [`[--runtime-template-id](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--runtime-template-id)`=`RUNTIME_TEMPLATE_ID`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--description)`=`DESCRIPTION` `[--no-enable-euc](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--enable-euc)` `[--enable-secure-boot](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--enable-secure-boot)` `[--idle-shutdown-timeout](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--idle-shutdown-timeout)`=`IDLE_SHUTDOWN_TIMEOUT`; default="3h" `[--labels](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--labels)`=[`KEY`=`VALUE`,…] `[--network-tags](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--network-tags)`=[`TAGS`,…] `[--accelerator-count](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--accelerator-count)`=`ACCELERATOR_COUNT` `[--accelerator-type](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--accelerator-type)`=`ACCELERATOR_TYPE` `[--machine-type](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--machine-type)`=`MACHINE_TYPE`; default="e2-standard-4" `[--disk-size-gb](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--disk-size-gb)`=`DISK_SIZE_GB`; default=100 `[--disk-type](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--disk-type)`=`DISK_TYPE`; default=`"PD_STANDARD"` [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--kms-project)`=`KMS_PROJECT`] `[--no-enable-internet-access](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--enable-internet-access)` `[--network](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--network)`=`NETWORK` [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--subnetwork)`=`SUBNETWORK` : `[--subnetwork-region](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--subnetwork-region)`=`SUBNETWORK_REGION`] `[--post-startup-script](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--post-startup-script)`=`POST_STARTUP_SCRIPT` `[--post-startup-script-behavior](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--post-startup-script-behavior)`=`POST_STARTUP_SCRIPT_BEHAVIOR` `[--post-startup-script-url](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--post-startup-script-url)`=`POST_STARTUP_SCRIPT_URL` `[--set-env-vars](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#--set-env-vars)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Colab Enterprise runtime template, a VM configuration for your notebook
runtimes.

**EXAMPLES**

: To create a runtime template in region 'us-central1' with the display name
'my-runtime-template', run:

```
gcloud colab runtime-templates create --region=us-central1 --display-name=my-runtime-template
```

To create a runtime template for a VM with machine type n1-standard-2 and one
NVIDIA_TESLA_V100 accelerator, run:

```
gcloud colab runtime-templates create --machine-type=n1-standard-2 --accelerator-type=NVIDIA_TESLA_V100 --accelerator-count=1 --region=us-central1 --display-name=my-runtime-template
```

To create a runtime template that disables end user credential access, run:

```
gcloud colab runtime-templates create --no-enable-euc --region=us-central1 --display-name=my-runtime-template
```

**REQUIRED FLAGS**

: **--display-name**:
The display name of the runtime template.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Region resource - Cloud region to create runtime template. Please see [https://cloud.google.com/colab/docs/locations](https://cloud.google.com/colab/docs/locations)
for a list of supported regions. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--region` on the command line with a fully
specified name;
- set the property `colab/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--region**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `--region` on the command line;
- set the property `colab/region`.**

**--runtime-template-id**:
The id of the runtime template. If not specified, a random id will be generated.

**--description**

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

: This variant is also available:

```
gcloud beta colab runtime-templates create
```