# gcloud projects get-ancestors  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors](https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors)*

**NAME**

: **gcloud projects get-ancestors - get the ancestors for a project**

**SYNOPSIS**

: **`gcloud projects get-ancestors` `[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors#PROJECT_ID)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/get-ancestors#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud projects get-ancestors` displays the ancestors for a project.
Projects may be grouped under folders and an organization. This comand will
print the folder and organization hierarchy for the given project.

**EXAMPLES**

: To print the ancestors for a project with ID `my-project`, run:

```
gcloud projects get-ancestors my-project
```

**POSITIONAL ARGUMENTS**

: **Project resource - The project for which to display ancestors. This represents a
Cloud resource.
This must be specified.

**`PROJECT_ID`**:
ID of the project or fully qualified identifier for the project.
To set the `project_id` attribute:

- provide the argument `project_id` on the command line.**

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

**API REFERENCE**

: This command uses the `cloudresourcemanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/resource-manager](https://cloud.google.com/resource-manager)

**NOTES**

: These variants are also available:

```
gcloud alpha projects get-ancestors
```

```
gcloud beta projects get-ancestors
```