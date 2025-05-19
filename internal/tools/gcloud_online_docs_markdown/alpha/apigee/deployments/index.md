# gcloud alpha apigee deployments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments)*

**NAME**

: **gcloud alpha apigee deployments - manage deployments of Apigee API proxies in runtime environments**

**SYNOPSIS**

: **`gcloud alpha apigee deployments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage deployments of Apigee API proxies in runtime
environments.
`gcloud alpha apigee deployments` contains commands for enumerating
and checking the status of deployments of proxies to runtime environments.

**EXAMPLES**

: To list all deployments for the active Cloud Platform project, run:

```
gcloud alpha apigee deployments list
```

To list all deployments in a particular environment of a particular Apigee
organization, run:

```
gcloud alpha apigee deployments list --environment=ENVIRONMENT --organization=ORG_NAME
```

To get the status of a specific deployment as a JSON object, run:

```
gcloud alpha apigee deployments describe --api=API_NAME --environment=ENVIRONMENT --format=json
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/describe)`**:
`(ALPHA)` Describe an Apigee API proxy deployment.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list)`**:
`(ALPHA)` List Apigee API proxy deployments.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee deployments
```

```
gcloud beta apigee deployments
```