# gcloud apigee developers describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe)*

**NAME**

: **gcloud apigee developers describe - describe an Apigee developer**

**SYNOPSIS**

: **`gcloud apigee developers describe` (`[DEVELOPER](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe#DEVELOPER)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Apigee developer.
`gcloud apigee developers describe` retrieves the developer's
details, including the developer's name, email address, apps, and other
information.

**EXAMPLES**

: To describe a developer for the active Cloud Platform project whose email
address is ``larry@example.com``, run:

```
gcloud apigee developers describe larry@example.com
```

To describe that developer in the Apigee organization
``my-org``, formatted as a JSON object, run:

```
gcloud apigee developers describe larry@example.com --organization=my-org --format=json
```

**POSITIONAL ARGUMENTS**

: **Developer resource - Email address of the developer to be described. To get a
list of available developers, run `[gcloud apigee developers
list](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/list)`. The arguments in this group can be used to specify the
attributes of this resource.
This must be specified.

**`DEVELOPER`**:
ID of the developer or fully qualified identifier for the developer.
To set the `developer` attribute:

- provide the argument `DEVELOPER` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Apigee organization containing the developer. If unspecified, the Cloud Platform
project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `DEVELOPER` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

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
gcloud alpha apigee developers describe
```

```
gcloud beta apigee developers describe
```