# gcloud composer environments storage dags export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export)*

**NAME**

: **gcloud composer environments storage dags export - export DAGs from an environment into local storage or Cloud Storage**

**SYNOPSIS**

: **`gcloud composer environments storage dags export` `[--destination](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export#--destination)`=`DESTINATION` (`[--environment](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export#--environment)`=`ENVIRONMENT` : `[--location](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export#--location)`=`LOCATION`) [`[--source](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If the SOURCE is a directory, it and its contents are are exported recursively.
If no SOURCE is provided, the entire contents of the environment's DAGs
directory will be exported. Colliding files in the DESTINATION will be
overwritten. If a file exists in the DESTINATION but there is no corresponding
file to overwrite it, it is untouched.

**EXAMPLES**

: Suppose the environment `myenv`'s Cloud Storage bucket has the
following structure:

```
gs://the-bucket
|
+-- dags
|   |
|   +-- file1.py
|   +-- file2.py
|   |
|   +-- subdir1
|   |   |
|   |   +-- file3.py
|   |   +-- file4.py
```

And the local directory '/foo' has the following structure:

```
/foo
|
+-- file1.py
+-- fileX.py
|   |
|   +-- subdir1
|   |   |
|   |   +-- file3.py
|   |   +-- fileY.py
```

The following command:

```
gcloud composer environments storage dags export myenv --destination=/foo
```

would result in the following structure in the local '/foo' directory:

```
/foo
|
+-- file1.py
+-- file2.py
+-- fileX.py
|   |
|   +-- subdir1
|   |   |
|   |   +-- file3.py
|   |   +-- file4.py
|   |   +-- fileY.py
```

The local files '/foo/file1.py' and '/foo/subdir1/file3.py' will be overwritten
with the contents of the corresponding files in the Cloud Storage bucket.
If instead we had run

```
gcloud composer environments storage dags export myenv --source=subdir1/file3.py --destination=/foo
```

the resulting local directory structure would be the following:

```
/foo
|
+-- file1.py
+-- file3.py
+-- fileX.py
|   |
|   +-- subdir1
|   |   |
|   |   +-- file3.py
|   |   +-- fileY.py
```

No local files would be overwritten since
'gs://the-bucket/dags/subdir1/file3.py' was written to '/foo/file3.py' instead
of 'foo/subdir1/file3.py'.

**REQUIRED FLAGS**

: **--destination**:
The path to an existing local directory or a Cloud Storage bucket/directory into
which to export files.

**Environment resource - The environment from whose Cloud Storage bucket to export
DAGs. The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--environment**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `--environment` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

**OPTIONAL FLAGS**

: **--source**:
An optional relative path to a file or directory to be exported from the dags/
subdirectory in the environment's Cloud Storage bucket.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha composer environments storage dags export
```

```
gcloud beta composer environments storage dags export
```