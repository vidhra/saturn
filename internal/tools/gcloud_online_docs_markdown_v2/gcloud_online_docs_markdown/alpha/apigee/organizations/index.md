# gcloud alpha apigee organizations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations)*

**NAME**

: **gcloud alpha apigee organizations - manage Apigee organizations**

**SYNOPSIS**

: **`gcloud alpha apigee organizations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage Apigee organizations.
`gcloud alpha apigee organizations` contains commands for managing
Apigee organizations, the highest-level grouping of Apigee objects. All API
proxies, environments, and so forth each belong to one organization.
Apigee organizations are distinct from Cloud Platform organizations, being more
similar to Cloud Platform projects in scope and purpose.

**EXAMPLES**

: To list all accessible organizations and their associated Cloud Platform
projects, run:

```
gcloud alpha apigee organizations list
```

To get a JSON array of all organizations whose Cloud Platform project names
contain the word ``sandbox``, run:

```
gcloud alpha apigee organizations list --format=json --filter="project:(sandbox)"
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/delete)`**:
`(ALPHA)` Delete an Apigee organization.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/list)`**:
`(ALPHA)` List Apigee organizations and their paired Cloud Platform
projects.

**`[provision](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision)`**:
`(ALPHA)` Provision an Apigee SaaS organization.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud apigee organizations
```

```
gcloud beta apigee organizations
```