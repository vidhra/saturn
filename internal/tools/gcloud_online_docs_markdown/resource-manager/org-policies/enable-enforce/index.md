# gcloud resource-manager org-policies enable-enforce  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce)*

**NAME**

: **gcloud resource-manager org-policies enable-enforce - turns on enforcement of boolean Organization Policy constraint**

**SYNOPSIS**

: **`gcloud resource-manager org-policies enable-enforce` `[ORG_POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce#ORG_POLICY_ID)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Turns on enforcement of a boolean Organization Policy constraint at the
specified resource.

**EXAMPLES**

: The following command enables enforcement of the Organization Policy boolean
constraint `compute.disableSerialPortAccess` on project
`foo-project`:

```
gcloud resource-manager org-policies enable-enforce compute.disableSerialPortAccess --project=foo-project
```

**POSITIONAL ARGUMENTS**

: **`ORG_POLICY_ID`**:
The Org Policy constraint name.

**REQUIRED FLAGS**

: **--folder**

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
gcloud alpha resource-manager org-policies enable-enforce
```

```
gcloud beta resource-manager org-policies enable-enforce
```