# gcloud alpha apigee archives update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update)*

**NAME**

: **gcloud alpha apigee archives update - update an existing Apigee archive deployment**

**SYNOPSIS**

: **`gcloud alpha apigee archives update` (`[ARCHIVE_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#ARCHIVE_DEPLOYMENT)` : `[--environment](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#--environment)`=`ENVIRONMENT` `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#--organization)`=`ORGANIZATION`) [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update an existing Apigee archive deployment.
`gcloud alpha apigee archives update` updates an Apigee archive
deployment.

**EXAMPLES**

: To update the ``tag`` and
``rev`` labels of an archive deployment with
the id ``abcdef01234`` in the Apigee
environment called ``my-env`` using the active
Cloud Platform project, run:

```
gcloud alpha apigee archives update abcdef01234 --environment=my-env --update-labels=tag=my-tag,rev=1234
```

To remove the ``dev`` label on an archive
deployment with the id ``uvwxyz56789``, in the
Apigee environment called ``my-env``, in an
organization called ``my-org``, run:

```
gcloud alpha apigee archives update uvwxyz56789 --environment=my-env --organization=my-org --remove-labels=dev
```

To clear all labels on an archive deployment with the id
``mnop4321``, in the Apigee environment called
``my-env``, in an organization called
``my-org``, and return the updated archive
deployment as a JSON object, run:

```
gcloud alpha apigee archives update mnop4321 --environment=my-env --organization=my-org --clear-labels --format=json
```

**POSITIONAL ARGUMENTS**

: **Archive deployment resource - Archive deployment to update. To get a list of
existing archive deployments, run `[gcloud alpha apigee
archives list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/list)`. The arguments in this group can be used to specify the
attributes of this resource.
This must be specified.

**`ARCHIVE_DEPLOYMENT`**:
ID of the archive deployment or fully qualified identifier for the archive
deployment.
To set the `archive_deployment` attribute:

- provide the argument `archive_deployment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--environment**:
Deployment environment of the archive deployment.
To set the `environment` attribute:

- provide the argument `archive_deployment` on the command line with a
fully specified name;
- provide the argument `--environment` on the command line.

**--organization**:
Apigee organization containing the archive deployment. If unspecified, the Cloud
Platform project's associated organization will be used.
To set the `organization` attribute:

- provide the argument `archive_deployment` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line;
- set the property [project] or provide the argument [--project] on the command
line, using a Cloud Platform project with an associated Apigee organization.**

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
allowlist. This variant is also available:

```
gcloud beta apigee archives update
```