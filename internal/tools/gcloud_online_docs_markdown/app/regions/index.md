# gcloud app regions  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/regions](https://cloud.google.com/sdk/gcloud/reference/app/regions)*

**NAME**

: **gcloud app regions - view regional availability of App Engine runtime environments**

**SYNOPSIS**

: **`gcloud app regions` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/regions#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/regions#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can be used to view availability of App Engine standard and
flexible runtime environments in all geographic regions.

**EXAMPLES**

: To view regional availability of App Engine runtime environments, run:

```
gcloud app regions list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list](https://cloud.google.com/sdk/gcloud/reference/app/regions/list)`**:
List the availability of flex and standard environments for each region.

**NOTES**

: This variant is also available:

```
gcloud beta app regions
```