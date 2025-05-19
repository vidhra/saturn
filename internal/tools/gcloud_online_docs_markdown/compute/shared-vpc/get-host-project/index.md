# gcloud compute shared-vpc get-host-project  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/get-host-project](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/get-host-project)*

**NAME**

: **gcloud compute shared-vpc get-host-project - get the shared VPC host project that the given project is associated with**

**SYNOPSIS**

: **`gcloud compute shared-vpc get-host-project` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/get-host-project#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/get-host-project#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the shared VPC host project that the given project is associated with.

**EXAMPLES**

: If `service-project1` and `service-project2` are
associated service projects of the shared VPC host project
`host-project`,

```
gcloud compute shared-vpc get-host-project service-project1
```

will show the `host-project` project.

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
ID for the project to get the host project for

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
gcloud alpha compute shared-vpc get-host-project
```

```
gcloud beta compute shared-vpc get-host-project
```