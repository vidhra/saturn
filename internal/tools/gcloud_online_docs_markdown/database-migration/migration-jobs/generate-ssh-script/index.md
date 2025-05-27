# gcloud database-migration migration-jobs generate-ssh-script  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script)*

**NAME**

: **gcloud database-migration migration-jobs generate-ssh-script - generate a SSH script for a Database Migration Service migration job**

**SYNOPSIS**

: **`gcloud database-migration migration-jobs generate-ssh-script` (`[MIGRATION_JOB](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#MIGRATION_JOB)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--region)`=`REGION`) `[--vm](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--vm)`=`VM` (`[--vm-zone](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--vm-zone)`=`VM_ZONE`     | [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--subnet)`=`SUBNET` `[--vm-machine-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--vm-machine-type)`=`VM_MACHINE_TYPE` : `[--vm-zone-create](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--vm-zone-create)`=`VM_ZONE_CREATE`]) [`[--vm-port](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#--vm-port)`=`VM_PORT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/migration-jobs/generate-ssh-script#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Generate a script for a Database Migration Service migration job, to configure
Reverse SSH tunnel connectivity with a bastion host on a Compute Engine VM
instance. You can use an existing VM instance or create a new VM for this
purpose.
Copy the generated script and run it in bash from a machine that has:

- The gcloud command-line tool installed.
- Access to your source database.
- Access to the existing bastion VM, or permissions and access to the Cloud
Compute API if creating a new bastion VM. Make sure this machine is available
during the entire migration.

Running the script will set up the SSH tunnel on the VM you selected and will
establish connectivity between the source database and the Cloud SQL instance.
Find additional information [here](https://cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel).

**EXAMPLES**

: To generate an SSH script with bastion VM instance creation:

```
gcloud database-migration migration-jobs generate-ssh-script my-migration-job --vm=vm1 --vm-port=1111 --vm-machine-type=n1-standard-1 --vm-zone-create=us-central1-a --subnet=sample-subnet --region=us-central1
```

To generate an SSH script with an existing bastion VM instance:

```
gcloud database-migration migration-jobs generate-ssh-script my-migration-job --vm=vm1 --vm-port=1111 --vm-zone=us-central1-a --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Migration job resource - The migration job to generate the SSH script for. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `migration_job` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MIGRATION_JOB`**:
ID of the migration_job or fully qualified identifier for the migration_job.
To set the `migration_job` attribute:

- provide the argument `migration_job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the region.
To set the `region` attribute:

- provide the argument `migration_job` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--vm**:
Bastion Compute Engine VM instance name to use or to create.

**--vm-zone**

**OPTIONAL FLAGS**

: **--vm-port**:
Port that will be open on the bastion host.

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

**API REFERENCE**

: This command uses the `datamigration/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/database-migration/](https://cloud.google.com/database-migration/)

**NOTES**

: This variant is also available:

```
gcloud alpha database-migration migration-jobs generate-ssh-script
```