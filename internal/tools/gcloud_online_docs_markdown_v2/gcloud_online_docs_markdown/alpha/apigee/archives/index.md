# gcloud alpha apigee archives  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives)*

**NAME**

: **gcloud alpha apigee archives - manage Apigee archive deployments**

**SYNOPSIS**

: **`gcloud alpha apigee archives` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Apigee archive deployments.

**EXAMPLES**

: To deploy a local archive deployment remotely to the management plane in the
``test`` environment, run:

```
gcloud alpha apigee archives deploy --environment=test
```

To list all archive deployments in the ``dev``
environment, run:

```
gcloud alpha apigee archives list --environment=dev
```

To describe the archive deployment with id
``abcdef01234`` in the
``demo`` environment of the
``my-org`` Apigee organization, run:

```
gcloud alpha apigee archives describe abcdef01234 --environment=demo --organization=my-org
```

To update the labels of the archive deployment with id
``uvxwzy56789`` in the
``test`` environment, run:

```
gcloud alpha apigee archives update uvxwzy56789 --environment=demo --update-labels=foo=1,bar=2
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/delete)`**:
`(ALPHA)` Delete an Apigee archive deployment.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/deploy)`**:
`(ALPHA)` Deploy an Apigee archive deployment to an environment.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/describe)`**:
`(ALPHA)` Describe an Apigee archive deployment.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/list)`**:
`(ALPHA)` List Apigee archive deployments.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/archives/update)`**:
`(ALPHA)` Update an existing Apigee archive deployment.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta apigee archives
```