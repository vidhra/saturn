# gcloud pubsub schemas  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas)*

**NAME**

: **gcloud pubsub schemas - manage Pub/Sub schemas**

**SYNOPSIS**

: **`gcloud pubsub schemas` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud pubsub schemas group lets you create and manage Pub/Sub schemas.
These schemas can be attached to topics to enable validation of published
messages. Commands to validate schemas and messages against schemas are also
available.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[commit](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/commit)`**:
Commit a Pub/Sub schema revision.

**`[create](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/create)`**:
Create a Pub/Sub schema.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/delete)`**:
Delete a Pub/Sub schema.

**`[delete-revision](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/delete-revision)`**:
Delete a Pub/Sub schema revision.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/describe)`**:
Show details of a Pub/Sub schema.

**`[list](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list)`**:
List Pub/Sub schemas.

**`[list-revisions](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/list-revisions)`**:
List revisions of a Pub/Sub schema.

**`[rollback](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/rollback)`**:
Roll back a Pub/Sub schema to a specified revision.

**`[validate-message](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-message)`**:
Validate a message against a Pub/Sub schema.

**`[validate-schema](https://cloud.google.com/sdk/gcloud/reference/pubsub/schemas/validate-schema)`**:
Validate a Pub/Sub schema.

**NOTES**

: These variants are also available:

```
gcloud alpha pubsub schemas
```

```
gcloud beta pubsub schemas
```