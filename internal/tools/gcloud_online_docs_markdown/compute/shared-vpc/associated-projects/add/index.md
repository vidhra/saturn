# gcloud compute shared-vpc associated-projects add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add)*

**NAME**

: **gcloud compute shared-vpc associated-projects add - associate the given project with a given shared VPC host project**

**SYNOPSIS**

: **`gcloud compute shared-vpc associated-projects add` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add#PROJECT_ID)` `[--host-project](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add#--host-project)`=`HOST_PROJECT` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc/associated-projects/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Associate the given project with a given shared VPC host project.

**EXAMPLES**

: To add the project `service-project` as an associated service project
of the shared VPC host project `host-project`, run:

```
gcloud compute shared-vpc associated-projects add --host-project=host-project service-project
```

**POSITIONAL ARGUMENTS**

: **`PROJECT_ID`**:
ID for the project to add to the host project

**REQUIRED FLAGS**

: **--host-project**:
The XPN host to add an associated project to

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
gcloud alpha compute shared-vpc associated-projects add
```

```
gcloud beta compute shared-vpc associated-projects add
```