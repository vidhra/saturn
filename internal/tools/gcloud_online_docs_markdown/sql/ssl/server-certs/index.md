# gcloud sql ssl server-certs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs)*

**NAME**

: **gcloud sql ssl server-certs - provide commands for managing server certificates of Cloud SQL instances**

**SYNOPSIS**

: **`gcloud sql ssl server-certs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Provide commands for managing server certificates of Cloud SQL instances,
including creating, listing, rotating in, and rolling back certificates.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/create)`**:
Create a server certificate for a Cloud SQL instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/list)`**:
List all server certificates for a Cloud SQL instance.

**`[rollback](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/rollback)`**:
Roll back to the previous server certificate for a Cloud SQL instance.

**`[rotate](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/rotate)`**:
Rotate in the upcoming server certificate for a Cloud SQL instance.

**NOTES**

: These variants are also available:

```
gcloud alpha sql ssl server-certs
```

```
gcloud beta sql ssl server-certs
```