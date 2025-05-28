# gcloud run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run](https://cloud.google.com/sdk/gcloud/reference/run)*

**NAME**

: **gcloud run - manage your Cloud Run applications**

**SYNOPSIS**

: **`gcloud run` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/run#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/run#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud run command group lets you deploy container images to Google Cloud
Run.

**EXAMPLES**

: To deploy your container, use the `[gcloud run deploy](https://cloud.google.com/sdk/gcloud/reference/run/deploy)` command:

```
gcloud run deploy <service-name> --image <image_name>
```

For more information, run:
```
gcloud run deploy --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[domain-mappings](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings)`**:
View and manage your Cloud Run for Anthos domain mappings.

**`[jobs](https://cloud.google.com/sdk/gcloud/reference/run/jobs)`**:
View and manage your Cloud Run jobs.

**`[regions](https://cloud.google.com/sdk/gcloud/reference/run/regions)`**:
View available Cloud Run (fully managed) regions.

**`[revisions](https://cloud.google.com/sdk/gcloud/reference/run/revisions)`**:
View and manage your Cloud Run revisions.

**`[services](https://cloud.google.com/sdk/gcloud/reference/run/services)`**:
View and manage your Cloud Run services.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/run/deploy)`**:
Create or update a Cloud Run service.

**NOTES**

: These variants are also available:

```
gcloud alpha run
```

```
gcloud beta run
```