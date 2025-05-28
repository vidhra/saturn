# gcloud vmware dns-bind-permission describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/describe)*

**NAME**

: **gcloud vmware dns-bind-permission describe - get all users and service accounts having bind permission**

**SYNOPSIS**

: **`gcloud vmware dns-bind-permission describe` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/dns-bind-permission/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Gets all the users and service accounts having bind permission on the intranet
VPC associated with the consumer project granted by the Grant API.

**EXAMPLES**

: To get all the users and service accounts having bind permission on the intranet
VPC associated with the consumer project `my-project`, run:

```
gcloud vmware dns-bind-permission describe --project=my-project
```

```
Or:
```

```
gcloud vmware dns-bind-permission describe
```

In the second example, the project is taken from gcloud properties core/project.

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