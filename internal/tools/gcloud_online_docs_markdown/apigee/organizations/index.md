# gcloud apigee organizations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/organizations](https://cloud.google.com/sdk/gcloud/reference/apigee/organizations)*

**NAME**

: **gcloud apigee organizations - manage Apigee organizations**

**SYNOPSIS**

: **`gcloud apigee organizations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/apigee/organizations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/organizations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Apigee organizations.
`gcloud apigee organizations` contains commands for managing Apigee
organizations, the highest-level grouping of Apigee objects. All API proxies,
environments, and so forth each belong to one organization.
Apigee organizations are distinct from Cloud Platform organizations, being more
similar to Cloud Platform projects in scope and purpose.

**EXAMPLES**

: To list all accessible organizations and their associated Cloud Platform
projects, run:

```
gcloud apigee organizations list
```

To get a JSON array of all organizations whose Cloud Platform project names
contain the word ``sandbox``, run:

```
gcloud apigee organizations list --format=json --filter="project:(sandbox)"
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list](https://cloud.google.com/sdk/gcloud/reference/apigee/organizations/list)`**:
List Apigee organizations and their paired Cloud Platform projects.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee organizations
```

```
gcloud beta apigee organizations
```