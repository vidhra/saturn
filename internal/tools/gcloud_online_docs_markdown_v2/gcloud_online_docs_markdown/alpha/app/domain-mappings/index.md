# gcloud alpha app domain-mappings  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings)*

**NAME**

: **gcloud alpha app domain-mappings - view and manage your App Engine domain mappings**

**SYNOPSIS**

: **`gcloud alpha app domain-mappings` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This set of commands can be used to view and manage your
app's domain mappings.
App Engine Domain Mappings allow an application to be served via one or many
custom domains, such as `example.com`, instead of the default
`https://<PROJECT-ID>.<REGION-ID>.r.appspot.com` address.
You can use a custom domain with or without SSL.
Use the AUTOMATIC management type to automatically provision an SSL certificate
for your domain. Use the MANUAL management type to provide your own certificate
or omit SSL.

**EXAMPLES**

: To list your App Engine domains, run:

```
gcloud alpha app domain-mappings list
```

To create a domain with an automatically managed certificate, run:

```
gcloud alpha app domain-mappings create 'example.com' --certificate-management=AUTOMATIC
```

To create a domain with a manual certificate, run:

```
gcloud alpha app domain-mappings create 'example.com' --certificate-management=manual --certificate-id=1234
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/create)`**:
`(ALPHA)` Creates a domain mapping.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/delete)`**:
`(ALPHA)` Deletes a specified domain mapping.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/describe)`**:
`(ALPHA)` Describes a specified domain mapping.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/list)`**:
`(ALPHA)` Lists domain mappings.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/app/domain-mappings/update)`**:
`(ALPHA)` Updates a domain mapping.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud app domain-mappings
```

```
gcloud beta app domain-mappings
```