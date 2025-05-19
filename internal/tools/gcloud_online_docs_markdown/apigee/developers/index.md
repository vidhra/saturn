# gcloud apigee developers  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apigee/developers](https://cloud.google.com/sdk/gcloud/reference/apigee/developers)*

**NAME**

: **gcloud apigee developers - manage Apigee developers**

**SYNOPSIS**

: **`gcloud apigee developers` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/apigee/developers#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apigee/developers#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Apigee developers.
`gcloud apigee developers` manages developers that want to use APIs
exposed via Apigee in their applications.

**EXAMPLES**

: To list the email addresses of all the developers in the active Cloud Platform
project, run:

```
gcloud apigee developers list
```

To get that list as a JSON array and only include developers with
``example.com`` addresses, run:

```
gcloud apigee developers list --format=json --filter="email:(@example.com)"
```

To get details about a specific developer in the active Cloud Platform project,
run:

```
gcloud apigee developers describe DEVELOPER_EMAIL
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/describe)`**:
Describe an Apigee developer.

**`[list](https://cloud.google.com/sdk/gcloud/reference/apigee/developers/list)`**:
List Apigee developers by email address.

**NOTES**

: These variants are also available:

```
gcloud alpha apigee developers
```

```
gcloud beta apigee developers
```