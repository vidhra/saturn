# gcloud compute addresses move  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move)*

**NAME**

: **gcloud compute addresses move - move an address to another project**

**SYNOPSIS**

: **`gcloud compute addresses move` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#NAME)` `[--target-project](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#--target-project)`=`TARGET_PROJECT` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#--description)`=`DESCRIPTION`] [`[--new-name](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#--new-name)`=`NEW_NAME`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/move#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: The following command moves address `external-ip1` in region
`us-central1` to project `test-playground` with new
address name `test-ip1`:

```
gcloud compute addresses move external-ip1 --new-name=test-ip1 --target-project=test-playground --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the address to operate on.

**REQUIRED FLAGS**

: **--target-project**:
The target project to move address to. It can be either a project name or a
project numerical ID. It must not be the same as the current project.

**OPTIONAL FLAGS**

: **--description**:
Description of moved new address.

**--new-name**:
Name of moved new address. If not specified, current address's name is used.

**--global**

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
gcloud alpha compute addresses move
```

```
gcloud beta compute addresses move
```