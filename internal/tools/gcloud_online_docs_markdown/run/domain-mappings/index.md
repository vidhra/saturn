# gcloud run domain-mappings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings)*

**NAME**

: **gcloud run domain-mappings - view and manage your Cloud Run for Anthos domain mappings**

**SYNOPSIS**

: **`gcloud run domain-mappings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your service's domain
mappings.
To view and manage fully managed Cloud Run domain mappings, use `[gcloud beta run
domain-mappings](https://cloud.google.com/sdk/gcloud/reference/beta/run/domain-mappings)`.

**EXAMPLES**

: To list your Cloud Run domain mappings, run:

```
gcloud run domain-mappings list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create)`**:
Create domain mappings for Cloud Run for Anthos.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete)`**:
Delete domain mappings for Cloud Run for Anthos.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe)`**:
Describe domain mappings for Cloud Run for Anthos.

**`[list](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/list)`**:
Lists domain mappings for Cloud Run for Anthos.

**NOTES**

: These variants are also available:

```
gcloud alpha run domain-mappings
```

```
gcloud beta run domain-mappings
```