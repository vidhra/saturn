# gcloud compute security-policies import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import)*

**NAME**

: **gcloud compute security-policies import - import security policy configs into your project**

**SYNOPSIS**

: **`gcloud compute security-policies import` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#NAME)` `[--file-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#--file-name)`=`FILE_NAME` [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#--file-format)`=`FILE_FORMAT`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies import` imports a security policy
to update an existing policy. To create a new policy from a file please use the
create command instead.

**EXAMPLES**

: To import a security policy from a YAML file run this:

```
gcloud compute security-policies import --file-name=myFile
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to import.

**REQUIRED FLAGS**

: **--file-name**:
The name of the JSON or YAML file to import the security policy config from.

**OPTIONAL FLAGS**

: **--file-format**:
The format of the file to import the security policy config from. Specify either
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
gcloud alpha compute security-policies import
```

```
gcloud beta compute security-policies import
```