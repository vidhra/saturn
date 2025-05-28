# gcloud alpha apigee organizations delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete)*

**NAME**

: **gcloud alpha apigee organizations delete - delete an Apigee organization**

**SYNOPSIS**

: **`gcloud alpha apigee organizations delete` `[ORGANIZATION](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete#ORGANIZATION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete an Apigee organization.
`gcloud alpha apigee organizations delete` deletes an organization
and all resources inside it. This is currently only supported for trial
organizations.
This is a long running operation. Once organization provisioning has begun,
`gcloud alpha apigee organizations delete` will exit, returning the
operation's ID and initial status. To continue monitoring the operation, run
`gcloud alpha apigee operations describe OPERATION_NAME`.

**EXAMPLES**

: To delete an organization called ``my-org``,
run:

```
gcloud alpha apigee organizations delete my-org
```

To delete an organization called ``my-org``,
and print only the name of the launched operation, run:

```
gcloud alpha apigee organizations delete my-org --format="value(name)"
```

**POSITIONAL ARGUMENTS**

: **Organization resource - The trial organization to be deleted. This represents a
Cloud resource.
This must be specified.

**`ORGANIZATION`**:
ID of the organization or fully qualified identifier for the organization.
To set the `organization` attribute:

- provide the argument `ORGANIZATION` on the command line.**

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
allowlist.