# gcloud run revisions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/revisions](https://cloud.google.com/sdk/gcloud/reference/run/revisions)*

**NAME**

: **gcloud run revisions - view and manage your Cloud Run revisions**

**SYNOPSIS**

: **`gcloud run revisions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/revisions#COMMAND)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/revisions#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/revisions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing Cloud Run
revisions.

**EXAMPLES**

: To list your existing revisions, run:

```
gcloud run revisions list
```

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/run/revisions/delete)`**:
Delete a revision.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/revisions/describe)`**:
Obtain details about revisions.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/revisions/list)`**:
List available revisions.

**NOTES**

: These variants are also available:

```
gcloud alpha run revisions
```

```
gcloud beta run revisions
```