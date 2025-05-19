# gcloud compute firewall-policies associations create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create)*

**NAME**

: **gcloud compute firewall-policies associations create - create a new association between a firewall policy and an organization or folder resource**

**SYNOPSIS**

: **`gcloud compute firewall-policies associations create` `[--firewall-policy](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#--firewall-policy)`=`FIREWALL_POLICY` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#--folder)`=`FOLDER`] [`[--name](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#--name)`=`NAME`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#--organization)`=`ORGANIZATION`] [`[--replace-association-on-target](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#--replace-association-on-target)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/associations/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute firewall-policies associations create` is used to
create organization firewall policy associations. An organization firewall
policy is a set of rules that controls access to various resources.

**EXAMPLES**

: To associate an organization firewall policy under folder with ID ``123456789"
to folder ``987654321", run:

```
gcloud compute firewall-policies associations create --firewall-policy=123456789 --folder=987654321
```

**REQUIRED FLAGS**

: **--firewall-policy**:
Security policy ID of the association.

**OPTIONAL FLAGS**

: **--folder**:
ID of the folder with which the association is created.

**--name**:
Name to identify this association. If unspecified, the name will be set to
"organization-{ORGANIZATION_ID}" or "folder-{FOLDER_ID}".

**--organization**:
ID of the organization in which the firewall policy is to be associated. Must be
set if FIREWALL_POLICY is short name.

**--replace-association-on-target**:
By default, if you attempt to insert an association to an organization or folder
resource that is already associated with a firewall policy the method will fail.
If this is set, the existing association will be deleted at the same time that
the new association is created.

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
gcloud alpha compute firewall-policies associations create
```

```
gcloud beta compute firewall-policies associations create
```