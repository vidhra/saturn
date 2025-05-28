# gcloud vmware dns-bind-permission revoke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke)*

**NAME**

: **gcloud vmware dns-bind-permission revoke - revokes a DNS Bind Permission**

**SYNOPSIS**

: **`gcloud vmware dns-bind-permission revoke` (`[--service-account](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke#--service-account)`=`SERVICE_ACCOUNT`     | `[--user](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke#--user)`=`USER`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/revoke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Revokes the bind permission from the customer provided user/service account on
the intranet VPC associated with the consumer project.

**EXAMPLES**

: To revoke the bind permission to the customer provided user
`user@abc.com` on the intranet VPC associated with the consumer
project `my-project`, run:

```
gcloud vmware dns-bind-permission revoke --user=user@abc.com --project=my-project
```

Or:

```
gcloud vmware dns-bind-permission revoke --user=user@abc.com
```

In the second example, the project is taken from gcloud properties core/project.
To revoke the bind permission to the customer provided service account
`service-account@gserviceaccount.com` on the intranet VPC associated
with the consumer project `my-project`, run:

```
gcloud vmware dns-bind-permission revoke --service-account=service-account@gserviceaccount.com --project=my-project
```

Or:

```
gcloud vmware dns-bind-permission revoke --service-account=service-account@gserviceaccount.com
```

In the second example, the project is taken from gcloud properties core/project.

**REQUIRED FLAGS**

: **--service-account**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

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