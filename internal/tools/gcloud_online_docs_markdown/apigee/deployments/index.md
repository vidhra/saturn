# gcloud apigee deployments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/deployments](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments)*

**NAME**

: **gcloud apigee deployments - manage deployments of Apigee API proxies in runtime environments**

**SYNOPSIS**

: **`gcloud apigee deployments` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage deployments of Apigee API proxies in runtime environments.
`gcloud apigee deployments` contains commands for enumerating and
checking the status of deployments of proxies to runtime environments.

**EXAMPLES**

: To list all deployments for the active Cloud Platform project, run:

```
gcloud apigee deployments list
```

To list all deployments in a particular environment of a particular Apigee
organization, run:

```
gcloud apigee deployments list --environment=ENVIRONMENT --organization=ORG_NAME
```

To get the status of a specific deployment as a JSON object, run:

```
gcloud apigee deployments describe --api=API_NAME --environment=ENVIRONMENT --format=json
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments/describe)`**:
Describe an Apigee API proxy deployment.

**`[list](https://cloud.google.com/sdk/gcloud/reference/apigee/deployments/list)`**:
List Apigee API proxy deployments.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee deployments
```

```
gcloud beta apigee deployments
```