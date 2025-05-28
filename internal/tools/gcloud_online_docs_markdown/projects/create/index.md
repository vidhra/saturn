# gcloud projects create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/projects/create](https://cloud.google.com/sdk/gcloud/reference/projects/create)*

**NAME**

: **gcloud projects create - create a new project**

**SYNOPSIS**

: **`gcloud projects create` [`[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/projects/create#PROJECT_ID)`] [`[--no-enable-cloud-apis](https://cloud.google.com/sdk/gcloud/reference/projects/create#--enable-cloud-apis)`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/projects/create#--folder)`=`FOLDER_ID`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/projects/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--name](https://cloud.google.com/sdk/gcloud/reference/projects/create#--name)`=`NAME`] [`[--organization](https://cloud.google.com/sdk/gcloud/reference/projects/create#--organization)`=`ORGANIZATION_ID`] [`[--set-as-default](https://cloud.google.com/sdk/gcloud/reference/projects/create#--set-as-default)`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/projects/create#--tags)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/projects/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new project with the given project ID. By default, projects are not
created under a parent resource. To do so, use either the
`--organization` or `--folder` flag.

**EXAMPLES**

: The following command creates a project with ID `example-foo-bar-1`,
name `Happy project` and label `type=happy`:

```
gcloud projects create example-foo-bar-1 --name="Happy project" --labels=type=happy
```

By default, projects are not created under a parent resource. The following
command creates a project with ID `example-2` with parent
`folders/12345`:

```
gcloud projects create example-2 --folder=12345
```

The following command creates a project with ID `example-3` with
parent `organizations/2048`:

```
gcloud projects create example-3 --organization=2048
```

**POSITIONAL ARGUMENTS**

: **[`PROJECT_ID`]**:
ID for the project you want to create.
Project IDs are immutable and can be set only during project creation. They must
start with a lowercase letter and can have lowercase ASCII letters, digits or
hyphens. Project IDs must be between 6 and 30 characters.

**FLAGS**

: **--enable-cloud-apis**:
Enable `cloudapis.googleapis.com` during creation. Enabled by
default, use `--no-enable-cloud-apis` to disable.

**--folder**:
ID for the folder to use as a parent

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--name**:
Name for the project you want to create. If not specified, will use project id
as name.

**--organization**:
ID for the organization to use as a parent

**--set-as-default**:
Set newly created project as [core/project] property.

**--tags**:
List of tags KEY=VALUE pairs to bind. Each item must be expressed as
`<tag-key-namespaced-name>=<tag-value-short-name>`.
Example: `123/environment=production,123/costCenter=marketing`
Note: Currently this field is in Preview.

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

**SEE ALSO**

: See [https://support.google.com/cloud/answer/6251787](https://support.google.com/cloud/answer/6251787)
for information on creating or deleting projects from the Google Cloud Platform
Console.

**NOTES**

: These variants are also available:

```
gcloud alpha projects create
```

```
gcloud beta projects create
```