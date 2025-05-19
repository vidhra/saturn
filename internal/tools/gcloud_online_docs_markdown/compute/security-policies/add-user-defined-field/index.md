# gcloud compute security-policies add-user-defined-field  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field)*

**NAME**

: **gcloud compute security-policies add-user-defined-field - add a user defined field to a Compute Engine security policy**

**SYNOPSIS**

: **`gcloud compute security-policies add-user-defined-field` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#NAME)` `[--base](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--base)`=`BASE` `[--offset](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--offset)`=`OFFSET` `[--size](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--size)`=`SIZE` `[--user-defined-field-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--user-defined-field-name)`=`USER_DEFINED_FIELD_NAME` [`[--mask](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--mask)`=`MASK`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies add-user-defined-field` is used to
add user defined fields to security policies.

**EXAMPLES**

: To add a user defined field run this:

```
gcloud compute security-policies add-user-defined-field SECURITY_POLICY --user-defined-field-name=my-field --base=ipv6 --offset=10 --size=3
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the security policy to update.

**REQUIRED FLAGS**

: **--base**:
The base relative to which offset is measured. `BASE` must
be one of: `ipv4`, `ipv6`, `tcp`,
`udp`.

**--offset**:
Offset of the first byte of the field (in network byte order) relative to base.

**--size**:
Size of the field in bytes. Valid values: 1-4.

**--user-defined-field-name**:
The name for the user defined field.

**OPTIONAL FLAGS**

: **--mask**:
If specified, apply this mask (bitwise AND) to the field to ignore bits before
matching. Encoded as a hexadecimal number (starting with "0x").

**--region**:
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
gcloud alpha compute security-policies add-user-defined-field
```

```
gcloud beta compute security-policies add-user-defined-field
```