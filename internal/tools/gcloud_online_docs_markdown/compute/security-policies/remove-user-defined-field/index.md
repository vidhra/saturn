# gcloud compute security-policies remove-user-defined-field  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field)*

**NAME**

: **gcloud compute security-policies remove-user-defined-field - remove a user defined field from a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies remove-user-defined-field` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field#NAME)` `[--user-defined-field-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field#--user-defined-field-name)`=`USER_DEFINED_FIELD_NAME` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies remove-user-defined-field` is used
to remove user defined fields from security policies.

**EXAMPLES**

: To remove a user defined field run this:

```
gcloud compute security-policies remove-user-defined-field SECURITY_POLICY --user-defined-field-name=my-field
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to update.

**REQUIRED FLAGS**

: **--user-defined-field-name**:
The name of the user defined field to remove.

**OPTIONAL FLAGS**

: **--region**:
Region of the security policy to update. Overrides the default
`compute/region` property value for this command invocation.

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
gcloud alpha compute security-policies remove-user-defined-field
```

```
gcloud beta compute security-policies remove-user-defined-field
```