# gcloud builds triggers import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/triggers/import](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/import)*

**NAME**

: **gcloud builds triggers import - import a build trigger**

**SYNOPSIS**

: **`gcloud builds triggers import` `[--source](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/import#--source)`=`PATH` [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/import#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To import a trigger from a file: $ cat > trigger.yaml <<EOF name:
my-trigger github: owner: GoogleCloudPlatform name: cloud-builders push: branch:
.`EOF`

**EXAMPLES**

: To import a build trigger from a file called trigger.yaml, run:

```
gcloud builds triggers import --source=trigger.yaml
```

**REQUIRED FLAGS**

: **--source**:
File path where trigger should be imported from.

**OPTIONAL FLAGS**

: **--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

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
gcloud alpha builds triggers import
```

```
gcloud beta builds triggers import
```