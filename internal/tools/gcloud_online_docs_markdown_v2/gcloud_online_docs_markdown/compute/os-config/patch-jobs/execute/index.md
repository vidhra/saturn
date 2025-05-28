# gcloud compute os-config patch-jobs execute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute)*

**NAME**

: **gcloud compute os-config patch-jobs execute - execute an OS patch on the specified VM instances**

**SYNOPSIS**

: **`gcloud compute os-config patch-jobs execute` (`[--instance-filter-all](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--instance-filter-all)`     | `[--instance-filter-group-labels](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--instance-filter-group-labels)`=[`KEY`=`VALUE`,…] `[--instance-filter-name-prefixes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--instance-filter-name-prefixes)`=[`INSTANCE_FILTER_NAME_PREFIXES`,…] `[--instance-filter-names](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--instance-filter-names)`=[`INSTANCE_FILTER_NAMES`,…] `[--instance-filter-zones](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--instance-filter-zones)`=[`INSTANCE_FILTER_ZONES`,…]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--display-name)`=`DISPLAY_NAME`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--dry-run)`] [`[--duration](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--duration)`=`DURATION`] [`[--mig-instances-allowed](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--mig-instances-allowed)`] [`[--reboot-config](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--reboot-config)`=`REBOOT_CONFIG`] [`[--apt-dist](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--apt-dist)` `[--apt-excludes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--apt-excludes)`=[`APT_EXCLUDES`,…]     | `[--apt-exclusive-packages](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--apt-exclusive-packages)`=[`APT_EXCLUSIVE_PACKAGES`,…]] [`[--post-patch-linux-executable](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--post-patch-linux-executable)`=`POST_PATCH_LINUX_EXECUTABLE` `[--post-patch-linux-success-codes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--post-patch-linux-success-codes)`=[`POST_PATCH_LINUX_SUCCESS_CODES`,…]] [`[--post-patch-windows-executable](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--post-patch-windows-executable)`=`POST_PATCH_WINDOWS_EXECUTABLE` `[--post-patch-windows-success-codes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--post-patch-windows-success-codes)`=[`POST_PATCH_WINDOWS_SUCCESS_CODES`,…]] [`[--pre-patch-linux-executable](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--pre-patch-linux-executable)`=`PRE_PATCH_LINUX_EXECUTABLE` `[--pre-patch-linux-success-codes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--pre-patch-linux-success-codes)`=[`PRE_PATCH_LINUX_SUCCESS_CODES`,…]] [`[--pre-patch-windows-executable](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--pre-patch-windows-executable)`=`PRE_PATCH_WINDOWS_EXECUTABLE` `[--pre-patch-windows-success-codes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--pre-patch-windows-success-codes)`=[`PRE_PATCH_WINDOWS_SUCCESS_CODES`,…]] [`[--rollout-mode](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--rollout-mode)`=`ROLLOUT_MODE` `[--rollout-disruption-budget](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--rollout-disruption-budget)`=`ROLLOUT_DISRUPTION_BUDGET`     | `[--rollout-disruption-budget-percent](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--rollout-disruption-budget-percent)`=`ROLLOUT_DISRUPTION_BUDGET_PERCENT`] [`[--windows-exclusive-patches](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--windows-exclusive-patches)`=[`WINDOWS_EXCLUSIVE_PATCHES`,…]     | `[--windows-classifications](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--windows-classifications)`=[`WINDOWS_CLASSIFICATIONS`,…] `[--windows-excludes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--windows-excludes)`=[`WINDOWS_EXCLUDES`,…]] [`[--yum-exclusive-packages](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--yum-exclusive-packages)`=[`YUM_EXCLUSIVE_PACKAGES`,…]     | `[--yum-excludes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--yum-excludes)`=[`YUM_EXCLUDES`,…] `[--yum-minimal](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--yum-minimal)` `[--yum-security](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--yum-security)`] [`[--zypper-exclusive-patches](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-exclusive-patches)`=[`ZYPPER_EXCLUSIVE_PATCHES`,…]     | `[--zypper-categories](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-categories)`=[`ZYPPER_CATEGORIES`,…] `[--zypper-excludes](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-excludes)`=[`ZYPPER_EXCLUDES`,…] `[--zypper-severities](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-severities)`=[`ZYPPER_SEVERITIES`,…] `[--zypper-with-optional](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-with-optional)` `[--zypper-with-update](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#--zypper-with-update)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Execute an OS patch on the specified VM instances.

**EXAMPLES**

: To start a patch job named `my patch job` that patches all instances
in the current project, run:

```
gcloud compute os-config patch-jobs execute --display-name="my patch job" --instance-filter-all
```

To patch an instance named `instance-1` in the
`us-east1-b` zone, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-names="zones/us-east1-b/instances/instance-1"
```

To patch all instances in the `us-central1-b` and
`europe-west1-d` zones, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-zones="us-central1-b,europe-west1-d"
```

To patch all instances where the `env` label is `test` and
`app` label is `web`, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-group-labels="env=test,app=web"
```

To patch all instances where the `env` label is `test` and
`app` label is `web` or where the `env` label
is `staging` and `app` label is `web`, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-group-labels="env=test,app=web" --instance-filter-group-labels="env=staging,app=web"
```

To apply security and critical patches to Windows instances with the prefix
`windows-` in the instance name, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-name-prefixes="windows-" --windows-classifications=SECURITY,CRITICAL
```

To update only `KB4339284` on Windows instances with the prefix
`windows-` in the instance name, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-name-prefixes="windows-" --windows-exclusive-patches=4339284
```

To patch all instances in the current project and specify scripts to run
pre-patch and post-patch, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-all --pre-patch-linux-executable="/bin/script" --pre-patch-linux-success-codes=0,200 --pre-patch-windows-executable="C:\Users\user\script.ps1" --post-patch-linux-executable="gs://my-bucket/linux-script#123" --post-patch-windows-executable="gs://my-bucket/windows-script#678"
```

To patch all instances zone-by-zone with no more than 50 percent of the
instances in the same zone disrupted at a given time, run:

```
gcloud compute os-config patch-jobs execute --instance-filter-all --rollout-mode=zone-by-zone --rollout-disruption-budget-percent=50
```

**REQUIRED FLAGS**

: **--instance-filter-all**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Textual description of the patch job.

**--display-name**:
Display name for this patch job. This does not have to be unique.

**--dry-run**:
Whether to execute this patch job as a dry run. If this patch job is a dry run,
instances are contacted, but the patch is not run.

**--duration**:
Total duration in which the patch job must complete. If the patch does not
complete in this time, the process times out. While some instances might still
be running the patch, they will not continue to work after completing the
current step. See $ [gcloud topic
datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on specifying absolute time durations.
If unspecified, the job stays active until all instances complete the patch.

**--mig-instances-allowed**:
If set, patching of VMs that are part of a managed instance group (MIG) is
allowed.

**--reboot-config**:
Post-patch reboot settings. `REBOOT_CONFIG` must be one
of:

**`always`**:
Always reboot the machine after the update completes.

**`default`**:
The agent decides if a reboot is necessary by checking signals such as registry
keys or '/var/run/reboot-required'.

**`never`**:
Never reboot the machine after the update completes.

**--apt-dist**

**--post-patch-linux-executable**

**--post-patch-windows-executable**

**--pre-patch-linux-executable**

**--pre-patch-windows-executable**

**--rollout-mode**

**--windows-exclusive-patches**

**--yum-exclusive-packages**

**--zypper-exclusive-patches**

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

: This variant is also available:

```
gcloud beta compute os-config patch-jobs execute
```