# gcloud container binauthz attestors create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create)*

**NAME**

: **gcloud container binauthz attestors create - create an Attestor**

**SYNOPSIS**

: **`gcloud container binauthz attestors create` `[ATTESTOR](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create#ATTESTOR)` (`[--attestation-authority-note](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create#--attestation-authority-note)`=`ATTESTATION_AUTHORITY_NOTE` : `[--attestation-authority-note-project](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create#--attestation-authority-note-project)`=`ATTESTATION_AUTHORITY_NOTE_PROJECT`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/attestors/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Attestor.

**EXAMPLES**

: To create an Attestor with an existing Note
`projects/my_proj/notes/my_note`:

```
gcloud container binauthz attestors create my_new_attestor --attestation-authority-note=my_note --attestation-authority-note-project=my_proj
```

**POSITIONAL ARGUMENTS**

: **Attestor resource - The attestor to be created. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `ATTESTOR` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ATTESTOR`**:
ID of the attestor or fully qualified identifier for the attestor.
To set the `name` attribute:

- provide the argument `ATTESTOR` on the command line.**

**REQUIRED FLAGS**

: **Note resource - The Container Analysis Note to which the created attestor will
be bound.
For the attestor to be able to access and use the Note, the Note must exist and
the active gcloud account (core/account) must have the
`containeranalysis.notes.listOccurrences` permission for the Note.
This can be achieved by granting the
`containeranalysis.notes.occurrences.viewer` role to the active
account for the Note resource in question.

```
The arguments in this group can be used to specify the attributes of this resource.
```

This must be specified.

**--attestation-authority-note**:
ID of the note or fully qualified identifier for the note.
To set the `note` attribute:

- provide the argument `--attestation-authority-note` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--attestation-authority-note-project**:
The Container Analysis project for the note.
To set the `project` attribute:

- provide the argument `--attestation-authority-note` on the command
line with a fully specified name;
- provide the argument `--attestation-authority-note-project` on the
command line.**

**OPTIONAL FLAGS**

: **--description**:
A description for the attestor

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
gcloud alpha container binauthz attestors create
```

```
gcloud beta container binauthz attestors create
```