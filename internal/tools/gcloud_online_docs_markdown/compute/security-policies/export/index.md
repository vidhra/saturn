# gcloud compute security-policies export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export)*

**NAME**

: **gcloud compute security-policies export - export security policy configs into YAML or JSON files**

**SYNOPSIS**

: **`gcloud compute security-policies export` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#NAME)` `[--file-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#--file-name)`=`FILE_NAME` [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#--file-format)`=`FILE_FORMAT`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies export` exports all data associated
with Compute Engine security policy into a local file.

**EXAMPLES**

: To export a security policy in JSON format to a given file, run:

```
gcloud compute security-policies export my-policy --file-name=my-file-name --file-format=json
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to export.

**REQUIRED FLAGS**

: **--file-name**:
The name of the file to export the security policy config to.

**OPTIONAL FLAGS**

: **--file-format**:
The format of the file to export the security policy config to. Specify either
yaml or json. Defaults to yaml if not specified.
`FILE_FORMAT` must be one of: `json`,
`yaml`.

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
gcloud alpha compute security-policies export
```

```
gcloud beta compute security-policies export
```