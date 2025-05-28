# gcloud looker instances export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/looker/instances/export](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export)*

**NAME**

: **gcloud looker instances export - export a Looker instance**

**SYNOPSIS**

: **`gcloud looker instances export` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export#--region)`=`REGION`) `[--kms-key](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export#--kms-key)`=`KMS_KEY` `[--target-gcs-uri](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export#--target-gcs-uri)`=`TARGET_GCS_URI` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/looker/instances/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The instance specified does not exist.
- The active account does not have permission to access the given instance.
- The Google Cloud Storage bucket does not exist.

**EXAMPLES**

: To export an instance with the name `my-looker-instance` in the
default region, run:

```
gcloud looker instances export my-looker-instance --target-gcs-uri='gs://bucketName/folderName' --kms-key='projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key'
```

Note that the kms-key flag should be the full name of the kms key.

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Looker instance you
want to export. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**--region**:
The region of the instance.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--kms-key**

**--target-gcs-uri**

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
gcloud alpha looker instances export
```