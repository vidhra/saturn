# gcloud artifacts rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/rules](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules)*

**NAME**

: **gcloud artifacts rules - manage Artifact Registry rules**

**SYNOPSIS**

: **`gcloud artifacts rules` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To list all rules in the current project and `artifacts/repository`
and `artifacts/location` properties are set, run:

```
gcloud artifacts rules list
```

To list rules under repository my-repo in the current project and location, run:

```
gcloud artifacts rules list --repository=my-repo
```

To delete rule `my-rule` under repository my-repo in the current
project and location, run:

```
gcloud artifacts rules delete my-rule --repository=my-repo
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/create)`**:
Create an Artifact Registry rule.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete)`**:
Delete an Artifact Registry rule.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/describe)`**:
Describe an Artifact Registry rule.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/list)`**:
List Artifact Registry rules.

**`[update](https://cloud.google.com/sdk/gcloud/reference/artifacts/rules/update)`**:
Update an Artifact Registry rule.