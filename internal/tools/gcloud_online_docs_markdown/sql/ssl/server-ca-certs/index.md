# gcloud sql ssl server-ca-certs  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs)*

**NAME**

: **gcloud sql ssl server-ca-certs - provide commands for managing server CA certs of Cloud SQL instances**

**SYNOPSIS**

: **`gcloud sql ssl server-ca-certs` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Provide commands for managing server CA certs of Cloud SQL instances, including
creating, listing, rotating in, and rolling back certs.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create)`**:
Create a server CA cert for a Cloud SQL instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/list)`**:
List all server CA certs for a Cloud SQL instance.

**`[rollback](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/rollback)`**:
Roll back to the previous server CA cert for a Cloud SQL instance.

**`[rotate](https://cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/rotate)`**:
Rotate in the upcoming server CA cert for a Cloud SQL instance.

**NOTES**

: These variants are also available:

```
gcloud alpha sql ssl server-ca-certs
```

```
gcloud beta sql ssl server-ca-certs
```