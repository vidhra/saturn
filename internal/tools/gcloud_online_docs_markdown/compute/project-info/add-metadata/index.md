# gcloud compute project-info add-metadata  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata)*

**NAME**

: **gcloud compute project-info add-metadata - add or update project-wide metadata**

**SYNOPSIS**

: **`gcloud compute project-info add-metadata` [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-info/add-metadata#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute project-info add-metadata` can be used to add or
update project-wide metadata. Every instance has access to a metadata server
that can be used to query metadata that has been set through this tool.
Project-wide metadata entries are visible to all instances. To set metadata for
individual instances, use `[gcloud compute
instances add-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata)`. For information on metadata, see [https://cloud.google.com/compute/docs/metadata](https://cloud.google.com/compute/docs/metadata)
Only metadata keys that are provided are mutated. Existing metadata entries will
remain unaffected.
If you are using this command to manage SSH keys for your project, please note
the [risks](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#risks)
of manual SSH key management as well as the required format for SSH key
metadata, available at [https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)

**FLAGS**

: **--metadata**:
Metadata to be made available to the guest operating system running on the
instances. Each metadata entry is a key/value pair separated by an equals sign.
Each metadata key must be unique and have a max of 128 bytes in length. Each
value must have a max of 256 KB in length. Multiple arguments can be passed to
this flag, e.g., ``--metadata
key-1=value-1,key-2=value-2,key-3=value-3``. The combined
total size for all metadata entries is 512 KB.
In images that have Compute Engine tools installed on them, such as the [official images](https://cloud.google.com/compute/docs/images), the
following metadata keys have special meanings:

**`startup-script`**:
Specifies a script that will be executed by the instances once they start
running. For convenience,
``--metadata-from-file`` can be used to pull
the value from a file.

**`startup-script-url`**:
Same as ``startup-script`` except that the
script contents are pulled from a publicly-accessible location on the web.
For startup scripts on Windows instances, the following metadata keys have
special meanings:
``windows-startup-script-url``,
``windows-startup-script-cmd``,
``windows-startup-script-bat``,
``windows-startup-script-ps1``,
``sysprep-specialize-script-url``,
``sysprep-specialize-script-cmd``,
``sysprep-specialize-script-bat``, and
``sysprep-specialize-script-ps1``. For more
information, see [Running startup
scripts](https://cloud.google.com/compute/docs/startupscript).
At least one of [--metadata] or [--metadata-from-file] is required.

**--metadata-from-file**:
Same as ``--metadata`` except that the value
for the entry will be read from a local file. This is useful for values that are
too large such as ``startup-script`` contents.
At least one of [--metadata] or [--metadata-from-file] is required.

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
gcloud alpha compute project-info add-metadata
```

```
gcloud beta compute project-info add-metadata
```