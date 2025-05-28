# gcloud alpha apigee applications describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe)*

**NAME**

: **gcloud alpha apigee applications describe - describe an Apigee application**

**SYNOPSIS**

: **`gcloud alpha apigee applications describe` (`[APPLICATION](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe#APPLICATION)` : `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe an Apigee application.
`gcloud alpha apigee applications describe` retrieves the
application's details, including its developer, credentials, API products, and
other information.

**EXAMPLES**

: To describe an application for the active Cloud Platform project whose UUID is
``46d6151e-0000-4dfa-b9c7-c03b8b58bb2f``, run:

```
gcloud alpha apigee applications describe 46d6151e-0000-4dfa-b9c7-c03b8b58bb2f
```

To describe that application in the Apigee organization
``my-org``, formatted as a JSON object, run:

```
gcloud alpha apigee applications describe 46d6151e-0000-4dfa-b9c7-c03b8b58bb2f --organization=my-org --format=json
```

**POSITIONAL ARGUMENTS**

: **Application resource - Application to be described. To get a list of available
applications, run `[gcloud alpha apigee
applications list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/applications/list)`. The arguments in this group can be used to specify
the attributes of this resource.
This must be specified.

**`APPLICATION`**:
ID of the application or fully qualified identifier for the application.
To set the `app` attribute:

- provide the argument `APPLICATION` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--organization**:
Apigee organization containing the application. If unspecified, the Cloud
Platform project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `APPLICATION` on the command line with a fully
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee applications describe
```

```
gcloud beta apigee applications describe
```