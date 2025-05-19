# gcloud compute security-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create)*

**NAME**

: **gcloud compute security-policies create - create a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--description)`=`DESCRIPTION`] [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--file-format)`=`FILE_FORMAT`] [`[--file-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--file-name)`=`FILE_NAME`     | `[--type](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--type)`=`SECURITY_POLICY_TYPE`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies create` is used to create security
policies. A security policy policy is a set of rules that controls access to
various resources.

**EXAMPLES**

: To create a security policy with a given type and description, run:

```
gcloud compute security-policies create my-policy --type=CLOUD_ARMOR_EDGE --description="policy description"
```

To create a security from an input file, run:

```
gcloud compute security-policies create my-policy --file-name=my-file-name
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to create.

**FLAGS**

: **--description**:
An optional, textual description for the security policy.

**--file-format**:
The format of the file to create the security policy config from. Specify either
yaml or json. Defaults to yaml if not specified. Will be ignored if --file-name
is not specified. `FILE_FORMAT` must be one of:
`json`, `yaml`.

**--file-name**

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
gcloud alpha compute security-policies create
```

```
gcloud beta compute security-policies create
```